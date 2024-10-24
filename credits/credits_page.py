import streamlit as st

st.title('Créditos')
st.markdown('Esse projeto foi desenvolvido por uma equipe de estudantes de Engenharia de Computação da Universidade de Pernambuco (UPE) com propósito educacional sobre transformadores e eletromagnetismo.')
st.divider()

st.subheader('𝐓𝐢𝐦𝐞 𝐝𝐞 𝐃𝐞𝐬𝐞𝐧𝐯𝐨𝐥𝐯𝐢𝐦𝐞𝐧𝐭𝐨')
col1, col2, col3, col4 = st.columns(4)
col1.image('credits/models/carlos.png', caption='Carlos Eduardo')
col2.image('credits/models/george.png', caption='George Vieira')
col3.image('credits/models/pedro.png', caption='Pedro Hirschle')
col4.image('credits/models/riquelme.png', caption='Riquelme Lopes')
st.divider()

st.subheader('𝐏𝐫𝐨𝐟𝐞𝐬𝐬𝐨𝐫 𝐑𝐞𝐬𝐩𝐨𝐧𝐬á𝐯𝐞𝐥')
st.image('credits/models/professor.png', caption='Raimundo Lima')
st.divider()

st.subheader('𝐈𝐧𝐬𝐭𝐢𝐭𝐮𝐢çã𝐨 𝐝𝐞 𝐄𝐧𝐬𝐢𝐧𝐨')
col1, col2, col3 = st.columns(3)
col1.image('credits/models/upe.png')
col2.image('credits/models/poli.png')
col3.image('credits/models/ecomp.png')