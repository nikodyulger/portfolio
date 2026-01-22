import streamlit as st

# Page settings and constants
PAGE_TITLE = "Experiencia"
PAGE_ICON = "👨🏼‍💻"

EXPERIENCE = {
    "Accenture": {
        "company": ":violet[Accenture] | IA & Big Data",
        "dates": "###### Septiembre 2026 - Actualidad",
        "position": "###### Data Engineer",
        "location": "###### Madrid (Remoto)",
        "description": """
            - Diseño e implementación de una arquitectura de datos en tiempo real orientada a la creación de un Golden Record, sincronizando bases de datos on-premise con bases de datos no relacionales mediante CDC.
            - Orquestación de procesos de carga inicial y conciliación de datos entre sistemas, asegurando la integridad y trazabilidad de la información
            - Desarrollo de herramientas de automatización operativa para la generación de configuraciones facilitando su mantenimiento y evolución.
        """,
    },
    "DIVE.Tech": {
        "company": ":red[DIVE.Tech] | Soluciones IA",
        "dates": "###### Abril 2025 - Septiembre 2025",
        "position": "###### Data Engineer",
        "location": "###### Madrid (Remoto)",
        "description": """
            - Diseño de arquitecturas de datos batch y streaming, y de modelos de datos analíticos enfocados en la optimización de costes, el rendimiento analítico y la operación del dato.
            - Implementación de un sistema de Change Data Capture (CDC) desde PostgreSQL hacia ClickHouse, utilizando Kafka, Debezium y Pandas, garantizando consistencia y baja latencia en la sincronización de datos.
            - Optimización de consultas SQL para la explotación analítica, mejorando tiempos de respuesta y eficiencia en el acceso a la información
            - Desarrollo de APIs REST, abarcando diseño de la lógica, definición de endpoints y documentación para facilitar la integración con otros sistemas
            - Colaboración técnica con el equipo en la resolución de incidencias y en la mejora continua de procesos y arquitectura
        """,
    },
    "Openbank": {
        "company": ":rainbow[Openbank] | Banco Digital",
        "dates": "###### Septiembre 2022 - Agosto 2024",
        "position": "###### Arquitecto AWS",
        "location": "###### Madrid",
        "description": """
            - Diseño y evolución de arquitecturas serverless y orientadas a eventos en la nube, destinadas a la transferencia e integración de información entre múltiples sistemas
            - Despliegue y gestión de infraestructura como código, garantizando entornos reproducibles, escalables y mantenibles
            - Implementación de mecanismos de monitorización y observabilidad, junto con la detección y resolución proactiva de incidencias, asegurando la estabilidad de los sistemas
            - Coordinación técnica entre equipos internos y terceros para la integración de sistemas, con foco en escalabilidad, resiliencia y fiabilidad operativa
        """,
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
        """,
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
        """,
    },
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.divider()

for exp in EXPERIENCE.keys():
    col1, _, col3 = st.columns([3, 1, 1])
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
