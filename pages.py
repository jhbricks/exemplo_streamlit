import streamlit as st
from multiapp import MultiApp
from apps import (saude, Home, pobreza, fome, genero, agua, educacao)
from PIL import Image

# Definindo o ícone e titulo da página
#icon = Image.open("SDG Wheel_PRINT_Transparent.png")
st.set_page_config(layout='wide', page_title='Mapa da Desigualdade', page_icon=icon)

apps = MultiApp()

# Adicionando as aplicações
#apps.add_app('Página Inicial', Home.app)
#apps.add_app("1 - Erradicação da pobreza", pobreza.app)
#apps.add_app("2 - Fome Zero e Agricultura Sustentável", fome.app)
apps.add_app("3 - Saúde e Bem-Estar", saude.app)


# The main app
apps.run()
