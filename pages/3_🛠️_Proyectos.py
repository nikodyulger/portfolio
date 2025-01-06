import streamlit as st

# Page settings and constants
PAGE_TITLE = "Proyectos"
PAGE_ICON = "🛠️"
PROJECTS = {
    "Blog Recetas": {
        "link": "https://github.com/nikodyulger/blog-recetas",
        "description": """
            Breve recopilatorio de recetas desplegado en AWS como página web estática que se actualiza con cada push de código
        """,
        "tags": ["GitHub Actions", "Hugo", "Terraform", "Cloudfront", "S3", "Lambda@Edge", "Route 53"]
    },
    "Frigorífico AWS": {
        "link": "https://github.com/nikodyulger/aws-fridge-app",
        "description": """
            Aplicación para ilustrar cómo desplegar una aplicación web con un pipeline de CI/CD, manejar los costes
            apagando y levantando los contenedores, todo ello utilizando herramientas de infraestructura como código
        """,
        "tags": ["Cloudformation", "Lambda", "CodePipeline", "AppRunner", "SNS", "DynamoDB", "Route53", "Flask", "Pytest", "Docker"],
    },
    "Datathon Logic": {
        "link": "https://github.com/nikodyulger/datathon-logic",
        "description": """
            Proyecto de visualización de datos, nuestra propuesta para el reto del Datathon Cajamar UniversityHack 2022
        """,
        "tags": ["Plotly", "Pandas", "Dash", "Spacy"]
    },
    "Interprice": {
        "link": "https://github.com/nikodyulger/interprice",
        "description": """
            Comparador de precios de productos alimenticios de diferentes supermercados de España
        """,
        "tags": ["Scrapy", "VueJs", "Lambda", "Aurora MySQL", "API Gateway", "S3"]
    },
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.divider()


for pr in PROJECTS.keys():
    col1, col2 = st.columns([5,1])
    with col1:
        st.subheader(pr)
    with col2:
        st.link_button(label="Código", icon="🔗", url=PROJECTS[pr]["link"])

    st.pills("Tecnologías", PROJECTS[pr]["tags"])
    st.write(PROJECTS[pr]["description"])
    st.divider()