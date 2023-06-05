import streamlit
import streamlit as st
import folium
import streamlit_folium
from streamlit_folium import folium_static

#Layout da página
name = "Mapa da Desigualdade"
st.set_page_config(layout="wide", page_title=name)

#Opções do menu
st.sidebar.markdown('# Mapa da Desigualdade')
options = st.sidebar.selectbox("Selecione uma opção:", ("Paraná", "Núcleo Territorial Central"))

st.text('Fixed width text: st.text')
st.markdown('_Markdown_') # see *
st.caption('Balloons. Hundreds of them: st.caption') 
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects: st.write') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub: st.subheader')
st.code('for i in range(8): foo()')

st.button('Hit me')
#st.download_button('On the dl', data)
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')

if options == "Paraná":
  st.subheader("Mapa da Desigualdade do Paraná")
  categoria = st.sidebar.selectbox("Selecione uma categoria:", ("Renda e Riqueza", "Categoria 2", "Categoria 3", "Categoria 4"))
  st.sidebar.markdown("**Dica:** Feche este menu para uma melhor visualização dos mapas.")
  if categoria == "Renda e Riqueza":
    st.header("Renda e Riqueza do Paraná")
