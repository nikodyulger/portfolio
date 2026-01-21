import streamlit as st

# Page settings and constants
PAGE_TITLE = "Proyectos"
PAGE_ICON = "🛠️"
PROJECTS = {
    "Datos Calidad Aire Albacete": {
        "link": "https://github.com/nikodyulger/dataeng-ab-aire",
        "description": """
            Recopilación de los datos provenientes de las estaciones meteorológicas repartidas por la ciudad de Albacete. Todo se orquesta a través de Airflow. La intención es publicar los datos y documentar todo el proceso de desarrollo
        """,
        "tags": [
            "Airflow",
            "Polars",
            "playwright",
            "Medallion",
            "Dremio",
            "Medium",
        ],
        "img": "static/dataeng_ab_aire.png",
    },
    "Notebooks": {
        "link": "https://github.com/nikodyulger/kaggle_notebooks",
        "description": """
            Recopilación de notebooks de ciencia de datos sobre diferentes temas:
             - Extracción de datos de APIs públicas sobre los precios de las gasolineras de Albacete y su análisis
             - Redes neuronales para clasificar imágenes de mariposas
             - Modelos de clasificación y regresión
        """,
        "tags": [
            "Pandas",
            "Sci-kit Learn",
            "Machine Learning",
            "Neural Networks",
            "EDA",
            "Kaggle",
        ],
        "img": "static/kaggle_notebooks.png",
    },
    "Blog Recetas": {
        "link": "https://github.com/nikodyulger/blog-recetas",
        "description": """
            Breve recopilatorio de recetas desplegado en AWS como página web estática que se actualiza con cada push de código
        """,
        "tags": [
            "GitHub Actions",
            "Hugo",
            "Terraform",
            "Cloudfront",
            "S3",
            "Lambda@Edge",
            "Route 53",
        ],
        "img": "static/blog-recetas.png",
    },
    "Frigorífico AWS": {
        "link": "https://github.com/nikodyulger/aws-fridge-app",
        "description": """
            Aplicación para ilustrar cómo desplegar una aplicación web con un pipeline de CI/CD, manejar los costes
            apagando y levantando los contenedores, todo ello utilizando herramientas de infraestructura como código
        """,
        "tags": [
            "Cloudformation",
            "Lambda",
            "CodePipeline",
            "AppRunner",
            "SNS",
            "DynamoDB",
            "Route53",
            "Flask",
            "Pytest",
            "Docker",
        ],
        "img": "static/aws-fridge-app.gif",
    },
    "Datathon Logic": {
        "link": "https://github.com/nikodyulger/datathon-logic",
        "description": """
            Proyecto de visualización de datos, nuestra propuesta para el reto del Datathon Cajamar UniversityHack 2022
        """,
        "tags": ["Plotly", "Pandas", "Dash", "Spacy"],
        "img": "static/datathon.gif",
    },
    "Interprice": {
        "link": "https://github.com/nikodyulger/interprice",
        "description": """
            Comparador de precios de productos alimenticios de diferentes supermercados de España
        """,
        "tags": ["Scrapy", "VueJs", "Lambda", "Aurora MySQL", "API Gateway", "S3"],
        "img": "static/interprice.gif",
    },
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.divider()


for pr in PROJECTS.keys():
    col1, col2 = st.columns([5, 1])
    with col1:
        st.subheader(pr)
    with col2:
        st.link_button(label="Código", icon="🔗", url=PROJECTS[pr]["link"])

    st.pills("Tecnologías", PROJECTS[pr]["tags"])
    st.write(PROJECTS[pr]["description"])
    col1, _ = st.columns([5, 1])
    with col1:
        st.image(PROJECTS[pr]["img"])
    st.divider()
