import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

if 'transformer_challenge' not in st.session_state:
    st.session_state['transformer_challenge'] = False

st.title(':blue[𝐒𝐞𝐜̧𝐚̃𝐨 𝟒]')
st.title('Cálculo da regulação do transformador')
st.markdown('A regulação do transformador é uma medida que indica a variação percentual na tensão secundária de um transformador quando ele passa da condição de vazio (sem carga) para a condição de carga nominal.')

with st.form(key='input_form'):
    st.subheader('Insira os Parâmetros do Transformador')
    v_secundaria = st.number_input('Tensão Nominal Secundária (V)', min_value=0.1, value=2400.0, step=10.0)  # V
    z_eq_real = st.number_input('Resistência Equivalente (Ohms)', min_value=0.0, value=0.28, step=0.01)  # real da impedância
    z_eq_imag = st.number_input('Reatância Equivalente (Ohms)', min_value=0.0, value=1.0, step=0.01)  # imag da impedância
    
    st.subheader('Insira os Parâmetros da Carga')
    p_carga = st.number_input('Potência da Carga (VA)', min_value=1.0, value=180000.0, step=100.0)  # VA
    fp_carga = st.number_input('Fator de Potência da Carga (0 a 1)', min_value=0.0, max_value=1.0, value=0.92, step=0.01)
    
    fp_tipo = st.radio("Tipo de Fator de Potência:", ("Atrasado", "Adiantado"))  # Radio button para tipo de fator de potência
    
    submit_button = st.form_submit_button(label='Gerar Resultado')

