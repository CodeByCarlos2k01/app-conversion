import streamlit as st
import pandas as pd
import math

if 'challenge1' not in st.session_state:
    st.session_state['challenge1'] = False
    st.session_state['challenge1_circuito_p'] = 1
    st.session_state['challenge1_Vp2'] = 0.0
    st.session_state['challenge1_circuito_s'] = 1
    st.session_state['challenge1_Vs2'] = 0.0
    st.session_state['challenge1_Ws'] = 0.0

laminas = pd.DataFrame(data={'a'    : [1.5, 2, 2.5, 3, 3.5, 4, 5], 
                             'secao': [168, 300, 468, 675, 900, 1200, 1880], 
                             'peso' : [0.095, 0.170, 0.273, 0.380, 0.516, 0.674, 1.053]})

secao_condutor = pd.DataFrame(data={'potencia' : [500, 1000, 3000], 
                                    'densidade': [3, 2.5, 2]})

awg = pd.DataFrame(data={'numero' : ['0000', '000', '00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44'], 
                         'secao'  : [107.2, 85.3, 67.43, 53.48, 42.41, 33.63, 26.67, 21.15, 16.77, 13.30, 10.55, 8.36, 6.63, 5.26, 4.17, 3.31, 2.63, 2.08, 1.65, 1.31, 1.04, 0.82, 0.65, 0.52, 0.41, 0.33, 0.26, 0.20, 0.16, 0.13, 0.10, 0.08, 0.064, 0.051, 0.04, 0.032, 0.0254, 0.0201, 0.0159, 0.0127, 0.01, 0.0079, 0.0063, 0.005, 0.004, 0.0032, 0.0025, 0.002]})


st.title(':blue[𝐒𝐞𝐜̧𝐚̃𝐨 𝟏]')

st.title('Dimensionamento de um transformador monofásico')
st.markdown('O dimensionamento de um transformador monofásico serve para garantir que o equipamento seja capaz de atender às necessidades específicas de um sistema elétrico, operando com segurança e eficiência. Esse processo envolve calcular as capacidades elétricas adequadas.')
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫 𝐓𝐢𝐩𝐨 𝟏')
    st.image('challenge1/models/circuito1.png', caption='1 𝑐𝑖𝑟𝑐𝑢𝑖𝑡𝑜 𝑝𝑟𝑖𝑚𝑎́𝑟𝑖𝑜 𝑒 1 𝑠𝑒𝑐𝑢𝑛𝑑𝑎́𝑟𝑖𝑜')
with col2:
    st.subheader('𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫 𝐓𝐢𝐩𝐨 𝟐')
    st.image('challenge1/models/circuito2.png', caption='2 𝑐𝑖𝑟𝑐𝑢𝑖𝑡𝑜𝑠 𝑝𝑟𝑖𝑚𝑎́𝑟𝑖𝑜 𝑒 1 𝑠𝑒𝑐𝑢𝑛𝑑𝑎́𝑟𝑖𝑜\n (𝑉𝑖𝑐𝑒-𝑉𝑒𝑟𝑠𝑎)')
with col3:
    st.subheader('𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫 𝐓𝐢𝐩𝐨 𝟑')
    st.image('challenge1/models/circuito3.png', caption='2 𝑐𝑖𝑟𝑐𝑢𝑖𝑡𝑜𝑠 𝑝𝑟𝑖𝑚𝑎́𝑟𝑖𝑜 𝑒 2 𝑠𝑒𝑐𝑢𝑛𝑑𝑎́𝑟𝑖𝑜')

st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚')
    st.markdown('• Tensão Primária Vp em Volts')
    st.markdown('• Tensão Secundária Vs em Volts')
    st.markdown('• Potência da carga em VA ou W')
with col2:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐬𝐚𝐢́𝐝𝐚')
    st.markdown('• Número de Espiras do Enrolamento Primário e Secundário')
    st.markdown('• Bitola do cabo primário e do cabo secundário')
    st.markdown('• Tipo de lâmina e quantidade')
    st.markdown('• Dimensões do transformador: Núcleo e dimensões finais, peso.')

