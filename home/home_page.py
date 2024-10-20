import streamlit as st

st.title('Página Inicial')
st.markdown('A ferramenta surge com o propósito de facilitar o desenvolvimento, assim como a gestão dos transformadores de tensão. Dispositivos esses que tem uma importância inestimável para o nosso sistema elétrico nos dias atuais.')
st.divider()

st.title('Sobre transformadores')
st.markdown('Os transformadores são dispositivos elétricos usados para transferir energia elétrica entre dois ou mais circuitos através de indução eletromagnética. Eles funcionam com corrente alternada (CA) e são amplamente utilizados para aumentar (transformador elevador) ou reduzir (transformador abaixador) a tensão de um sistema elétrico, dependendo das necessidades.')
st.markdown('Quando uma corrente alternada passa pela bobina primária, cria-se um campo magnético que, por sua vez, induz uma corrente na bobina secundária. A relação entre o número de voltas nas bobinas determina a transformação da tensão.')
st.write('')

col1, col2 = st.columns(2)
with col1:
    st.image('home/models/transformador_1.png', caption='𝐼𝑙𝑢𝑠𝑡𝑟𝑎𝑐̧𝑎̃𝑜 1')
with col2:
    st.image('home/models/transformador_2.png', caption='𝐼𝑙𝑢𝑠𝑡𝑟𝑎𝑐̧𝑎̃𝑜 2')
st.divider()

st.title('Sobre a ferramenta')
st.markdown('Esta aplicação contém 4 (quatro) funcionalidades que estão isoladamente presentes em cada uma das seções. A partir dos resultados gerados será possível avaliar a estratégia de resolução utilizada pelo algoritmo, para que sejam compreendidos e validados.')
st.divider()

st.subheader(':blue[𝟏.] 𝐃𝐢𝐦𝐞𝐧𝐬𝐢𝐨𝐧𝐚𝐦𝐞𝐧𝐭𝐨 𝐝𝐨 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫')
st.markdown('O dimensionamento de um transformador monofásico serve para garantir que o equipamento seja capaz de atender às necessidades específicas de um sistema elétrico, operando com segurança e eficiência. Esse processo envolve calcular as capacidades elétricas adequadas.')
st.subheader(':blue[𝟐.] 𝐂𝐮𝐫𝐯𝐚 𝐝𝐚 𝐂𝐨𝐫𝐫𝐞𝐧𝐭𝐞 𝐝𝐞 𝐌𝐚𝐠𝐧𝐞𝐭𝐢𝐳𝐚𝐜̧𝐚̃𝐨')
st.markdown('Coloca o texto da seção 2 aqui')
st.subheader(':blue[𝟑.] 𝐂𝐚́𝐥𝐜𝐮𝐥𝐨 𝐝𝐞 𝐏𝐚𝐫𝐚̂𝐦𝐞𝐭𝐫𝐨𝐬 𝐝𝐨 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫')
st.markdown('''A determinação dos parâmetros do transformador monofásico é realizada através dos ensaios 
de circuito aberto e curto-circuito, usando os valores de tensão, corrente e potência. Esses ensaios permitem 
calcular os parâmetros do transformador, como resistência e reatância, além de obter suas características fasoriais.''')
st.subheader(':blue[𝟒.] 𝐂𝐚́𝐥𝐜𝐮𝐥𝐨 𝐝𝐚 𝐑𝐞𝐠𝐮𝐥𝐚𝐜̧𝐚̃𝐨 𝐝𝐨 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫')
st.markdown('Calcular a regulação de um transformador é fundamental para garantir que ele funcione eficientemente em diversas condições de carga, assegurando a qualidade da energia, otimizando o desempenho do sistema e permitindo um planejamento de manutenção mais eficaz. ')