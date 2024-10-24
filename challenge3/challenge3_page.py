import streamlit as st
import math

# Função para conversão de alta para baixa ou baixa para alta
def converter(valor, n, lado_entrada, lado_saida):
    if lado_entrada == "Baixa Tensão" and lado_saida == "Alta Tensão":
        return valor * n
    elif lado_entrada == "Alta Tensão" and lado_saida == "Baixa Tensão":
        return valor / n
    else:
        return valor

# Função para calcular parâmetros de circuito aberto
def calcular_parametros_circuito_aberto(Vca, Ica, Pca):
    Rc = Vca**2 / Pca  # Resistência do núcleo
    Zphi = Vca / Ica  # Impedância do ramo de magnetização    
    # Cálculo da reatância de magnetização 
    if (1/Zphi)**2 - (1/Rc)**2 > 0:
        Xm = 1 / math.sqrt((1/Zphi)**2 - (1/Rc)**2)
    else:
        Xm = 0  # Evita erro de domínio
    
    return Rc, Zphi, Xm

# Função para calcular parâmetros de curto-circuito
def calcular_parametros_curto_circuito(Vcc, Icc, Pcc):
    Zcc = Vcc / Icc  # Impedância de curto-circuito
    Req = Pcc / Icc**2  # Resistência equivalente
    Xeq = math.sqrt(Zcc**2 - Req**2)  # Reatância equivalente
    return Req, Zcc, Xeq  # Retorna 3 valores

if 'challenge3' not in st.session_state:
    st.session_state['challenge3'] = True
    st.session_state['challenge3_btn1'] = False
    st.session_state['challenge3_btn2'] = False
    st.session_state['challenge3_n'] = 0.0
    st.session_state['challenge3_lado_saida']  = "Alta Tensão"
    st.session_state['challenge3_tipo_ensaio'] = "Circuito Aberto"
    st.session_state['challenge3_Ica'] = 0.0
    st.session_state['challenge3_Vca'] = 0.0
    st.session_state['challenge3_Pca'] = 0.0
    st.session_state['challenge3_lado_Vca'] = "Alta Tensão"
    st.session_state['challenge3_lado_Ica'] = "Alta Tensão"
    st.session_state['challenge3_lado_Pca'] = "Alta Tensão"
    st.session_state['challenge3_Icc'] = 0.0
    st.session_state['challenge3_Vcc'] = 0.0
    st.session_state['challenge3_Pcc'] = 0.0
    st.session_state['challenge3_lado_Vcc'] = "Alta Tensão"
    st.session_state['challenge3_lado_Icc'] = "Alta Tensão"
    st.session_state['challenge3_lado_Pcc'] = "Alta Tensão"

st.title(':blue[𝐒𝐞çã𝐨 𝟑]')

st.title('Determinação dos parâmetros do transformador monofásico')
st.markdown('''A determinação dos parâmetros do transformador monofásico é realizada através dos ensaios de circuito aberto e curto-circuito, usando os valores de tensão, corrente e potência. Esses ensaios permitem calcular os parâmetros do transformador, como resistência e reatância, além de obter suas características fasoriais.''')
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚')
    st.markdown('• Ensaio de Circuito Aberto: Vca/ Ica/Pca')
    st.markdown('• Ensaio de Curto-circuito: Vcc/Icc/Pcc')
with col2:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐬𝐚í𝐝𝐚')
    st.markdown('• Parâmetros do transformador')
    st.markdown('• Característica fasorial do transformador')
    st.markdown('• Imagem ilustrando os parâmetros do transformador')
st.divider()

# Interface do Streamlit
st.title("Dados de Entrada")
with st.expander('', expanded=True):
    col1, col2 = st.columns(2)

    # Relação de transformação
    n = col1.number_input("Relação de Transformação [𝐧 = 𝐕_𝐚𝐥𝐭𝐚 / 𝐕_𝐛𝐚𝐢𝐱𝐚]", step=10.0)
    n = st.session_state['challenge3_n'] if n == 0 else n

    # Escolha da saída (alta ou baixa tensão)
    lado_saida = col2.radio("Deseja que os resultados sejam referidos ao lado de:", ("Alta Tensão", "Baixa Tensão"))

    # Escolha do tipo de ensaio
    tipo_ensaio = st.selectbox("Escolha o tipo de ensaio", ["", "Circuito Aberto", "Curto-Circuito"])
    (tipo_ensaio, lado_saida) = (st.session_state['challenge3_tipo_ensaio'], st.session_state['challenge3_lado_saida']) if tipo_ensaio == "" else (tipo_ensaio, lado_saida)

