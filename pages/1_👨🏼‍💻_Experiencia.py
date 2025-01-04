import streamlit as st

# Page settings and constants
PAGE_TITLE = "Experiencia"
PAGE_ICON = "👨🏼‍💻"

EXPERIENCE = {
    "Openbank": {
        "company": ":rainbow[Openbank] | Banco Digital",
        "dates": "###### Septiembre 2022 - Agosto 2024",
        "position": "###### Arquitecto AWS",
        "location": "###### Madrid",
        "description": """
            - Mantenimiento y mejora de un sistema serverless para la transmisión de ficheros con S3, EFS y SFTP
            - Coordinar y dar soporte a diferentes equipos para cumplir sus integraciones de ficheros con terceros
            - Planear y desplegar infraestructura como código
            - Creación de métricas para monitorizar el sistema y resolución de incidencias
        """
    },
    "HRPath": {
        "company": ":blue[Integra] | Consultoría RRHH",
        "dates": "###### Enero 2021 - Octubre 2021",
        "position": "###### Consultor Técnico Junior",
        "location": "###### Albacete",
        "description": """
            - Desarrollo de funcionalidades personalizadas en SAP
            - Creación de servicios de datos y aplicaciones web
            - Soporte y mantenimiento de incidencias
        """
    },
    "UCLM": {
        "company": ":red[UCLM] | Universidad",
        "dates": "###### Noviembre 2020 - Julio 2021",
        "position": "###### Becario de Investigación",
        "location": "###### Albacete",
        "description": """
            - Desarrollo y despliegue en AWS de una aplicación web para comparar precios de productos de supermercado
            - Automatización de data pipelines para web scraping
            - Entrenamiento de redes neuronales profundas para la clasificación de imágenes de monumentos
            - Exploración, limpieza y visualización de grandes volúmenes de datos
        """
    }
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.divider()

for exp in EXPERIENCE.keys():
    col1, _, col3 = st.columns([3,1,1])
    with col1:
        st.subheader(EXPERIENCE[exp]["company"])
    with col3:
        st.write("")
        st.markdown(EXPERIENCE[exp]["dates"])

    col1, _, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown(EXPERIENCE[exp]["position"])
    with col3:
        st.markdown(EXPERIENCE[exp]["location"])

    st.write(EXPERIENCE[exp]["description"])
    st.divider()