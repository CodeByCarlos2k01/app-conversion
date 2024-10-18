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
    if Zphi**2 - Rc**2 >= 0:
        Xm = math.sqrt(Zphi**2 - Rc**2)  # Reatância de magnetização
    else:
        Xm = 0  # Evita erro de domínio
    return Rc, Zphi, Xm  # Agora estamos retornando os 3 valores: Rc, Zphi, Xm

# Função para calcular parâmetros de curto-circuito
def calcular_parametros_curto_circuito(Vcc, Icc, Pcc):
    Zcc = Vcc / Icc  # Impedância de curto-circuito
    Req = Pcc / Icc**2  # Resistência equivalente
    Xeq = math.sqrt(Zcc**2 - Req**2)  # Reatância equivalente
    return Req, Zcc, Xeq  # Retorna 3 valores

st.title(':blue[𝐒𝐞𝐜̧𝐚̃𝐨 𝟑]')
st.title('Determinação dos parâmetros do transformador monofásico')

st.markdown('Coloca um texto aqui explicando do que se trata a seção.')
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚')
    st.markdown('• Ensaio de Circuito Aberto: Vca/ Ica/Pca')
    st.markdown('• Ensaio de Curto-circuito: Vcc/Icc/Pcc')
with col2:
    st.subheader('𝐃𝐚𝐝𝐨𝐬 𝐝𝐞 𝐬𝐚𝐢́𝐝𝐚')
    st.markdown('• Parâmetros do transformador')
    st.markdown('• Característica fasorial do transformador')
    st.markdown('• Imagem ilustrando os parâmetros do transformador')

st.divider()

# Interface do Streamlit
st.title("Dados de Entrada")
col1, col2 = st.columns(2)

# Relação de transformação
n = col1.number_input("Relação de Transformação [𝐧 = 𝐕_𝐚𝐥𝐭𝐚 / 𝐕_𝐛𝐚𝐢𝐱𝐚]", value=20.0)

# Escolha da saída (alta ou baixa tensão)
lado_saida = col2.radio("Deseja que os resultados sejam referidos ao lado de:", ("Alta Tensão", "Baixa Tensão"))

# Escolha do tipo de ensaio
tipo_ensaio = st.selectbox("Escolha o tipo de ensaio", ["Circuito Aberto", "Curto-Circuito"])
st.divider()

# Exibição dos inputs com base na escolha
if tipo_ensaio == "Circuito Aberto":

    st.subheader("Dados para Ensaio de Circuito Aberto")
    col1, col2, col3 = st.columns(3)

    with col1:
        Vca = st.number_input("Tensão Circuito Aberto (𝐕𝐜𝐚)", value=240.0)
        lado_Vca = st.radio("A tensão (𝐕𝐜𝐚) está em:", ("Alta Tensão", "Baixa Tensão"), key="Vca")
    with col2:
        Ica = st.number_input("Corrente Circuito Aberto (𝐈𝐜𝐚)", value=1.8)
        lado_Ica = st.radio("A corrente (𝐈𝐜𝐚) está em:", ("Alta Tensão", "Baixa Tensão"), key="Ica")
    with col3:
        Pca = st.number_input("Potência Circuito Aberto (𝐏𝐜𝐚)", value=154.0)
        lado_Pca = st.radio("A potência (𝐏𝐜𝐚) está em:", ("Alta Tensão", "Baixa Tensão"), key="Pca")
    
    # Conversão dos valores para o lado de saída
    Vca_conv = converter(Vca, n, lado_Vca, lado_saida)
    Ica_conv = converter(Ica, n, lado_Ica, lado_saida)
    Pca_conv = converter(Pca, n, lado_Pca, lado_saida)

    # Cálculo de Circuito Aberto
    if st.button("Calcular Circuito Aberto"):
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

elif tipo_ensaio == "Curto-Circuito":

    st.subheader("Dados para Ensaio de Curto-Circuito")
    col1, col2, col3 = st.columns(3)

    with col1:
        Vcc = st.number_input("Tensão Curto-Circuito (𝐕𝐜𝐜)", value=350.0)
        lado_Vcc = st.radio("A tensão (𝐕𝐜𝐜) está em:", ("Alta Tensão", "Baixa Tensão"), key="Vcc")
    with col2:
        Icc = st.number_input("Corrente Curto-Circuito (𝐈𝐜𝐜)", value=2.07)
        lado_Icc = st.radio("A corrente (𝐈𝐜𝐜) está em:", ("Alta Tensão", "Baixa Tensão"), key="Icc")
    with col3:
        Pcc = st.number_input("Potência Curto-Circuito (𝐏𝐜𝐜)", value=210.0)
        lado_Pcc = st.radio("A potência (𝐏𝐜𝐜) está em:", ("Alta Tensão", "Baixa Tensão"), key="Pcc")
    
    # Conversão dos valores para o lado de saída
    Vcc_conv = converter(Vcc, n, lado_Vcc, lado_saida)
    Icc_conv = converter(Icc, n, lado_Icc, lado_saida)
    Pcc_conv = converter(Pcc, n, lado_Pcc, lado_saida)

    # Cálculo de Curto-Circuito
    if st.button("Calcular Curto-Circuito"):
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