# Exibição dos inputs com base na escolha
if tipo_ensaio == "Circuito Aberto":
    with st.form('challenge3_form'):
        st.subheader("Dados para Ensaio de Circuito Aberto")
        col1, col2, col3 = st.columns(3)

        with col1:
            Vca = st.number_input("Tensão Circuito Aberto (𝐕𝐜𝐚)", step=10.0)
            lado_Vca = st.radio("A tensão (𝐕𝐜𝐚) está em:", ("Alta Tensão", "Baixa Tensão"), key="Vca")
            (Vca, lado_Vca) = (st.session_state['challenge3_Vca'], st.session_state['challenge3_lado_Vca']) if Vca == 0 else (Vca, lado_Vca)
        with col2:
            Ica = st.number_input("Corrente Circuito Aberto (𝐈𝐜𝐚)", step=10.0)
            lado_Ica = st.radio("A corrente (𝐈𝐜𝐚) está em:", ("Alta Tensão", "Baixa Tensão"), key="Ica")
            (Ica, lado_Ica) = (st.session_state['challenge3_Ica'], st.session_state['challenge3_lado_Ica']) if Ica == 0 else (Ica, lado_Ica)
        with col3:
            Pca = st.number_input("Potência Circuito Aberto (𝐏𝐜𝐚)", step=10.0)
            lado_Pca = st.radio("A potência (𝐏𝐜𝐚) está em:", ("Alta Tensão", "Baixa Tensão"), key="Pca")
            (Pca, lado_Pca) = (st.session_state['challenge3_Pca'], st.session_state['challenge3_lado_Pca']) if Pca == 0 else (Pca, lado_Pca)

        # Conversão dos valores para o lado de saída
        Vca_conv = converter(Vca, n, lado_Vca, lado_saida)
        Ica_conv = converter(Ica, n, lado_Ica, lado_saida)
        Pca_conv = converter(Pca, n, lado_Pca, lado_saida)
        st.write('')

        challenge3_button1 = st.form_submit_button("Calcular Circuito Aberto")

    # Cálculo de Circuito Aberto
    if (challenge3_button1 or st.session_state['challenge3_btn1']):
        st.session_state['challenge3_btn1'] = True
        st.session_state['challenge3_n'] = n
        st.session_state['challenge3_lado_saida']  = lado_saida
        st.session_state['challenge3_tipo_ensaio'] = tipo_ensaio
        st.session_state['challenge3_Ica'] = Ica
        st.session_state['challenge3_Vca'] = Vca
        st.session_state['challenge3_Pca'] = Pca
        st.session_state['challenge3_lado_Vca'] = lado_Vca
        st.session_state['challenge3_lado_Ica'] = lado_Ica
        st.session_state['challenge3_lado_Pca'] = lado_Pca

        st.title('Resultado')
        with st.expander('Passo a Passo da Resolução', expanded=True):
            try:
                Rc, Zphi, Xm = calcular_parametros_circuito_aberto(Vca_conv, Ica_conv, Pca_conv)
                
                # Explicação detalhada dos cálculos
                st.markdown("### Explicação dos Cálculos Realizados: Circuito Aberto")
                
                # Explicação passo a passo
                st.markdown("#### 1. Cálculo da Resistência do Núcleo ($R_c$):")
                st.latex(r"R_c = \frac{V_{ca}^2}{P_{ca}}")
                st.latex(f"R_c = \\frac{{{Vca_conv}^2}}{{{Pca_conv}}} = {Rc:.2f} \, \text{{ohms}}")
                
                st.markdown("#### 2. Cálculo da Impedância do Ramo de Magnetização ($Z_\\varphi$):")
                st.latex(r"Z_\varphi = \frac{V_{ca}}{I_{ca}}")
                st.latex(f"Z_\\varphi = \\frac{{{Vca_conv}}}{{{Ica_conv}}} = {Zphi:.2f} \, \text{{ohms}}")
                
                st.markdown("#### 3. Cálculo da Reatância de Magnetização ($X_m$):")
                st.latex(r"X_m = \sqrt{Z_\varphi^2 - R_c^2}")
                st.latex(f"X_m = \\sqrt{{{Zphi:.2f}^2 - {Rc:.2f}^2}} = {Xm:.2f} \, \text{{ohms}}")
            except:
                st.error(':blue[𝐎𝐜𝐨𝐫𝐫𝐞𝐮 𝐮𝐦 𝐞𝐫𝐫𝐨 𝐝𝐞 𝐞𝐱𝐞𝐜𝐮çã𝐨 𝐩𝐨𝐫 𝐪𝐮𝐞 𝐝𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚 𝐢𝐧𝐯á𝐥𝐢𝐝𝐨𝐬 𝐟𝐨𝐫𝐚𝐦 𝐟𝐨𝐫𝐧𝐞𝐜𝐢𝐝𝐨𝐬.]')

