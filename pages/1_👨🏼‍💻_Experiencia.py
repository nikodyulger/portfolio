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
            - Gestión y optimización de una arquitectura **serverless** para la transferencia de archivos entre aplicativos, utilizando S3, EFS y SFTP.
            - Actuar como enlace entre equipos para garantizar la correcta transferencia de archivos
            - Diseño e implementación de infraestructura en la nube para la orquestación entre componentes de diferentes sistemas
            - Identificación y resolución proactiva de problemas técnicos
        """
    },
    "HRPath": {
        "company": ":blue[Integra] | Consultoría RRHH",
        "dates": "###### Enero 2021 - Octubre 2021",
        "position": "###### Consultor Técnico Junior",
        "location": "###### Albacete",
        "description": """
            - Implementación de funcionalidades a medida en SAP HCM: nóminas, IRPF, correos, etc.
            - Diseño de APIs REST/OData para la integración con otros sistemas
            - Creación de aplicaciones web para gestión interna de los datos
            - Soporte y mantenimiento de incidencias
        """
    },
    "UCLM": {
        "company": ":red[UCLM] | Universidad",
        "dates": "###### Noviembre 2020 - Julio 2021",
        "position": "###### Becario de Investigación",
        "location": "###### Albacete",
        "description": """
            - Diseño, desarrollo y despliegue de aplicaciones web con AWS
            - Construcción de pipelines automatizados para extraer, transformar y cargar datos de sitios web
            - Entrenamiento de redes neuronales profundas para la clasificación de imágenes de puntos turísticos
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