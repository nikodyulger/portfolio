import pandas as pd
import streamlit as st
from PIL import Image
# Page settings and constants
PAGE_TITLE = "Formación"
PAGE_ICON = "📚"
EDUCATION = {
    "CIDAEN": {
        "university": "UCLM",
        "dates": "2023-2024",
        "score": "9.75"
    },
    "Master en Informática": {
        "university": "UCLM",
        "dates": "2021-2022",
        "score": "9.2"
    },
    "Grado en Informática": {
        "university": "UCLM",
        "dates": "2017-2024",
        "score": "8.8"
    }
}
CERTIFICATIONS = {
    "AWS Solutions Architect Associate": "2023",
    "Srum Master": "2021",
}
LANGUAGES = {
    "Inglés🇬🇧": "C1",
    "Español🇪🇸": "Nativo",
    "Búlgaro🇧🇬": "Nativo"
}
AWS_ARCHITECT_PIC_PATH = "static/aws_solutions_architect.png"
PSM_SCRUM_PIC_PATH = "static/psm_scrum_master.png"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.divider()

df_grado = pd.read_csv('data/grado.csv')
df_master = pd.read_csv('data/master.csv')
df_cidaen = pd.read_csv('data/cidaen.csv')

aws_architect_image = Image.open(AWS_ARCHITECT_PIC_PATH)
psm_scrum_image = Image.open(PSM_SCRUM_PIC_PATH)

st.subheader("Notas medias", help="Trayectoria académica en la UCLM")
col1, col2, col3 = st.columns(3)
col1.metric("Grado Informática", round(df_grado['NOTA'].mean(),2), border=True)
col2.metric("Máster Informática", round(df_master['NOTA'].mean(),2), border=True)
col3.metric("Máster CIDAEN", round(df_cidaen['NOTA'].mean(),2), border=True)

st.subheader("Idiomas")
for l, col in zip(LANGUAGES.keys(), st.columns(3)):
    col.metric(l, LANGUAGES[l], border=True)

st.subheader("Certificaciones")
col1, col2, _ = st.columns(3)
col1.image(aws_architect_image)
col2.image(psm_scrum_image)