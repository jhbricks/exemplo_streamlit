import streamlit
import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import pandas as pd



PR = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson'
NTC = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson'
ren = 'https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/renda.csv'

#Layout da página
name = "Mapa da Desigualdade"
st.set_page_config(layout="wide", page_title=name)

#Opções do menu
st.sidebar.markdown('# Mapa da Desigualdade')
HOME = st.sidebar.button('Página inicial')
options = st.sidebar.selectbox("Selecione uma opção:", ("Paraná", "Núcleo Territorial Central"))
ABOUT = st.sidebar.button('Sobre')


if options == "Paraná":
  st.subheader("Mapa da Desigualdade do Paraná")
  categoria = st.sidebar.selectbox("Selecione uma categoria:", ("Contextualização", "Renda e Riqueza", "Municípios", "Categoria 4"))
  st.sidebar.markdown("**Dica:** Feche este menu para uma melhor visualização dos mapas.")
  if categoria == "Contextualização":
    cat2 = st.sidebar.selectbox("Selecione uma categoria:", ("Geral", "População", "CAT2", "Categoria 4"))
    if cat2 == "Geral":
      st.header("Como ler mapas")
      df_csv = pd.read_csv(ren)
      gdf_geojson = gpd.read_file(PR)
      merged_gdf = gdf_geojson.merge(df_csv, on="Município")
      if not isinstance(merged_gdf, gpd.GeoDataFrame):
        print("merged_gdf não é um GeoDataFrame")
        exit()
      max_value = merged_gdf["Índice de Gini da Renda Domiciliar per Capita (2010)"].max()
      min_value = merged_gdf["Índice de Gini da Renda Domiciliar per Capita (2010)"].min()
      max_municipio = merged_gdf.loc[merged_gdf["Índice de Gini da Renda Domiciliar per Capita (2010)"] == max_value, "Município"].iloc[0]
      min_municipio = merged_gdf.loc[merged_gdf["Índice de Gini da Renda Domiciliar per Capita (2010)"] == min_value, "Município"].iloc[0]
      m = leafmap.Map(center=[-24.7, -51.8],
                      zoom= 7,
                      draw_control=False,
                      measure_control=False,
                      fullscreen_control=False,
                      attribution_control=True)
      folium.Marker(
        [merged_gdf.loc[merged_gdf["Índice de Gini da Renda Domiciliar per Capita (2010)"] == max_value, "Y"].iloc[0],
         merged_gdf.loc[merged_gdf["Índice de Gini da Renda Domiciliar per Capita (2010)"] == max_value, "X"].iloc[0]],
        popup=f"Maior valor Gini: {max_value}<br>{max_municipio}",
        icon=folium.Icon(color="green", icon="arrow-up"),
      ).add_to(m)
      folium.Marker(
        [merged_gdf.loc[merged_gdf["Índice de Gini da Renda Domiciliar per Capita (2010)"] == min_value, "Y"].iloc[0],
         merged_gdf.loc[merged_gdf["Índice de Gini da Renda Domiciliar per Capita (2010)"] == min_value, "X"].iloc[0]],
        popup=f"Menor valor Gini: {min_value}<br>{min_municipio}",
        icon=folium.Icon(color="red", icon="arrow-down"),
      ).add_to(m)
      m.add_data(
        merged_gdf,
        column='Índice de Gini da Renda Domiciliar per Capita (2010)',
        scheme='FisherJenks',
        k = 3,
        cmap= 'RdPu',
        fields= ['Município','Índice de Gini da Renda Domiciliar per Capita (2010)'],
        legend_title='Índice de Gini da Renda Domiciliar per Capita (2010)',
        legend_position = "bottomright",
        layer_name = "'Índice de Gini da Renda Domiciliar per Capita (2010)",
        style={"stroke": True, "color": "#000000", "weight": 1, "fillOpacity": 1}
      )
      m.to_streamlit()
      col1, col2 = st.columns(2)
      with col1:
        arrow_icon = '\u2193'
        output_str = f"{min_municipio}"
        st.text(output_str)
        st.header(:green[colors] arrow_icon) st.subheader(output_str) 
      with col2:
        st.button('Hit me')
        
      
