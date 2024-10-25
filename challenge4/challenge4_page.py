import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

if 'challenge4' not in st.session_state:
    st.session_state['challenge4']              = False
    st.session_state['challenge4_v_secundaria'] = 0.0
    st.session_state['challenge4_z_eq_real']    = 0.0
    st.session_state['challenge4_z_eq_imag']    = 0.0
    st.session_state['challenge4_p_carga']      = 0.0
    st.session_state['challenge4_fp_carga']     = 0.0
    st.session_state['challenge4_fp_tipo']      = "Atrasado"

st.title(':blue[𝐒𝐞çã𝐨 𝟒]')
st.title('Cálculo da regulação do transformador')
st.markdown('A regulação do transformador é uma medida que indica a variação percentual na tensão secundária de um transformador quando ele passa da condição de vazio (sem carga) para a condição de carga nominal.')
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚')
    st.markdown('• Parâmetros do transformador')
    st.markdown('• Dados da carga')
with col2:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐬𝐚í𝐝𝐚')
    st.markdown('• Regulação do Transformador')
    st.markdown('• Diagrama fasorial')

st.divider()
st.title('Dados de Entrada')
with st.form(key='input_form'):
    st.subheader('Insira os Parâmetros do Transformador')
    col1, col2, col3 = st.columns(3)
    v_secundaria = col1.number_input('Tensão Nominal Secundária (𝐕)', min_value=0.0, step=10.0)  # V
    v_secundaria = st.session_state['challenge4_v_secundaria'] if v_secundaria == 0 else v_secundaria
    
    z_eq_real = col2.number_input('Resistência Equivalente (𝐎𝐡𝐦𝐬)', min_value=0.0, step=0.01)  # real da impedância
    z_eq_real = st.session_state['challenge4_z_eq_real'] if z_eq_real == 0 else z_eq_real

    z_eq_imag = col3.number_input('Reatância Equivalente (𝐎𝐡𝐦𝐬)', min_value=0.0, step=0.01)  # imag da impedância
    z_eq_imag = st.session_state['challenge4_z_eq_imag'] if z_eq_imag == 0 else z_eq_imag

    st.subheader('Insira os Parâmetros da Carga')
    col1, col2, col3 = st.columns(3)
    p_carga = col1.number_input('Potência da Carga (𝐕𝐀)', min_value=0.0, step=100.0)  # VA
    p_carga = st.session_state['challenge4_p_carga'] if p_carga == 0 else p_carga

    fp_carga = col2.number_input('Fator de Potência da Carga [𝟎 𝐚 𝟏]', min_value=0.0, max_value=1.0, step=0.01)
    fp_tipo  = col3.radio("Tipo de Fator de Potência:", ("Atrasado", "Adiantado"))
    (fp_carga, fp_tipo) = (st.session_state['challenge4_fp_carga'], st.session_state['challenge4_fp_tipo']) if fp_carga == 0 else (fp_carga, fp_tipo)

    challenge4_button = st.form_submit_button(label='Gerar Resultado')

