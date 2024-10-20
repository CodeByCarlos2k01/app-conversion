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

    # Corrente de carga (Ic)
    i_carga = p_carga / v_secundaria

    # Ajuste de corrente pela componente reativa
    if st.session_state['fp_tipo'] == 'Atrasado':
        # Fator de potência atrasado (fase negativa)
        i_carga_complexa = i_carga * (st.session_state['fp_carga'] - 1j * np.sqrt(1 - st.session_state['fp_carga']**2))
    else:
        # Fator de potência adiantado (fase positiva)
        i_carga_complexa = i_carga * (st.session_state['fp_carga'] + 1j * np.sqrt(1 - st.session_state['fp_carga']**2))

    fase_i_carga_rad = np.angle(i_carga_complexa)
    fase_i_carga_graus = np.degrees(fase_i_carga_rad)

    queda_tensao = i_carga_complexa * z_eq  # (ΔV)

    # tensão secundária em carga
    v_full_load = v_secundaria # - abs(queda_tensao)

    # tensão sem carga considerando a queda de tensão
    v_no_load = v_secundaria + queda_tensao

    # Cálculo da regulação
    regulacao = ((abs(v_no_load) - abs(v_full_load)) / abs(v_full_load)) * 100

    st.write('Vamos realizar os cálculos usando os valores inseridos:')
    st.latex(f'I_{{\\text{{carga}}}} = \\frac{{{p_carga:.2f}}}{{{v_secundaria:.2f}}} = {i_carga:.2f} \\text{{ A}}')
    st.latex(f'I_{{\\text{{cargaComplexa}}}} = {i_carga_complexa}')
    st.latex(f'\\Delta V = I_{{\\text{{carga}}}} \\times Z_{{\\text{{eq}}}} = ({i_carga_complexa:.2f}) \\times ({z_eq.real} + j{z_eq.imag}) = {queda_tensao:.2f} \\text{{ V}}')
    st.latex(f'\\text{{Ângulo de fase (φ) =}} {fase_i_carga_graus:.2f}º')
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

    ## ------------------ diagrama fasorial ------------------ ##
    fig_real, ax_real = plt.subplots()
    ax_real.quiver(0, 0, np.real(i_carga_complexa), np.imag(i_carga_complexa), angles='xy', scale_units='xy', scale=1, color='r', label='Corrente', linewidth=2)
    ax_real.quiver(0, 0, np.real(queda_tensao), np.imag(queda_tensao), angles='xy', scale_units='xy', scale=1, color='b', label='Queda de Tensão', linewidth=2)
    ax_real.quiver(0, 0, v_secundaria, 0, angles='xy', scale_units='xy', scale=1, color='g', label='Tensão Secundária', linewidth=2)

    plt.xlim(-1.5 * abs(v_secundaria), 1.5 * abs(v_secundaria))
    plt.ylim(-1.5 * abs(v_secundaria), 1.5 * abs(v_secundaria))
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.title('Diagrama Fasorial do Transformador')
    plt.xlabel('Parte Real (V)')
    plt.ylabel('Parte Imaginária (V)')
    plt.legend()
    st.pyplot(fig_real)

    ## ------------------ diagrama fasorial normalizado ------------------ ##
    fig_normalized, ax_normalized = plt.subplots()
    max_magnitude = max(abs(v_secundaria), abs(i_carga_complexa), abs(queda_tensao))
    ax_normalized.quiver(0, 0, np.real(i_carga_complexa) / max_magnitude, np.imag(i_carga_complexa) / max_magnitude, angles='xy', scale_units='xy', scale=1, color='r', label='Corrente', linewidth=2)
    ax_normalized.quiver(0, 0, np.real(queda_tensao) / max_magnitude, np.imag(queda_tensao) / max_magnitude, angles='xy', scale_units='xy', scale=1, color='b', label='Queda de Tensão', linewidth=2)
    ax_normalized.quiver(0, 0, v_secundaria / max_magnitude, 0, angles='xy', scale_units='xy', scale=1, color='g', label='Tensão Secundária', linewidth=2)

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.title('Diagrama Fasorial Normalizado do Transformador')
    plt.xlabel('Parte Real (V)')
    plt.ylabel('Parte Imaginária (V)')
    plt.legend()
    st.pyplot(fig_normalized)
