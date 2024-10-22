import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Inicializar o session_state
if 'Vp' not in st.session_state:
    st.session_state.Vp = 120.0
if 'freq' not in st.session_state:
    st.session_state.freq = 50.0
if 'Np' not in st.session_state:
    st.session_state.Np = 850

# Título da aplicação
st.title("Simulação da Corrente de Magnetização de um Transformador")

# Inputs interativos no Streamlit com valores padrão usando session_state
st.session_state.Vp = st.number_input('Tensão Primária (Vp) em Volts', value=st.session_state.Vp)
st.session_state.freq = st.number_input('Frequência (Hz)', value=st.session_state.freq)
st.session_state.Np = st.number_input('Número de Espiras no Primário (Np)', value=st.session_state.Np)

# Nome do caminho do arquivo
path = 'MagCurve-3.xlsx'

# Carregar os dados de fluxo (proporcional a B) e MMF (proporcional a H) do arquivo Excel
data = pd.read_excel(path)
flux_data = data['Fluxo']
mmf_data = data['MMF']

# Calcular a tensão máxima (pico) aplicada ao transformador
Vm = st.session_state.Vp * np.sqrt(2)

# Velocidade angular (omega) é dada por 2 * pi * frequência
omega = 2 * np.pi * st.session_state.freq

# Definir o intervalo de tempo para simulação
t_final = 340e-3
t_step = 1 / 3000
time = np.arange(0, t_final, t_step)

# Calcular fluxo magnético (proporcional a B) em função do tempo
flux = -Vm / (omega * st.session_state.Np) * np.cos(omega * time)

# Interpolação da curva BxH
mmf = np.interp(flux, flux_data, mmf_data)

# Calcular a corrente de magnetização (I_m)
im = mmf / st.session_state.Np

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
st.latex(r"V_m = V_p \cdot \sqrt{2} = " + f"{st.session_state.Vp} \cdot \sqrt{{2}} = {Vm:.2f} \, V")

# Mostrar a velocidade angular
st.write(r"Velocidade angular \( omega \):")
st.latex(r"\omega = 2 \pi \cdot f = 2 \pi \cdot " + f"{st.session_state.freq} = {omega:.2f} \, \text{{rad/s}}")

# Mostrar a fórmula do fluxo magnético
st.write(r"Fluxo magnético \( phi(t) \) em função do tempo:")
st.latex(r"\phi(t) = - \frac{V_m}{\omega N_p} \cos(\omega t)")
st.write(f"Com \( V_m = {Vm:.2f} \, V \), \( \omega = {omega:.2f} \, \t {{rad/s}} \), e \( N_p = {st.session_state.Np}  \t {{espiras}} \):")
st.latex(r"\phi(t) = - \frac{" + f"{Vm:.2f}" + r"}{" + f"{omega:.2f} \cdot {st.session_state.Np}" + r"} \cos(\omega t)")

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