if (challenge4_button or st.session_state['challenge4']):
    st.session_state['challenge4']              = True
    st.session_state['challenge4_v_secundaria'] = v_secundaria
    st.session_state['challenge4_z_eq_real']    = z_eq_real
    st.session_state['challenge4_z_eq_imag']    = z_eq_imag
    st.session_state['challenge4_p_carga']      = p_carga
    st.session_state['challenge4_fp_carga']     = fp_carga
    st.session_state['challenge4_fp_tipo']      = fp_tipo

    st.title('Resultado')
    with st.expander('Passo a Passo da Resolução', expanded=True):
        try:
            st.subheader('Cálculos Detalhados')
            z_eq = complex(z_eq_real, z_eq_imag)  # impedância como número complexo

            # corrente de carga (Ic)
            i_carga = p_carga / v_secundaria

            if fp_tipo == 'Atrasado':
                # fator de potência atrasado (fase negativa)
                fp_sign = '-'
                i_carga_complexa = i_carga * (fp_carga - 1j * np.sqrt(1 - fp_carga**2))
            else:
                # fator de potência adiantado (fase positiva)
                fp_sign = '+'
                i_carga_complexa = i_carga * (fp_carga + 1j * np.sqrt(1 - fp_carga**2))

            queda_tensao_resistiva = i_carga_complexa * z_eq_real

            # queda de tensão reativa (imaginária)
            queda_tensao_reativa = i_carga_complexa * z_eq_imag

            # queda de tensão total
            queda_tensao = queda_tensao_resistiva + 1j * queda_tensao_reativa
            
            # queda_tensao = i_carga_complexa * z_eq  # (ΔV)

            fase_i_carga_graus = np.degrees(np.angle(i_carga_complexa))

            # tensão secundária em carga
            v_full_load = v_secundaria  # - queda_tensao (análise habitual de transformador de boa qualidade)

            # tensão sem carga considerando a queda de tensão
            v_no_load = v_secundaria + queda_tensao

            # cálculo da regulação
            regulacao = ((abs(v_no_load) - abs(v_full_load)) / abs(v_full_load)) * 100

            st.write('Vamos realizar os cálculos usando os valores inseridos:')
            st.latex(f'I_{{\\text{{carga}}}} = \\frac{{{p_carga:.2f}}}{{{v_secundaria:.2f}}} = {i_carga:.2f} \\text{{ A}}')
            st.write(f'Calculando a carga complexa:')
            st.latex(f'I_{{\\text{{cargaComplexa}}}} = I_{{\\text{{carga}}}} \\times (fp_{{\\text{{carga}}}} {{{fp_sign}}} j \\sqrt{{1 - (fp_{{\\text{{carga}}}})^2}})')
            st.latex(f'I_{{\\text{{cargaComplexa}}}} = {i_carga_complexa}')
            st.write("   - *Esse resultado é um número complexo que contém tanto a parte real (ativa) quanto a parte imaginária (reativa) da corrente.*")

            st.write('Agora, devemos encontrar o ângulo da corrente complexa, o fator de potência dado foi:')
            st.latex(f'fp_{{\\text{{carga}}}} = {fp_carga}')
            if fp_tipo == 'Atrasado':
                st.write('Como o fator de potência é atrasado, o ângulo de fase é:')
                st.latex(f'\\phi = -\\cos^{{-1}}(fp_{{\\text{{carga}}}}) = -\\cos^{{-1}}({fp_carga}) = {fase_i_carga_graus:.2f}^\\circ')
            else:
                st.write('Como o fator de potência é adiantado, o ângulo de fase é:')
                st.latex(f'\\phi = \\cos^{{-1}}(fp_{{\\text{{carga}}}}) = \\cos^{{-1}}({fp_carga}) = {fase_i_carga_graus:.2f}^\\circ')

            st.write(f'Temos:')
            st.latex(f'\\phi = {fase_i_carga_graus:.2f}^\\circ')

            st.write(f'Agora, continuamos calculando o valor de queda de tensão:')
            st.latex(f'\\Delta V = I_{{\\text{{carga}}}} \\times Z_{{\\text{{eq}}}} = ({i_carga_complexa:.2f}) \\times ({z_eq.real} + j{z_eq.imag}) = {queda_tensao:.2f} \\text{{ V}}')
            st.write('Convertendo esse valor ΔV para absoluto...')
            st.latex(f'\\Delta V = {abs(queda_tensao)}')
            st.latex(f'\\Delta V =~ {abs(queda_tensao):.2f}')
            st.write('Cenário habitual de análise:')

            # Exibição das tensões
            st.latex(f'V_{{\\text{{comCarga}}}} = V_{{\\text{{secundário}}}}')
            st.latex(f'V_{{\\text{{semCarga}}}} = V_{{\\text{{secundário}}}} + \\Delta V = {v_secundaria:.2f} + {queda_tensao:.2f} = {v_no_load:.2f} \\text{{ V}}')
            st.latex(f'\\text{{Regulação}} = \\frac{{|V_{{semCarga}}| - |V_{{comCarga}}|}}{{|V_{{comCarga}}|}} \\times 100\\% = \\frac{{{abs(v_no_load):.2f} - {abs(v_full_load):.2f}}}{{{abs(v_full_load):.2f}}} \\times 100\\% = {regulacao:.2f}\\%')

            st.subheader('Resultado da Regulação do Transformador')
            st.write(f'**Regulação do Transformador:** {regulacao:.2f}%')


            if -1 < regulacao < 1:
                st.success("*Avaliação:* Excelente. O transformador mantém a tensão praticamente constante sob carga.")
            elif 1 <= regulacao < 3 or -3 <= regulacao < -1:
                st.success("*Avaliação:* Muito Bom. A variação de tensão é quase imperceptível para a maioria das aplicações.")
            elif 3 <= regulacao < 5 or -5 <= regulacao < -3:
                st.warning("*Avaliação:* Bom. A variação de tensão é aceitável para a maioria das aplicações comerciais e industriais.")
            elif 5 <= regulacao < 10 or -10 <= regulacao < -5:
                st.warning("*Avaliação:* Razoável. A variação de tensão é mais perceptível, mas ainda tolerável em situações não críticas.")
            elif 10 <= regulacao < 15 or -15 <= regulacao < -10:
                st.error("*Avaliação:* Ruim. A variação de tensão é alta e pode afetar equipamentos sensíveis.")
            else:
                st.error("*Avaliação:* Inaceitável. A regulação é muito alta, indicando que o transformador não é adequado para a maioria das aplicações.")

            # ------------------ diagrama fasorial ------------------ #
            
            fig_normalizado, ax_normalizado = plt.subplots()
            
            # vetor da tensão nominal secundária (V_secundaria)
            ax_normalizado.quiver(0, 0, v_secundaria * np.cos(0), v_secundaria * np.sin(0), angles='xy', scale_units='xy', scale=1, color='blue', label='Tensão Secundária (Plena Carga)', linewidth=2)

            # vetor da tensão sem carga (V_no_load)
            ax_normalizado.quiver(0, 0, np.real(v_no_load), np.imag(v_no_load), angles='xy', scale_units='xy', scale=1, color='purple', label='Tensão Secundária (Sem Carga)', linewidth=2)

            # vetor da corrente (I_carga_complexa), deslocado pelo ângulo
            angulo_ic_rad = np.radians(fase_i_carga_graus)

            # escala para possibilitar vermos o vetor de corrente
            if v_secundaria > 1000:
                fator_escala = 10
            else:
                fator_escala = 1.5
            ax_normalizado.quiver(0, 0, fator_escala * i_carga * np.cos(angulo_ic_rad), fator_escala * i_carga * np.sin(angulo_ic_rad), angles='xy', scale_units='xy', scale=1, color='r', label='Corrente', linewidth=2)

            x_resistiva = fator_escala * queda_tensao_resistiva * np.cos(angulo_ic_rad)
            y_resistiva = fator_escala * queda_tensao_resistiva * np.sin(angulo_ic_rad)

            # Desenha o vetor da queda de tensão resistiva (do centro)
            ax_normalizado.quiver(0, 0, x_resistiva, y_resistiva, 
                      angles='xy', scale_units='xy', scale=1, color='blue', label='Queda de Tensão Resistiva (ΔV_R)', linewidth=2)


            angulo_reativo_rad = angulo_ic_rad + np.pi / 2  # Defasado em 90º

            # Desenha o vetor da queda de tensão reativa a partir do final da queda resistiva
            ax_normalizado.quiver(x_resistiva, y_resistiva, 
                      fator_escala * queda_tensao_reativa * np.cos(angulo_reativo_rad), 
                      fator_escala * queda_tensao_reativa * np.sin(angulo_reativo_rad), 
                      angles='xy', scale_units='xy', scale=1, color='green', label='Queda de Tensão Reativa (ΔV_X)', linewidth=2)



            # cálculo dos ângulos dos vetores de tensão
            angulo_v_secundaria_rad = np.angle(v_secundaria)
            angulo_v_no_load_rad = np.angle(v_no_load)

            # diferença de ângulo entre os vetores de tensão
            angulo_diferenca_rad = angulo_v_no_load_rad - angulo_v_secundaria_rad
            angulo_diferenca_graus = np.degrees(angulo_diferenca_rad)

            # configurações do gráfico
            ax_normalizado.set_xlim(-2 * abs(v_secundaria), 2 * abs(v_secundaria)) 
            ax_normalizado.set_ylim(-2 * abs(v_secundaria), 2 * abs(v_secundaria)) 
            ax_normalizado.axhline(0, color='black', lw=0.5, ls='--')
            ax_normalizado.axvline(0, color='black', lw=0.5, ls='--')
            ax_normalizado.grid()
            ax_normalizado.set_aspect('equal')
            ax_normalizado.set_title('Diagrama Fasorial')
            ax_normalizado.legend()


            posicao_x = -1.0 * abs(v_secundaria) 
            posicao_y = -1.0 * abs(v_secundaria)   
            angulo_tensoes_texto = f'Ângulo entre tensões: {angulo_diferenca_graus:.2f}°'
            angulo_corrente_texto = f'Ângulo da corrente: {fase_i_carga_graus:.2f}°'

            ax_normalizado.text(posicao_x, posicao_y, angulo_tensoes_texto, fontsize=8, ha='center', color='black')
            ax_normalizado.text(posicao_x, posicao_y*1.4, angulo_corrente_texto, fontsize=8, ha='center', color='black')

            st.pyplot(fig_normalizado)

            st.warning(f'**:blue[O valor da corrente no gráfico foi multiplicado por {fator_escala} para melhor visualização do seu vetor.]**')
        except:
            st.error('Ocorreu um erro ao gerar o gráfico, possivelmente devido a parâmetros inconsistentes.')
