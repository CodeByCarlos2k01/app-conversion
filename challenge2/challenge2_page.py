import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

if 'challenge2' not in st.session_state:
    st.session_state['challenge2'] = False
    st.session_state['challenge2_Vp'] = 0.0
    st.session_state['challenge2_Np'] = 0.0
    st.session_state['challenge2_freq'] = 0.0

st.title(':blue[𝐒𝐞𝐜̧𝐚̃𝐨 𝟐]')

# Título da aplicação
st.title("Corrente de Magnetização de um Transformador")
st.write('Calcular a regulação de um transformador é fundamental para garantir que ele funcione eficientemente em diversas condições de carga, assegurando a qualidade da energia, otimizando o desempenho do sistema e permitindo um planejamento de manutenção mais eficaz.')
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚')
    st.markdown('• Característica do material (Curva BxH)')
with col2:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐬𝐚𝐢́𝐝𝐚')
    st.markdown('• Curva da corrente de magnetização x tempo')
st.divider()

st.title('Dados de Entrada')
with st.form('challenge2_form'):
    # Inputs interativos no Streamlit com valores padrão usando session_state
    st.subheader('Tensão primária')
    Vp = st.number_input('Informe a Tensão Primária (Vp) em Volts', min_value=0.0)
    Vp = st.session_state['challenge2_Vp'] if Vp == 0 else Vp

    st.subheader('Frequência')
    freq = st.number_input('Informe a Frequência (Hz)', min_value=0.0)
    freq = st.session_state['challenge2_freq'] if freq == 0 else freq
    
    st.subheader('Número de espiras')
    Np = st.number_input('Informe o Número de Espiras no Primário (Np)', min_value=0.0)
    Np = st.session_state['challenge2_Np'] if Np == 0 else Np

    challenge2_button = st.form_submit_button('Gerar Resultado')

