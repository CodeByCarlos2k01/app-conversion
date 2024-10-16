import streamlit as st

st.title('Página Inicial')
st.markdown('A ferramenta surge com o propósito de facilitar o desenvolvimento, assim como a gestão dos transformadores de tensão. Dispositivos esses que tem uma importância inestimável para o nosso sistema elétrico nos dias atuais.')
st.divider()

st.title('Sobre transformadores')
st.markdown('Os transformadores são dispositivos elétricos usados para transferir energia elétrica entre dois ou mais circuitos através de indução eletromagnética. Eles funcionam com corrente alternada (CA) e são amplamente utilizados para aumentar (transformador elevador) ou reduzir (transformador abaixador) a tensão de um sistema elétrico, dependendo das necessidades.')

st.subheader('Como funciona')
st.markdown('Quando uma corrente alternada passa pela bobina primária, cria-se um campo magnético que, por sua vez, induz uma corrente na bobina secundária. A relação entre o número de voltas nas bobinas determina a transformação da tensão.')

st.write('')

col1, col2 = st.columns(2)
with col1:
    st.image('home/models/transformador_1.png')
with col2:
    st.image('home/models/transformador_2.png')
st.divider()

st.title('Sobre a ferramenta')
st.markdown('Texto...')