elif tipo_ensaio == "Curto-Circuito":
    with st.form('challenge3_form'):
        st.subheader("Dados para Ensaio de Curto-Circuito")
        col1, col2, col3 = st.columns(3)

        with col1:
            Vcc = st.number_input("Tensão Curto-Circuito (𝐕𝐜𝐜)", step=10.0)
            lado_Vcc = st.radio("A tensão (𝐕𝐜𝐜) está em:", ("Alta Tensão", "Baixa Tensão"), key="Vcc")
            (Vcc, lado_Vcc) = (st.session_state['challenge3_Vcc'], st.session_state['challenge3_lado_Vcc']) if Vcc == 0 else (Vcc, lado_Vcc)
        with col2:
            Icc = st.number_input("Corrente Curto-Circuito (𝐈𝐜𝐜)", step=10.0)
            lado_Icc = st.radio("A corrente (𝐈𝐜𝐜) está em:", ("Alta Tensão", "Baixa Tensão"), key="Icc")
            (Icc, lado_Icc) = (st.session_state['challenge3_Icc'], st.session_state['challenge3_lado_Icc']) if Icc == 0 else (Icc, lado_Icc)
        with col3:
            Pcc = st.number_input("Potência Curto-Circuito (𝐏𝐜𝐜)", step=10.0)
            lado_Pcc = st.radio("A potência (𝐏𝐜𝐜) está em:", ("Alta Tensão", "Baixa Tensão"), key="Pcc")
            (Pcc, lado_Pcc) = (st.session_state['challenge3_Pcc'], st.session_state['challenge3_lado_Pcc']) if Pcc == 0 else (Pcc, lado_Pcc)
        
        # Conversão dos valores para o lado de saída
        Vcc_conv = converter(Vcc, n, lado_Vcc, lado_saida)
        Icc_conv = converter(Icc, n, lado_Icc, lado_saida)
        Pcc_conv = converter(Pcc, n, lado_Pcc, lado_saida)
        st.write('')

        challenge3_button2 = st.form_submit_button("Calcular Curto-Circuito")

    # Cálculo de Curto-Circuito
    if (challenge3_button2 or st.session_state['challenge3_btn2']):
        st.session_state['challenge3_btn2'] = True
        st.session_state['challenge3_n'] = n
        st.session_state['challenge3_lado_saida']  = lado_saida
        st.session_state['challenge3_tipo_ensaio'] = tipo_ensaio
        st.session_state['challenge3_Icc'] = Icc
        st.session_state['challenge3_Vcc'] = Vcc
        st.session_state['challenge3_Pcc'] = Pcc
        st.session_state['challenge3_lado_Vcc'] = lado_Vcc
        st.session_state['challenge3_lado_Icc'] = lado_Icc
        st.session_state['challenge3_lado_Pcc'] = lado_Pcc

        st.title('Resultado')
        with st.expander('Passo a Passo da Resolução', expanded=True):
            try:
                Req, Zcc, Xeq = calcular_parametros_curto_circuito(Vcc_conv, Icc_conv, Pcc_conv)
                
                # Explicação detalhada dos cálculos
                st.markdown("### Explicação dos Cálculos Realizados: Curto-Circuito")
                
                st.markdown("#### 1. Cálculo da Impedância de Curto-Circuito ($Z_{cc}$):")
                st.latex(r"Z_{cc} = \frac{V_{cc}}{I_{cc}}")
                st.latex(f"Z_{{cc}} = \\frac{{{Vcc_conv}}}{{{Icc_conv}}} = {Zcc:.2f} \, \text{{ohms}}")

                st.markdown("#### 2. Cálculo da Resistência Equivalente ($R_{eq}$):")
                st.latex(r"R_{eq} = \frac{P_{cc}}{I_{cc}^2}")
                st.latex(f"R_{{eq}} = \\frac{{{Pcc_conv}}}{{{Icc_conv}^2}} = {Req:.2f} \, \text{{ohms}}")
                
                st.markdown("#### 3. Cálculo da Reatância Equivalente ($X_{eq}$):")
                st.latex(r"X_{eq} = \sqrt{Z_{cc}^2 - R_{eq}^2}")
                st.latex(f"X_{{eq}} = \\sqrt{{{Zcc:.2f}^2 - {Req:.2f}^2}} = {Xeq:.2f} \, \text{{ohms}}")
            except:
                st.error(':blue[𝐎𝐜𝐨𝐫𝐫𝐞𝐮 𝐮𝐦 𝐞𝐫𝐫𝐨 𝐝𝐞 𝐞𝐱𝐞𝐜𝐮çã𝐨 𝐩𝐨𝐫 𝐪𝐮𝐞 𝐝𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚 𝐢𝐧𝐯á𝐥𝐢𝐝𝐨𝐬 𝐟𝐨𝐫𝐚𝐦 𝐟𝐨𝐫𝐧𝐞𝐜𝐢𝐝𝐨𝐬.]')