if submit_button or st.session_state['transformer_challenge']:
    st.session_state['transformer_challenge'] = True
    st.session_state['v_secundaria'] = v_secundaria
    st.session_state['z_eq_real'], st.session_state['z_eq_imag'], st.session_state['p_carga'], st.session_state['fp_carga'], st.session_state['fp_tipo'] = z_eq_real, z_eq_imag, p_carga, fp_carga, fp_tipo

    st.divider()
    st.subheader('Cálculos Detalhados')

    p_carga = st.session_state['p_carga']
    v_secundaria = st.session_state['v_secundaria']
    z_eq = complex(st.session_state['z_eq_real'], st.session_state['z_eq_imag'])  # impedância como número complexo

    # corrente de carga (Ic)
    i_carga = p_carga / v_secundaria

    # Ajuste de corrente pela componente reativa
    if st.session_state['fp_tipo'] == 'Atrasado':
        # fator de potência atrasado (fase negativa)
        i_carga_complexa = i_carga * (st.session_state['fp_carga'] - 1j * np.sqrt(1 - st.session_state['fp_carga']**2))
    else:
        # fator de potência adiantado (fase positiva)
        i_carga_complexa = i_carga * (st.session_state['fp_carga'] + 1j * np.sqrt(1 - st.session_state['fp_carga']**2))

    fase_i_carga_graus = np.degrees(np.angle(i_carga_complexa))

    queda_tensao = i_carga_complexa * z_eq  # (ΔV)

    # tensão secundária em carga
    v_full_load = v_secundaria  # - abs(queda_tensao)

    # tensão sem carga considerando a queda de tensão
    v_no_load = v_secundaria + queda_tensao

    # cálculo da regulação
    regulacao = ((abs(v_no_load) - abs(v_full_load)) / abs(v_full_load)) * 100

    st.write('Vamos realizar os cálculos usando os valores inseridos:')
    st.latex(f'I_{{\\text{{carga}}}} = \\frac{{{p_carga:.2f}}}{{{v_secundaria:.2f}}} = {i_carga:.2f} \\text{{ A}}')
    st.latex(f'I_{{\\text{{cargaComplexa}}}} = {i_carga_complexa}')
    st.latex(f'\\Delta V = I_{{\\text{{carga}}}} \\times Z_{{\\text{{eq}}}} = ({i_carga_complexa:.2f}) \\times ({z_eq.real} + j{z_eq.imag}) = {queda_tensao:.2f} \\text{{ V}}')
    st.write(f'Convertendo esse valor ΔV para absoluto...')
    st.latex(f'\\Delta V = {abs(queda_tensao)}')
    st.latex(f'\\Delta V =~ {abs(queda_tensao):.2f}')
    st.latex(f'V_{{\\text{{comCarga}}}} = V_{{\\text{{secundário}}}} - |\\Delta V| = {v_secundaria:.2f} - {abs(queda_tensao):.2f} = {v_full_load:.2f} \\text{{ V}}')
    st.latex(f'V_{{\\text{{semCarga}}}} = V_{{\\text{{secundário}}}} + \\Delta V = {v_secundaria:.2f} + {queda_tensao:.2f} = {v_no_load:.2f} \\text{{ V}}')
    st.latex(f'\\text{{Regulação}} = \\frac{{|V_{{sem carga}}| - |V_{{comCarga}}|}}{{|V_{{comCarga}}|}} \\times 100\\% = \\frac{{{abs(v_no_load):.2f} - {abs(v_full_load):.2f}}}{{{abs(v_full_load):.2f}}} \\times 100\\% = {regulacao:.2f}\\%')

    st.subheader('Resultado da Regulação do Transformador')
    st.write(f'**Regulação do Transformador:** {regulacao:.2f}%')
    if regulacao < 0:
        st.warning("*Atenção:* A regulação do transformador é negativa! Isso indica que a tensão sob carga é maior do que a tensão nominal sem carga. Essa condição pode causar problemas em equipamentos conectados e não é desejável para a operação segura do sistema.")
    elif regulacao < 1:
        st.success("*Avaliação:* Excelente. O transformador mantém a tensão praticamente constante sob carga.")
    elif 1 <= regulacao < 3:
        st.success("*Avaliação:* Muito Bom. A variação de tensão é quase imperceptível para a maioria das aplicações.")
    elif 3 <= regulacao < 5:
        st.warning("*Avaliação:* Bom. A variação de tensão é aceitável para a maioria das aplicações comerciais e industriais.")
    elif 5 <= regulacao < 10:
        st.warning("*Avaliação:* Razoável. A variação de tensão é mais perceptível, mas ainda tolerável em situações não críticas.")
    elif 10 <= regulacao < 15:
        st.error("*Avaliação:* Ruim. A variação de tensão é alta e pode afetar equipamentos sensíveis.")
    else:
        st.error("*Avaliação:* Inaceitável. A regulação é muito alta, indicando que o transformador não é adequado para a maioria das aplicações.")

    # ------------------ diagrama fasorial ------------------ #
    
    fig_normalizado, ax_normalizado = plt.subplots()
    
    # vetor da tensão nominal secundária (V_secundaria)
    ax_normalizado.quiver(0, 0, v_secundaria * np.cos(0), v_secundaria * np.sin(0), angles='xy', scale_units='xy', scale=1, color='g', label='Tensão Nominal Secundária', linewidth=2)

    # vetor da tensão sem carga (V_no_load)
    ax_normalizado.quiver(0, 0, np.real(v_no_load), np.imag(v_no_load), angles='xy', scale_units='xy', scale=1, color='purple', label='Tensão Sem Carga', linewidth=2)

    # vetor da corrente (I_carga_complexa), deslocado pelo ângulo
    angulo_ic_rad = np.radians(fase_i_carga_graus)

    # escala para possibilitar vermos o vetor de corrente
    fator_escala = 15
    ax_normalizado.quiver(0, 0, fator_escala * i_carga * np.cos(angulo_ic_rad), fator_escala * i_carga * np.sin(angulo_ic_rad), angles='xy', scale_units='xy', scale=1, color='r', label='Corrente', linewidth=2)

    # cálculo dos ângulos dos vetores de tensão
    angulo_v_secundaria_rad = np.angle(v_secundaria)
    angulo_v_no_load_rad = np.angle(v_no_load)

    # diferença de ângulo entre os vetores de tensão
    angulo_diferenca_rad = angulo_v_no_load_rad - angulo_v_secundaria_rad
    angulo_diferenca_graus = np.degrees(angulo_diferenca_rad)

    st.write(f'**Ângulo entre os vetores de tensão:** {angulo_diferenca_graus:.2f}°')

    # configurações do gráfico
    ax_normalizado.set_xlim(-2 * abs(v_secundaria), 2 * abs(v_secundaria))  # Aumenta o limite do eixo X
    ax_normalizado.set_ylim(-2 * abs(v_secundaria), 2 * abs(v_secundaria))  # Aumenta o limite do eixo Y
    ax_normalizado.axhline(0, color='black', lw=0.5, ls='--')
    ax_normalizado.axvline(0, color='black', lw=0.5, ls='--')
    ax_normalizado.grid()
    ax_normalizado.set_aspect('equal')
    ax_normalizado.set_title('Diagrama Fasorial Normalizado')
    ax_normalizado.legend()

    # exibir angulo entre tensões
    posicao_x = (np.real(v_no_load) + np.real(v_secundaria)) / 2  
    posicao_y = -0.5 * abs(v_secundaria)
    angulo_tensoes_texto = f'Ângulo entre tensões: {angulo_diferenca_graus:.2f}°'
    angulo_corrente_texto = f'Ângulo da corrente: {fase_i_carga_graus:.2f}°'

    ax_normalizado.text(posicao_x, posicao_y, angulo_tensoes_texto, fontsize=8, ha='center', color='black')
    ax_normalizado.text(posicao_x, posicao_y*1.4, angulo_corrente_texto, fontsize=8, ha='center', color='black')

    st.pyplot(fig_normalizado)
