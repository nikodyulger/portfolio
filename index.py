import streamlit as st
from PIL import Image


st.title("Portfolio")

_, col2, _ = st.columns([2,3,1])

image = Image.open("static/profile.png")
new_size = (int(image.width/10), int(image.height/10))
resized_image = image.resize(new_size)
with col2:
    st.image(resized_image)
    st.markdown("#### Ingeniero Informático")

st.header("Sobre mí", divider="green")

st.text("Ingeniero informático especializado en Ingeniería y Ciencia de Datos en la Nube")
st.text("Me interesa saber como funcionan las cosas")
st.text("Aprendo rápido")
st.text("Tengo otros hobbies como leer, dibujar y correr")


st.header("Experiencia", divider="blue")

col1, _, col3 = st.columns([3,1,1])
with col1:
    st.subheader(":violet[Openbank] | Banco Digital")
with col3:
    st.write("")
    st.markdown("###### Septiembre 2022 - Agosto 2024")

col1, _, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### Arquitecto AWS")
with col3:
    st.markdown("###### Madrid")

st.write("""
- Mantenimiento y mejora de un sistema serverless para la transmisión de ficheros con S3, EFS y SFTP
- Coordinar y dar soporte a diferentes equipos para cumplir sus integraciones de ficheros con terceros
- Planear y desplegar infraestructura como código
- Creación de métricas para monitorizar el sistema y resolución de incidencias
 """)
st.divider()

col1, _, col3 = st.columns([3,1,1])
with col1:
    st.subheader(":orange[Integra] | Consultoría RRHH")

with col3:
    st.write("")
    st.markdown("###### Enero 2021 - Octubre 2021")

st.write("""
- Desarrollo de funcionalidades personalizadas en SAP
- Creación de servicios de datos y aplicaciones web
- Soporte y mantenimiento de incidencias
""")
st.divider()

col1, _, col3 = st.columns([3,1,1])
with col1:
    st.subheader(":red[UCLM] | Universidad")

with col3:
    st.write("")
    st.markdown("###### Enero 2021 - Octubre 2021")

st.write("""
- Desarrollo y despliegue en AWS de una aplicación web para comparar precios de productos de supermercado
- Automatización de data pipelines para web scraping
- Entrenamiento de redes neuronales profundas para la clasificación de imágenes de monumentos
- Exploración, limpieza y visualización de grandes volúmenes de datos
""")
st.divider()

st.header("Conocimientos", divider="orange")