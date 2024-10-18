import streamlit as st
import pandas as pd
import math

if 'challenge1' not in st.session_state:
    st.session_state['challenge1'] = False
    st.session_state['challenge1_Vp1'] = 0.0
    st.session_state['challenge1_Vp2'] = 0.0
    st.session_state['challenge1_Vs1'] = 0.0
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
    Vp1 = col1.number_input("Informe a Tensão Primária do circuito 1 em Volts", min_value = 0.0)
    Vp2 = col2.number_input("Informe a Tensão Primária do circuito 2 em Volts", min_value = 0.0)
    (Vp1, Vp2) = (st.session_state['challenge1_Vp1'], st.session_state['challenge1_Vp2']) if ((Vp1, Vp2) == (0, 0)) else (Vp1, Vp2)

    st.subheader('Tensão Secundária')
    col1, col2 = st.columns(2)
    Vs1 = col1.number_input("Informe a Tensão Secundária do circuito 1 em Volts", min_value = 0.0)
    Vs2 = col2.number_input("Informe a Tensão Secundária do circuito 2 em Volts", min_value = 0.0)
    (Vs1, Vs2) = (st.session_state['challenge1_Vs1'], st.session_state['challenge1_Vs2']) if ((Vs1, Vs2) == (0, 0)) else (Vs1, Vs2)

    st.subheader('Potência da Carga')
    Ws = st.number_input("Informe a Potência da carga em Volt-Ampere", min_value = 0.0, max_value = 800.0)
    Ws = st.session_state['challenge1_Ws'] if Ws == 0 else Ws

    if (st.form_submit_button('Gerar Resultado') or st.session_state['challenge1']):

        (Vp1, Vp2) = (0.0, max(Vp1, Vp2)) if (0.0 in [Vp1, Vp2]) else (Vp1, Vp2)
        (Vs1, Vs2) = (0.0, max(Vs1, Vs2)) if (0.0 in [Vs1, Vs2]) else (Vs1, Vs2)

        st.session_state['challenge1'] = True
        st.session_state['challenge1_Vp1'], st.session_state['challenge1_Vp2'] = Vp1, Vp2
        st.session_state['challenge1_Vs1'], st.session_state['challenge1_Vs2'] = Vs1, Vs2
        st.session_state['challenge1_Ws'] = Ws

        st.divider()
        st.subheader('Cálculo do Transformador Monofásico (Solução)')
        st.write(f'**Dados do Transformador monofásico:**')
        st.latex(fr'f = 50 \ Hz')
        st.latex(fr'W_{2} = {{{Ws}}} \ Va')
        st.latex(fr'V_{1} = {{{Vp1}}}/{{{Vp2}}} \ V')
        st.latex(fr'V_{2} = {{{Vs1}}}/{{{Vs2}}} \ V')

        Wp = round(1.1 * Ws, 2)
        st.write('-*Potência primária:*')
        st.latex(fr'W_{1} = 1,1 \cdot W_{2} = 1,1 \cdot ({{{Ws}}}) = {{{Wp}}} \ Va')

        Ip = round(Wp / Vp2, 2)
        st.write('-*Corrente primária:*')
        st.latex(fr'I_{1} = \frac{{W_{1}}}{{V_{1}}} = \frac{{{Wp}}}{{{Vp2}}} = {{{Ip}}} \ A')

        Is = round(Ws / Vs2, 2)
        st.write('-*Corrente secundária:*')
        st.latex(fr'I_{2} = \frac{{W_{2}}}{{V_{2}}} = \frac{{{Ws}}}{{{Vs2}}} = {{{Is}}} \ A')

        d = secao_condutor[secao_condutor['potencia'] > Ws]['densidade'].max()
        st.write(f'Escolhendo-se a densidade de corrente **d = {d} A/mm²**, obtém-se:')

        Sp = round(Ip / d, 2)
        st.latex(fr'- Secão \ do \ condutor \ primário: S_{1} = \frac{{I_{1}}}{{d}} = \frac{{{Ip}}}{{{d}}} = {{{Sp}}} \ mm²')
        idx = awg[awg['secao'] >= Sp].shape[0] - 1 
        secao1, n_awg = awg['secao'][idx], awg['numero'][idx]
        st.write(f'**Usa-se fio n.º {n_awg} (AWG) cuja seção é S₁ = {secao1} mm²**')

        Ss = round(Is / d, 2)
        st.latex(fr'- Secão \ do \ condutor \ secundário: S_{2} = \frac{{I_{2}}}{{d}} = \frac{{{Is}}}{{{d}}} = {{{Ss}}} \ mm²')
        idx = awg[awg['secao'] >= Ss].shape[0] - 1 
        secao2, n_awg = awg['secao'][idx], awg['numero'][idx]
        st.write(f'**Usa-se fio n.º {n_awg} (AWG) cuja seção é S₂ = {secao2} mm²**')

        st.write('**N.B. Em ambos os enrolamentos a densidade de corrente resulta inferior ou igual à prevista, isto é:**')
        dp = round(Ip / secao1, 2)
        st.latex(fr'd₁ = \frac{{I₁}}{{S₁}} = \frac{{{Ip}}}{{{Sp}}} = {{{dp}}} \ A/mm²')
        ds = round(Is / secao2, 2)
        st.latex(fr'd₂ = \frac{{I₂}}{{S₂}} = \frac{{{Is}}}{{{Ss}}} = {{{ds}}} \ A/mm²')
        st.write('Para o cálculo da perda no cobre considera-se a densidade média de:')
        d_mean = round((dp + ds) / 2, 2)
        st.latex(fr'd = {{{d_mean}}} \ A/mm²')

        st.write('-*Seção magnética do núcleo:* como o transformador possui um circuito primário e um circuito secundário, emprega-se a fórmula:')
        Sm = round(7.5 * math.sqrt(Ws / 50), 2)
        st.latex(fr'S_{{m}} = 7,5 \sqrt{{ \frac{{W_{2}}}{{f}} }} = 7,5 \sqrt{{ \frac{{{Ws}}}{{50}} }} = 7,5 \sqrt {{{Ws / 50}}} = {{{Sm}}} \ cm²')
        Sg = round(1.1 * Sm, 2)
        st.latex(fr'S_{{g}} = 1,1 \cdot S_{{m}} = 1,1 \cdot {{{Sm}}} = {{{Sg}}} \ cm²')

        n_lamina = laminas[laminas['a'] >= math.sqrt(Sg)].index[0]
        a = laminas['a'][n_lamina]
        b = round(Sg / a)
        Sg = round(a * b, 2)
        Sm = round(Sg / 1.1, 2)
        st.write(f'Dimensões do núcleo central **[{a}] X [{b}] cm**. Emprega-se a lâmina padronizada n.º {n_lamina}, resultando o comprimento do núcleo de **{a} cm**. Nestas condições, as dimensões efetivas do núcleo central resultam:')
        st.latex(fr'S_{{g}} = ({{{a}}}) \cdot ({{{b}}}) = {{{Sg}}} \ cm²; \quad S_{{m}} = \frac{{S_{{g}}}}{{1.1}} = \frac{{{Sg}}}{{1.1}} = {{{Sm}}} \ cm²')

        st.write('-*Espiras:* Sendo a frequência de 50 Hz, as espiras por volt resultam:')
        Esp_Volt = round(40 / Sm, 2)
        st.latex(fr'Esp/volt = \frac{{40}}{{S_{{m}}}} = \frac{{40}}{{{Sm}}} = {{{Esp_Volt}}}')

        st.write(f'As espiras do circuito primário cuja tensão é {Vp2} volts, resultam:')

        Np = round(Esp_Volt * Vp2, 2)
        st.latex(fr'N_{1} = {{{Esp_Volt}}} \cdot V_{1} = {{{Esp_Volt}}} \cdot {{{Vp2}}} = {{{Np}}}')

        st.write('As espiras secundárias devem ser acrescidas de 10% a fim de compensar as quedas de tensão, isto é:')

        Ns = round(Esp_Volt * Vs2 * 1.1, 2)
        st.latex(fr'N_{2} = ({{{Esp_Volt}}}) \cdot (V_{2}) \cdot (1.1) = ({{{Esp_Volt}}}) \cdot ({{{Vs2}}}) \cdot (1.1) = {{{Ns}}}')
        
        st.divider()
        col1, col2 = st.columns(2)
        col1.subheader('Transformador Tipo 1')
        col1.markdown('1 circuito no primário e 1 circuito no secundário')
        col2.image('challenge1/models/circuito1.png')
        st.write('**N.B. O esquema do transformador toma a forma indicada na figura.**')

    