st.divider()
st.info('𝐎 𝐚𝐥𝐠𝐨𝐫𝐢𝐭𝐦𝐨 𝐢𝐫𝐚́ 𝐜𝐨𝐧𝐬𝐢𝐝𝐞𝐫𝐚𝐫 𝐚 𝐅𝐫𝐞𝐪𝐮𝐞̂𝐧𝐜𝐢𝐚 𝐩𝐚𝐝𝐫𝐚̃𝐨 𝐝𝐞 𝟓𝟎 𝐇𝐳 𝐞 𝐚 𝐏𝐨𝐭𝐞̂𝐧𝐜𝐢𝐚 𝐥𝐢𝐦𝐢𝐭𝐞 𝐝𝐞 𝟖𝟎𝟎 𝐕𝐀.')

st.title('Dados de entrada')

with st.form('challenge1_form'):
    st.subheader('Tensão Primária')
    col1, col2 = st.columns(2)
    Vp2 = col1.number_input("Informe a Tensão Primária em Volts", min_value = 0.0)
    circuito_p = col2.radio("Informe o Número de Circuitos no Primário", (1, 2))
    (circuito_p, Vp2) = (st.session_state['challenge1_circuito_p'], st.session_state['challenge1_Vp2']) if Vp2 == 0 else (circuito_p, Vp2)

    st.subheader('Tensão Secundária')
    col1, col2 = st.columns(2)
    Vs2 = col1.number_input("Informe a Tensão Secundária em Volts", min_value = 0.0)
    circuito_s = col2.radio("Informe o Número de Circuitos no Secundário", (1, 2))
    (circuito_s, Vs2) = (st.session_state['challenge1_circuito_s'], st.session_state['challenge1_Vs2']) if Vs2 == 0 else (circuito_s, Vs2)

    st.subheader('Potência da Carga')
    Ws = st.number_input("Informe a Potência da carga em Volt-Ampere", min_value = 0.0, max_value = 800.0)
    Ws = st.session_state['challenge1_Ws'] if Ws == 0 else Ws

    if (st.form_submit_button('Gerar Resultado') or st.session_state['challenge1']):
        try:
            st.session_state['challenge1'] = True
            st.session_state['challenge1_circuito_p'], st.session_state['challenge1_Vp2'] = circuito_p, Vp2
            st.session_state['challenge1_circuito_s'], st.session_state['challenge1_Vs2'] = circuito_s, Vs2
            st.session_state['challenge1_Ws'] = Ws

            Vp1 = 0 if circuito_p == 1 else Vp2 / 2
            Vs1 = 0 if circuito_s == 1 else Vs2 / 2

            cond1 = Vp1 > 0
            cond2 = Vs1 > 0
            tipo_transformador = 1 if (cond1, cond2) == (False, False) else 2 if (cond1 or cond2) and not (cond1 and cond2) else 3

            st.write('\n')
            st.subheader('Cálculo do Transformador Monofásico (:green[Solução])')
            st.divider()
            
            col1, col2 = st.columns(2)
            col1.subheader(f'Transformador Tipo {tipo_transformador}')
            if tipo_transformador == 1:
                col1.markdown('1 circuito no primário e 1 circuito no secundário')
            elif tipo_transformador == 2:
                col1.markdown('2 circuitos no primário e 1 circuito no secundário (Vice-Versa)')
            else:
                col1.markdown('2 circuitos no primário e 2 circuitos no secundário')

            col2.image(f'challenge1/models/circuito{tipo_transformador}.png')
            st.write('**N.B. O esquema do transformador toma a forma indicada na figura.**')
            st.divider()

            st.write(f'𝐃𝐚𝐝𝐨𝐬 𝐝𝐨 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫 𝐦𝐨𝐧𝐨𝐟𝐚́𝐬𝐢𝐜𝐨:')
            st.latex(fr'f = 50 \ Hz')
            st.latex(fr'W_{2} = {{{Ws}}} \ Va')
            st.latex(fr'V_{1} = {{{Vp1}}}/{{{Vp2}}} \ V')
            st.latex(fr'V_{2} = {{{Vs1}}}/{{{Vs2}}} \ V')
            st.divider()

            Wp = round(1.1 * Ws, 2)
            st.write('-𝐏𝐨𝐭𝐞̂𝐧𝐜𝐢𝐚 𝐩𝐫𝐢𝐦𝐚́𝐫𝐢𝐚:')
            st.latex(fr'W_{1} = 1,1 \cdot W_{2} = 1,1 \cdot ({{{Ws}}}) = {{{Wp}}} \ Va')
            st.divider()

            st.write('-𝐂𝐨𝐫𝐫𝐞𝐧𝐭𝐞 𝐩𝐫𝐢𝐦𝐚́𝐫𝐢𝐚:')
            if cond1:
                Ip1 = round(Wp / Vp1, 2)
                st.latex(fr'I_{1} = \frac{{W_{1}}}{{V_{1}}} = \frac{{{Wp}}}{{{Vp1}}} = {{{Ip1}}} \ A')
            Ip2 = round(Wp / Vp2, 2)
            st.latex(fr'I_{1} = \frac{{W_{1}}}{{V_{1}}} = \frac{{{Wp}}}{{{Vp2}}} = {{{Ip2}}} \ A')
            st.divider()

            st.write('-𝐂𝐨𝐫𝐫𝐞𝐧𝐭𝐞 𝐬𝐞𝐜𝐮𝐧𝐝𝐚́𝐫𝐢𝐚:')
            if cond2:
                Is1 = round(Ws / Vs1, 2)
                st.latex(fr'I_{2} = \frac{{W_{2}}}{{V_{2}}} = \frac{{{Ws}}}{{{Vs1}}} = {{{Is1}}} \ A')
            Is2 = round(Ws / Vs2, 2)
            st.latex(fr'I_{2} = \frac{{W_{2}}}{{V_{2}}} = \frac{{{Ws}}}{{{Vs2}}} = {{{Is2}}} \ A')
            st.divider()

            d = secao_condutor[secao_condutor['potencia'] > Ws]['densidade'].max()
            st.write(f'Escolhendo-se a densidade de corrente **𝐝 = {d} 𝐀/𝐦𝐦²**, obtém-se:')
            if cond1:
                Sp1 = round(Ip1 / d, 2)
                st.latex(fr'S_{1} = \frac{{I_{1}}}{{d}} = \frac{{{Ip1}}}{{{d}}} = {{{Sp1}}} \ mm²')
                idx = awg[awg['secao'] >= Sp1].shape[0] - 1 
                secao11, n_awg11 = awg['secao'][idx], awg['numero'][idx]
                st.write(f'Usa-se **𝐟𝐢𝐨 𝐧.º {n_awg11} (𝐀𝐖𝐆)** cuja seção é **𝐒₁ = {secao11} 𝐦𝐦²**')
            Sp2 = round(Ip2 / d, 2)
            st.latex(fr'S_{1} = \frac{{I_{1}}}{{d}} = \frac{{{Ip2}}}{{{d}}} = {{{Sp2}}} \ mm²')
            idx = awg[awg['secao'] >= Sp2].shape[0] - 1 
            secao12, n_awg12 = awg['secao'][idx], awg['numero'][idx]
            st.write(f'Usa-se **𝐟𝐢𝐨 𝐧.º {n_awg12} (𝐀𝐖𝐆)** cuja seção é **𝐒₁ = {secao12} 𝐦𝐦²**')

            if cond2:
                Ss1 = round(Is1 / d, 2)
                st.latex(fr'S_{2} = \frac{{I_{2}}}{{d}} = \frac{{{Is1}}}{{{d}}} = {{{Ss1}}} \ mm²')
                idx = awg[awg['secao'] >= Ss1].shape[0] - 1 
                secao21, n_awg21 = awg['secao'][idx], awg['numero'][idx]
                st.write(f'Usa-se **𝐟𝐢𝐨 𝐧.º {n_awg21} (𝐀𝐖𝐆)** cuja seção é **𝐒₂ = {secao21} 𝐦𝐦²**')
            Ss2 = round(Is2 / d, 2)
            st.latex(fr'S_{2} = \frac{{I_{2}}}{{d}} = \frac{{{Is2}}}{{{d}}} = {{{Ss2}}} \ mm²')
            idx = awg[awg['secao'] >= Ss2].shape[0] - 1 
            secao22, n_awg22 = awg['secao'][idx], awg['numero'][idx]
            st.write(f'Usa-se **𝐟𝐢𝐨 𝐧.º {n_awg22} (𝐀𝐖𝐆)** cuja seção é **𝐒₂ = {secao22} 𝐦𝐦²**')
            st.divider()

            st.write('**N.B. Em ambos os enrolamentos a densidade de corrente resulta inferior ou igual à prevista, isto é:**')
            if cond1:
                dp1 = round(Ip1 / secao11, 2)
                st.latex(fr'd₁ = \frac{{I₁}}{{S₁}} = \frac{{{Ip1}}}{{{secao11}}} = {{{dp1}}} \ A/mm²')
            dp2 = round(Ip2 / secao12, 2)
            st.latex(fr'd₁ = \frac{{I₁}}{{S₁}} = \frac{{{Ip2}}}{{{secao12}}} = {{{dp2}}} \ A/mm²')

            if cond2:
                ds1 = round(Is1 / secao21, 2)
                st.latex(fr'd₂ = \frac{{I₂}}{{S₂}} = \frac{{{Is1}}}{{{secao21}}} = {{{ds1}}} \ A/mm²')
            ds2 = round(Is2 / secao22, 2)
            st.latex(fr'd₂ = \frac{{I₂}}{{S₂}} = \frac{{{Is2}}}{{{secao22}}} = {{{ds2}}} \ A/mm²')

            dp = round((dp1 + dp2) / 2, 2) if cond1 else dp2
            ds = round((ds1 + ds2) / 2, 2) if cond2 else ds2
            st.write('Para o cálculo da perda no cobre considera-se a densidade média de:')
            d_mean = round((dp + ds) / 2, 2)
            st.latex(fr'd = {{{d_mean}}} \ A/mm²')
            st.divider()

            col1, col2 = st.columns(2)
            col1.markdown('𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐫 𝐝𝐢𝐦𝐞𝐧𝐬𝐨̃𝐞𝐬 [:green[𝐚]] 𝐞 [:green[𝐛]] 𝐝𝐚 𝐩𝐞𝐜̧𝐚')
            col2.image('challenge1/models/secao.png')
            st.write('-𝐒𝐞𝐜̧𝐚̃𝐨 𝐦𝐚𝐠𝐧𝐞́𝐭𝐢𝐜𝐚 𝐝𝐨 𝐧𝐮́𝐜𝐥𝐞𝐨: como o transformador possui um circuito primário e um circuito secundário, emprega-se a fórmula:')

            if tipo_transformador == 1:
                Sm = round(7.5 * math.sqrt(Ws / 50), 2)
                st.latex(fr'S_{{m}} = 7,5 \sqrt{{ \frac{{W_{2}}}{{f}} }} = 7,5 \sqrt{{ \frac{{{Ws}}}{{50}} }} = 7,5 \sqrt {{{Ws / 50}}} = {{{Sm}}} \ cm²')
            elif tipo_transformador == 2:
                Sm = round(7.5 * math.sqrt(1.25 * Ws / 50), 2)
                st.latex(fr'S_{{m}} = 7,5 \sqrt{{ \frac{{1.25 \cdot W_{2}}}{{f}} }} = 7,5 \sqrt{{ \frac{{{1.25} \cdot {Ws}}}{{50}} }} = 7,5 \sqrt {{{1.25 * Ws / 50}}} = {{{Sm}}} \ cm²')
            elif tipo_transformador == 3:
                Sm = round(7.5 * math.sqrt(1.5 * Ws / 50), 2)
                st.latex(fr'S_{{m}} = 7,5 \sqrt{{ \frac{{1.5 \cdot W_{2}}}{{f}} }} = 7,5 \sqrt{{ \frac{{{1.5} \cdot {Ws}}}{{50}} }} = 7,5 \sqrt {{{1.5 * Ws / 50}}} = {{{Sm}}} \ cm²')
            
            Sg = round(1.1 * Sm, 2)
            st.latex(fr'S_{{g}} = 1,1 \cdot S_{{m}} = 1,1 \cdot {{{Sm}}} = {{{Sg}}} \ cm²')
            n_lamina = laminas[laminas['a'] >= min(math.sqrt(Sg), 5)].index[0]
            a = laminas['a'][n_lamina]
            b = round(Sg / a, 1)
            Sg = round(a * b, 2)
            Sm = round(Sg / 1.1, 2)
            st.write(f'Dimensões do núcleo central **[{a}] 𝐗 [{b}] 𝐜𝐦**. Emprega-se a lâmina padronizada **𝐧.º {n_lamina}**, resultando o comprimento do núcleo de **{a} 𝐜𝐦**. Nestas condições, as dimensões efetivas do núcleo central resultam:')
            st.latex(fr'S_{{g}} = ({{{a}}}) \cdot ({{{b}}}) = {{{Sg}}} \ cm²; \quad S_{{m}} = \frac{{S_{{g}}}}{{1.1}} = \frac{{{Sg}}}{{1.1}} = {{{Sm}}} \ cm²')
            st.divider()

            st.write(f'-𝐍𝐮́𝐦𝐞𝐫𝐨 𝐝𝐞 𝐥𝐚̂𝐦𝐢𝐧𝐚𝐬: Considerando que a espessura das lâminas padrão seja **𝟏.𝟓 𝐦𝐦**, temos que:')
            b_mag = round(Sm / a, 2)
            n_laminas = round(b_mag / 0.15, 2)
            st.latex(fr'b_{{mag}} = \frac{{Sm}}{{a}} = \frac{{{Sm}}}{{{a}}} = {{{b_mag}}} \ cm')
            st.latex(fr'N_{{laminas}} = \frac{{b_{{mag}}}}{{0.15}} = \frac{{{b_mag}}}{{0.15}} = {{{n_laminas}}} \ Laminas')
            st.divider()

            Vp = Vp1 if cond1 else Vp2
            Vs = Vs1 if cond2 else Vs2
            st.write('-𝐄𝐬𝐩𝐢𝐫𝐚𝐬: Sendo a frequência de **𝟓𝟎 𝐇𝐳**, as espiras por volt resultam:')
            Esp_Volt = round(40 / Sm, 2)
            st.latex(fr'Esp/volt = \frac{{40}}{{S_{{m}}}} = \frac{{40}}{{{Sm}}} = {{{Esp_Volt}}}')
            st.write(f'As espiras do circuito primário cuja tensão é **{Vp} 𝐯𝐨𝐥𝐭𝐬**, resultam:')
            Np = round(Esp_Volt * Vp, 2)
            st.latex(fr'N_{1} = {{{Esp_Volt}}} \cdot V_{1} = {{{Esp_Volt}}} \cdot {{{Vp}}} = {{{Np}}} \ Espiras / circuito')
            st.write('As espiras secundárias devem ser acrescidas de **𝟏𝟎%** a fim de compensar as quedas de tensão, isto é:')
            Ns = round(Esp_Volt * Vs * 1.1, 2)
            st.latex(fr'N_{2} = ({{{Esp_Volt}}}) \cdot (V_{2}) \cdot (1.1) = ({{{Esp_Volt}}}) \cdot ({{{Vs}}}) \cdot (1.1) = {{{Ns}}} \ Espiras / circuito')
            st.divider()

            secao1 = round(secao11 + secao12, 2) if cond1 else secao12
            secao2 = round(secao21 + secao22, 2) if cond2 else secao22
            st.write('-𝐒𝐞𝐜̧𝐚̃𝐨 𝐝𝐨 𝐜𝐨𝐛𝐫𝐞 𝐞𝐧𝐫𝐨𝐥𝐚𝐝𝐨:')
            Scu = round(Np * secao1 + Ns * secao2, 2)
            st.latex(fr'S_{{cu}} = N_{1} S_{1} + N_{2} S_{2} = {{{Np}}} \cdot {{{secao1}}} + {{{Ns}}} \cdot {{{secao2}}} = {{{Scu}}} \ mm²')
            st.divider()

            st.write('-𝐏𝐨𝐬𝐬𝐢𝐛𝐢𝐥𝐢𝐝𝐚𝐝𝐞 𝐝𝐞 𝐞𝐱𝐞𝐜𝐮𝐜̧𝐚̃𝐨:')
            Sj = laminas['secao'][n_lamina]
            st.write(f'Observa-se que a lâmina padronizada **𝐧.º {n_lamina}** tem a janela com **𝐒ᴊ = {Sj} 𝐦𝐦²**, assim sendo, a relação')
            relacao = round(Sj / Scu, 2)
            st.latex(fr'\frac{{S_{{j}}}}{{S_{{cu}}}} = \frac{{{Sj}}}{{{Scu}}} = {{{relacao}}}')
            if relacao >= 3:
                st.write('fornece um resultado 𝐦𝐚𝐢𝐨𝐫 𝐪𝐮𝐞 𝟑, o que indica que o :green[𝐭𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫 𝐞́ 𝐞𝐱𝐞𝐜𝐮𝐭𝐚́𝐯𝐞𝐥].')
            st.divider()

            st.write('-𝐏𝐞𝐬𝐨 𝐝𝐨 𝐟𝐞𝐫𝐫𝐨:')
            peso = laminas['peso'][n_lamina]
            st.write(f'Observa-se que cada centímetro de núcleo feito com a lâmina padronizada **𝐧.º {n_lamina}** pesa **{peso} 𝐤𝐠**. Sendo assim, o peso do núcleo resulta:')
            Pfe = round(peso * b, 2)
            st.latex(fr'P_{{fe}} = {{{peso}}} \cdot {{{b}}} = {{{Pfe}}} \ kg')
            st.divider()

            st.write('-𝐏𝐞𝐬𝐨 𝐝𝐨 𝐜𝐨𝐛𝐫𝐞:')
            st.write('O comprimeto da espira média do cobre resulta:')
            lm = round(2 * a + 2 * b + 0.5 * a * 3.14, 2)
            st.latex(fr'lm = 2a + 2b + 0,5aπ = {{{lm}}} \ cm')
            st.write('de onde:')
            Pcu = round(Scu * lm * 9 / 100 / 1000, 2)
            st.latex(fr'P_{{cu}} = \frac{{S_{{cu}}}}{{100}} \cdot lm \cdot 9 = \frac{{{Scu}}}{{{100}}} \cdot {{{lm}}} \cdot 9 = {{{Pcu * 1000}}} \ g =~ {{{Pcu}}} \ kg')
            st.divider()

            st.write('-𝐏𝐞𝐫𝐝𝐚𝐬 𝐧𝐨 𝐟𝐞𝐫𝐫𝐨:')
            st.write(f'O núcleo do transformador pesa **{Pfe} 𝐤𝐠**.')
            st.write('A perda específica das lâminas Acesita 145, para a indução **𝐁𝐦 = 𝟏𝟏.𝟑𝟎𝟎** e **𝐟 = 𝟓𝟎 𝐇𝐳** resulta:')
            wfe = 1.72
            st.latex(fr'w_{{Fe}} = 1,35 \cdot ( \frac{{11.300}}{{10,000}} )² = {{{wfe}}}')
            st.write('As perdas do núcleo do transformador, resultam:')
            Wfe = round(1.15 * wfe * Pfe, 2)
            st.latex(fr'W_{{Fe}} = 1,15 \cdot w_{{Fe}} \cdot P_{{fe}} = 1,15 \cdot {{{wfe}}} \cdot {{{Pfe}}} = {{{Wfe}}} \ watts')
            st.divider()

            st.write('-𝐏𝐞𝐫𝐝𝐚𝐬 𝐧𝐨 𝐜𝐨𝐛𝐫𝐞:')
            st.write(f'Foi calculada anteriormente a densidade média de corrente no cobre, resultando de **{d_mean} 𝐀/𝐦𝐦²**. Assim sendo, a perda específica no cobre resulta:')
            wcu = round(2.43 * d_mean ** 2, 2)
            st.latex(fr'w_{{cu}} = 2,43 \cdot d² = 2,43 \cdot {{{d_mean}}}² = {{{wcu}}} \ W/kg')
            st.write(f'As perdas no cobre do transformador resultam:')
            Wcu = round(wcu * Pcu, 2)
            st.latex(fr'W_{{cu}} = w_{{cu}} \cdot P_{{cu}} = {{{wcu}}} \cdot {{{Pcu}}} = {{{Wcu}}} \ watts')
            st.divider()

            st.write('-𝐑𝐞𝐧𝐝𝐢𝐦𝐞𝐧𝐭𝐨 𝐝𝐨 𝐭𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫:')
            u = round(Ws / (Ws + Wfe + Wcu), 2)
            st.latex(fr'µ = \frac{{W_{2}}}{{W_{1}}} = \frac{{W_{2}}}{{W_{2} + W_{{fe}} + W_{{cu}}}} = \frac{{{Ws}}}{{{Ws} + {Wfe} + {Wcu}}} = {{{u}}}')
            st.divider()

            st.write('A fim de se anotarem os valores obtidos no cálculo de forma ordenada, serão distribuídos conforme indicado a seguir:')
            st.latex('𝐅𝐎𝐋𝐇𝐀 \ 𝐃𝐄 \ 𝐂𝐀́𝐋𝐂𝐔𝐋𝐎 \ 𝐃𝐎 \ 𝐓𝐑𝐀𝐍𝐒𝐅𝐎𝐑𝐌𝐀𝐃𝐎𝐑')
            st.write(f'𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫 𝐦𝐨𝐧𝐨𝐟𝐚́𝐬𝐢𝐜𝐨: 𝐟 = 𝟓𝟎 𝐇𝐳; 𝐖₂ = {Ws} 𝐕𝐀; 𝐕₁ = [{Vp1}, {Vp2}] 𝐕; 𝐕₂ = [{Vs1}, {Vs2}] 𝐕')
            st.latex(fr'W_{1} = {{{Wp}}} \ | \ V_{1} = {{{Vp2}}} \ | \ I_{1} = {Ip2} \ A \ | \ S_{1} = {{{Sp2}}} \ | \ fio \ {n_awg12} \ ({secao12} \ mm²)')
            if cond1:
                st.latex(fr'I_{1} = {Ip1} \ A \ | \ S_{1} = {{{Sp1}}} \ | \ fio \ {n_awg11} \ ({secao11} \ mm²)')
            st.latex(fr'W_{2} = {{{Ws}}} \ | \ V_{2} = {{{Vs2}}} \ | \ I_{2} = {Is2} \ A \ | \ S_{2} = {{{Ss2}}} \ | \ fio \ {n_awg22} \ ({secao22} \ mm²)')
            if cond2:
                st.latex(fr'I_{2} = {Is1} \ A \ | \ S_{2} = {{{Ss1}}} \ | \ fio \ {n_awg21} \ ({secao21} \ mm²)')
            st.latex(fr'S_{{m}} = {{{Sm}}} \ cm² \ | \ S_{{g}} = {{{Sg}}} \ cm² \ | \ usa-se \ lâmina \ n.º \ {{{n_lamina}}}')
            st.latex(fr'Núcleo \ central \ [{{{a}}}] \ X \ [{{{b}}}]')
            st.latex(fr'b_{{mag}} = {{{b_mag}}} \ cm; \quad N_{{laminas}} = {{{n_laminas}}} \ Laminas')
            st.latex(fr'Esp/volt = {{{Esp_Volt}}}')
            st.latex(fr'N_{1} = {{{Np}}} \ Espiras / circuito')
            st.latex(fr'N_{2} = {{{Ns}}} \ Espiras / circuito')
            st.latex(fr'S_{{cu}} = {{{Scu}}} \ cm²')
            st.latex(fr'\frac{{S_{{j}}}}{{S_{{cu}}}} = {{{relacao}}}')
            st.latex(fr'P_{{fe}} = {{{Pfe}}} \ kg')
            st.latex(fr'lm = {{{lm}}} \ cm')
            st.latex(fr'P_{{cu}} = {{{Pcu}}} \ kg')
            st.latex(fr'W_{{fe}} = {{{Wfe}}} \ watts')
            st.latex(fr'W_{{cu}} = {{{Wcu}}} \ watts')
            st.latex(fr'Rendimento = {{{u}}}')
        except:
            st.info(':red[𝐎𝐜𝐨𝐫𝐫𝐞𝐮 𝐮𝐦 𝐞𝐫𝐫𝐨 𝐝𝐞 𝐞𝐱𝐞𝐜𝐮𝐜̧𝐚̃𝐨 𝐩𝐨𝐫 𝐪𝐮𝐞 𝐝𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚 𝐢𝐧𝐯𝐚́𝐥𝐢𝐝𝐨𝐬 𝐟𝐨𝐫𝐚𝐦 𝐟𝐨𝐫𝐧𝐞𝐜𝐢𝐝𝐨𝐬.]')