if (challenge2_button or st.session_state['challenge2']):
    st.title('Resultado')
    with st.expander('Passo a Passo da Resolução', expanded=True):
        try:
            st.session_state['challenge2'] = True
            st.session_state['challenge2_Vp'] = Vp
            st.session_state['challenge2_Np'] = Np
            st.session_state['challenge2_freq'] = freq

            # Nome do caminho do arquivo
            path = 'challenge2/models/MagCurve-3.xlsx'

            # Carregar os dados de fluxo (proporcional a B) e MMF (proporcional a H) do arquivo Excel
            data = pd.read_excel(path)
            flux_data = data['Fluxo']
            mmf_data = data['MMF']

            # Calcular a tensão máxima (pico) aplicada ao transformador
            Vm = Vp * np.sqrt(2)

            # Velocidade angular (omega) é dada por 2 * pi * frequência
            omega = 2 * np.pi * freq

            # Definir o intervalo de tempo para simulação
            t_final = 340e-3
            t_step = 1 / 3000
            time = np.arange(0, t_final, t_step)

            # Calcular fluxo magnético (proporcional a B) em função do tempo
            flux = -Vm / (omega * Np) * np.cos(omega * time)

            # Interpolação da curva BxH
            mmf = np.interp(flux, flux_data, mmf_data)

            # Calcular a corrente de magnetização (I_m)
            im = mmf / Np

            # Exibir o gráfico da corrente de magnetização
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(time * 1000, im)
            ax.set_title('Corrente de Magnetização x Tempo')
            ax.set_xlabel('Tempo (ms)')
            ax.set_ylabel('Corrente de Magnetização (A)')
            ax.grid(True)

            # Exibir o gráfico usando streamlit
            st.pyplot(fig)

            # Cálculo do valor eficaz da corrente de magnetização
            irms = np.sqrt(np.mean(im**2))

            # Exibir o valor eficaz da corrente de magnetização
            st.write(f'O valor eficaz da corrente de magnetização é: {irms:.4f} A')

            # Exibir o passo a passo dos cálculos
            st.subheader("Passo a Passo dos Cálculos")

            # Mostrar a tensão máxima Vm
            st.write(r"Tensão máxima \( V_m \):")
            st.latex(r"V_m = V_p \cdot \sqrt{2} = " + f"{Vp} \cdot \sqrt{{2}} = {Vm:.2f} \, V")

            # Mostrar a velocidade angular
            st.write(r"Velocidade angular \( omega \):")
            st.latex(r"\omega = 2 \pi \cdot f = 2 \pi \cdot " + f"{freq} = {omega:.2f} \, \text{{rad/s}}")

            # Mostrar a fórmula do fluxo magnético
            st.write(r"Fluxo magnético \( phi(t) \) em função do tempo:")
            st.latex(r"\phi(t) = - \frac{V_m}{\omega N_p} \cos(\omega t)")
            st.write(f"Com \( V_m = {Vm:.2f} \, V \), \( \omega = {omega:.2f} \, \t {{rad/s}} \), e \( N_p = {Np}  \t {{espiras}} \):")
            st.latex(r"\phi(t) = - \frac{" + f"{Vm:.2f}" + r"}{" + f"{omega:.2f} \cdot {Np}" + r"} \cos(\omega t)")

            # Explicação sobre interpolação
            st.write("**Interpolação** da MMF a partir dos valores de fluxo calculados:")
            st.write(f"A interpolação é usada para calcular o valor da **força magnetomotriz (MMF)** correspondente \
            aos valores de **fluxo magnético** que variam continuamente no tempo. Sabemos que os valores exatos de MMF \
            estão disponíveis apenas em alguns pontos discretos na curva de magnetização fornecida no arquivo '{path}'. \
            Como os valores de fluxo calculados podem não coincidir exatamente com os dados da tabela, usamos a interpolação \
            para estimar a MMF nesses pontos intermediários.")

            # Exibir os valores de fluxo e MMF usados na interpolação
            st.write(f"**Valores de Fluxo Magnético calculados (primeiros 5 valores)**:")
            st.write(flux[:5])

            st.write(f"**Valores de MMF correspondentes interpolados (primeiros 5 valores)**:")
            st.write(mmf[:5])

            # Mostrar a corrente de magnetização
            st.write(r"Corrente de magnetização \( I_m \):")
            st.latex(r"I_m = \frac{MMF}{N_p}")

            # Explicar o cálculo da corrente eficaz
            st.write(f"Valor eficaz (RMS) da corrente de magnetização:")
            st.latex(r"I_{{rms}} = " + f"{irms:.4f} \, A")

            # Explicação detalhada das variáveis
            st.subheader("Explicação Detalhada")
            st.write("""
            - **Vp**: Tensão Primária - a tensão aplicada ao enrolamento primário do transformador.
            - **freq**: Frequência - a frequência da tensão aplicada em hertz (Hz).
            - **P**: Potência Aparente - a potência nominal do transformador em volt-ampere (VA).
            - **Np**: Número de Espiras no Primário - o número de voltas do enrolamento primário.
            - **Vm**: Tensão Máxima - calculada como \( V_p \cdot \sqrt{2} \), representa o pico da tensão.
            - **omega**: Velocidade Angular - calculada como \( 2 \pi \cdot \t {freq} \), em rad/s.
            - **flux**: Fluxo Magnético - a densidade de fluxo magnético no núcleo ao longo do tempo.
            - **mmf**: Força Magnetomotriz - interpolada a partir dos dados de fluxo.
            - **im**: Corrente de Magnetização - corrente necessária para magnetizar o núcleo.
            - **irms**: Corrente RMS - valor eficaz da corrente de magnetização, calculado como \(\sqrt{\frac{1}{T} \int_0^T i^2(t) \, dt}\).

            Este cálculo do valor eficaz (RMS) é importante para entender o comportamento real da corrente ao longo do tempo e suas implicações no desempenho do transformador.
            """)
        except:
            st.error(':blue[𝐎𝐜𝐨𝐫𝐫𝐞𝐮 𝐮𝐦 𝐞𝐫𝐫𝐨 𝐝𝐞 𝐞𝐱𝐞𝐜𝐮𝐜̧𝐚̃𝐨 𝐩𝐨𝐫 𝐪𝐮𝐞 𝐝𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚 𝐢𝐧𝐯𝐚́𝐥𝐢𝐝𝐨𝐬 𝐟𝐨𝐫𝐚𝐦 𝐟𝐨𝐫𝐧𝐞𝐜𝐢𝐝𝐨𝐬.]')