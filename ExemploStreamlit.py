import streamlit
import streamlit as st

#Layout da página
name = "Mapa da Desigualdade"
st.set_page_config(layout="wide", page_title=name)

#Opções do menu
st.sidebar.markdown('# Mapa da Desigualdade')
options = st.sidebar.selectbox("Selecione uma opção:", ("Paraná", "Núcleo Territorial Central"))

if options == "Paraná":
  st.subheader("Mapa da Desigualdade do Paraná")
  categoria = st.sidebar.selectbox("Selecione uma categoria:", ("Renda e Riqueza", "Categoria 2", "Categoria 3", "Categoria 4"))
  st.sidebar.markdown("**Dica:** Feche este menu para uma melhor visualização dos mapas.")
  if categoria == "Renda e Riqueza":
    st.header("Renda e Riqueza do Paraná")
    st.header("Década de 1870")
    col1, col2 = st.columns(2)
    with col1:
      st.text('Fixed width text: st.text')
      st.markdown('_Markdown_') # see *
      st.caption('Balloons. Hundreds of them: st.caption') 
      st.latex(r''' e^{i\pi} + 1 = 0 ''')
      st.write('Most objects: st.write') # df, err, func, keras!
    with col2:
      st.write(['st', 'is <', 3]) # see *
      st.title('My title')
      st.header('My header')
      st.subheader('My sub: st.subheader')
      st.code('for i in range(8): foo()')
  elif categoria == "Categoria 2":
    st.button('Hit me')
    #st.download_button('On the dl', data)
    st.checkbox('Check me out')
    st.radio('Radio', [1,2,3])
    st.selectbox('Select', [1,2,3])
    st.multiselect('Multiselect', [1,2,3])
  else:
    col1, col2, col3 = st.columns((0.2,1,0.3))
      with col1:
        with st.expander("Fonte:"):
        st.write("IBGE, [2010].")
      with col2:
        st.slider('Slide me', min_value=0, max_value=10)
        st.select_slider('Slide to select', options=[1,'2'])
        st.text_input('Enter some text')
        st.number_input('Enter a number')
        st.text_area('Area for textual entry')
      with col3:
        st.date_input('Date input')
        st.time_input('Time entry')
        st.file_uploader('File uploader')
        st.color_picker('Pick a color')
