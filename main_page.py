import streamlit as st

st.image('home/models/logo.png')
st.title('𝐏𝐥𝐚𝐭𝐚𝐟𝐨𝐫𝐦𝐚 𝐝𝐞 𝐒𝐮𝐩𝐨𝐫𝐭𝐞 𝐩𝐚𝐫𝐚 𝐏𝐫𝐨𝐣𝐞𝐭𝐨𝐬 𝐝𝐞 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫𝐞𝐬')
st.divider()

pg = st.navigation({"𝐎𝐩𝐜̧𝐨̃𝐞𝐬 𝐝𝐨 𝐀𝐩𝐩":[
     st.Page('home/home_page.py', title='𝐏𝐚́𝐠𝐢𝐧𝐚 𝐈𝐧𝐢𝐜𝐢𝐚𝐥', icon='🏠'),
     st.Page('challenge1/challenge1_page.py', title='𝐃𝐢𝐦𝐞𝐧𝐬𝐢𝐨𝐧𝐚𝐦𝐞𝐧𝐭𝐨', icon='1️⃣'),
     st.Page('challenge2/challenge2_page.py', title='𝐂𝐨𝐫𝐫𝐞𝐧𝐭𝐞 𝐝𝐞 𝐌𝐚𝐠𝐧𝐞𝐭𝐢𝐳𝐚çã𝐨', icon='2️⃣'),
     st.Page('challenge3/challenge3_page.py', title='𝐏𝐚𝐫â𝐦𝐞𝐭𝐫𝐨𝐬 𝐝𝐨 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫', icon='3️⃣'),
     st.Page('challenge4/challenge4_page.py', title='𝐑𝐞𝐠𝐮𝐥𝐚çã𝐨 𝐝𝐨 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐚𝐝𝐨𝐫', icon='4️⃣'),
     st.Page('credits/credits_page.py', title='𝐂𝐫𝐞́𝐝𝐢𝐭𝐨𝐬', icon='©️')
]})

pg.run()