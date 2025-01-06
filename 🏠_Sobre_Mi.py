import streamlit as st
from PIL import Image

# Page settings and constants
PAGE_TITLE = "Portfolio | Nikola Dyulgerov"
PAGE_ICON = ":clipboard:"
NAME = "Nikola Dyulgerov"
DESCRIPTION = """
Ingeniero informático con interés en diseño aplicaciones serverless, gestionar lagos de datos y construir modelos de aprendizaje automático
"""
SOCIAL_MEDIA_LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/nikola-dyulgerov/",
    "GitHub": "https://github.com/nikodyulger",
    "Kaggle": "https://www.kaggle.com/nikoladyulgerov"
}

SOCIAL_MEDIA_ICONS = {
    "LinkedIn": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="40" height="40"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d="M100.3 448H7.4V148.9h92.9zM53.8 108.1C24.1 108.1 0 83.5 0 53.8a53.8 53.8 0 0 1 107.6 0c0 29.7-24.1 54.3-53.8 54.3zM447.9 448h-92.7V302.4c0-34.7-.7-79.2-48.3-79.2-48.3 0-55.7 37.7-55.7 76.7V448h-92.8V148.9h89.1v40.8h1.3c12.4-23.5 42.7-48.3 87.9-48.3 94 0 111.3 61.9 111.3 142.3V448z"/></svg>',
    "GitHub": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512" width="35" height="35"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3 .3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5 .3-6.2 2.3zm44.2-1.7c-2.9 .7-4.9 2.6-4.6 4.9 .3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8zM97.2 352.9c-1.3 1-1 3.3 .7 5.2 1.6 1.6 3.9 2.3 5.2 1 1.3-1 1-3.3-.7-5.2-1.6-1.6-3.9-2.3-5.2-1zm-10.8-8.1c-.7 1.3 .3 2.9 2.3 3.9 1.6 1 3.6 .7 4.3-.7 .7-1.3-.3-2.9-2.3-3.9-2-.6-3.6-.3-4.3 .7zm32.4 35.6c-1.6 1.3-1 4.3 1.3 6.2 2.3 2.3 5.2 2.6 6.5 1 1.3-1.3 .7-4.3-1.3-6.2-2.2-2.3-5.2-2.6-6.5-1zm-11.4-14.7c-1.6 1-1.6 3.6 0 5.9 1.6 2.3 4.3 3.3 5.6 2.3 1.6-1.3 1.6-3.9 0-6.2-1.4-2.3-4-3.3-5.6-2z"/></svg>',
    "Kaggle": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" width="30" height="33"><!--!Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2025 Fonticons, Inc.--><path d="M304.2 501.5L158.4 320.3 298.2 185c2.6-2.7 1.7-10.5-5.3-10.5h-69.2c-3.5 0-7 1.8-10.5 5.3L80.9 313.5V7.5q0-7.5-7.5-7.5H21.5Q14 0 14 7.5v497q0 7.5 7.5 7.5h51.9q7.5 0 7.5-7.5v-109l30.8-29.3 110.5 140.6c3 3.5 6.5 5.3 10.5 5.3h66.9q5.3 0 6-3z"/></svg>',
}
SKILLS = {
    "Python": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg",
    "Javascript": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg",
    "Git": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg",
    "Pandas": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg",
    "ApacheSpark": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/apachespark/apachespark-original.svg",
    "ScikitLearn": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg",
    "Jupyter": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg",
    "Tensorflow": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg",
    "ApacheAirflow": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/apacheairflow/apacheairflow-original.svg",
    "VueJs": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vuejs/vuejs-original.svg",
    "Postgres": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg",
    "MongoDB": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg",
    "AWS": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/amazonwebservices/amazonwebservices-original-wordmark.svg",
    "Docker": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg",
    "CI/CD": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/githubactions/githubactions-original.svg",
    "Terraform": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/terraform/terraform-original.svg",
}
PDF_PATH = "static/cv.pdf"
PROFILE_PIC_PATH = "static/profile.png"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load cv pdf and profile pic
with open(PDF_PATH, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()
profile_pic = Image.open(PROFILE_PIC_PATH)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(PROFILE_PIC_PATH)

with col2:
    st.markdown(f"## {NAME}")
    st.write(DESCRIPTION)
    st.write("")
    st.download_button(
        label="Descargar CV",
        data=pdf_bytes,
        icon="💾",
        mime="application/octet-stream",
        file_name="cv-nikola.pdf",
        type="primary"
    )
    st.write("")
    html = f"""<div style="display: flex; align-items: center; justify-content: left; gap: 15px;">"""
    for snet in SOCIAL_MEDIA_LINKS.keys():
        html += f"""<a href="{SOCIAL_MEDIA_LINKS[snet]}" target="_blank">{SOCIAL_MEDIA_ICONS[snet]}</a>"""
    html += """</div>"""
    st.markdown(html, unsafe_allow_html=True)

st.header("Sobre mí", divider="blue")

st.markdown(":cloud: Especializado en arquitectura de datos en la nube")
st.markdown(":bulb: Me gusta entender las cosas para poder encontran una mejor solución")
st.markdown(":arrows_counterclockwise: Me adapto fácilmente a nuevos entornos y tecnologías")
st.markdown(":running: Fuera del ámbito profesional, tengo otros hobbies como: leer, dibujar y correr")

st.header("Tecnologías")

skill_markdown_content = ""
icons_per_row = 4
current_row = []
for idx, (skill, icon_url) in enumerate(SKILLS.items(), start=1):
    current_row.append(f'<div style="text-align: center; margin: 10px;">'
                       f'<img src="{icon_url}" width="50"><br>{skill}</div>')
    if idx % icons_per_row == 0 or idx == len(SKILLS):
        skill_markdown_content += f'<div style="display: flex; justify-content: space-between;">' + "".join(current_row) + "</div><br>"
        current_row = []

st.markdown(skill_markdown_content, unsafe_allow_html=True)