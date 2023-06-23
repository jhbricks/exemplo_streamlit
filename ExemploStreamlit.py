import streamlit
import streamlit as st

#Layout da página
name = "Mapa da Desigualdade"
st.set_page_config(layout="wide", page_title=name)

#Opções do menu
st.sidebar.markdown('# Mapa da Desigualdade')
options = st.sidebar.selectbox("Selecione uma opção:", ("Paraná", "Núcleo Territorial Central"))

st.title("Mapa da Desigualdade: Contextualização")
st.title("População")

#-----------------Parte do mapa

#Arquivos
PR = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson'
NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
contx = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/contexto.csv'
pop = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/pop_2021.csv'

#Unir csv com geojson
import pandas as pd
import geopandas as gpd

geojson_pr = gpd.read_file(PR)

csv_pop = pd.read_csv(pop)
pr_pop = geojson_pr.merge(csv_pop, on="Município")
csv_contx = pd.read_csv(contx)
pr_contx = geojson_pr.merge(csv_contx, on="Município")

#Mapa da População
import leafmap
# Configura o mapa geral
m = leafmap.Map(center=[-51.8, -24.7],
                zoom= 11,
                draw_control=False,
                measure_control=False,
                fullscreen_control=False,
                attribution_control=True
                               )
m.add_data(
    pr_pop,
    column='População',
    scheme='FisherJenks',
    k = 7,
    cmap= 'YlGnBu',
    fields= ['Município','População'],
    legend_title='População total',
    legend_position = "bottomright",
    style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1}
)
m
col1, col2 = st.columns(2)
with col1:
  st.header('Maior e Menor Valor')
  import pandas as pd
  maior_populacao = dataframe['População'].max()
  menor_populacao = dataframe['População'].min()
  municipio_maior_populacao = dataframe.loc[dataframe['População'] == maior_populacao, 'Municípios'].iloc[0]
  municipio_menor_populacao = dataframe.loc[dataframe['População'] == menor_populacao, 'Municípios'].iloc[0]
  print(f"Maior: ({municipio_maior_populacao}) com {maior_populacao} habitantes")
  print(f"Menor população: {menor_populacao} ({municipio_menor_populacao})")
with col2:
  st.header('Observações:')
  st.subheader('ANO BASE: 2021')
  st.subheader('FÓRMULA: População total do município')
  st.subheader('FONTE: IBGE, 2021')
  st.subheader('OBSERVAÇÕES: População total de acordo com o censo do IBGE de 2021')
            
        






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
