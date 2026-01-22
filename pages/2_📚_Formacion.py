import pandas as pd
import streamlit as st
from PIL import Image

# Page settings and constants
PAGE_TITLE = "Formación"
PAGE_ICON = "📚"
EDUCATION = {
    "CIDAEN": {"university": "UCLM", "dates": "2023-2024", "score": "9.75"},
    "Master en Informática": {
        "university": "UCLM",
        "dates": "2021-2022",
        "score": "9.2",
    },
    "Grado en Informática": {
        "university": "UCLM",
        "dates": "2017-2024",
        "score": "8.8",
    },
}
LANGUAGES = {"Inglés🇬🇧": "C1", "Español🇪🇸": "Nativo", "Búlgaro🇧🇬": "Nativo"}
SNOWFLAKE_SNOWPRO_CORE = "static/snowflake_snowpro_core.png"
AWS_DATA_ENGINEER_PIC_PATH = "static/aws_data_engineer.png"
AWS_ARCHITECT_PIC_PATH = "static/aws_solutions_architect.png"
PSM_SCRUM_PIC_PATH = "static/psm_scrum_master.png"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.divider()

df_grado = pd.read_csv("data/grado.csv")
df_master = pd.read_csv("data/master.csv")
df_cidaen = pd.read_csv("data/cidaen.csv")

df_grado["Estudios"] = "Grado Informática"
df_master["Estudios"] = "Máster Informática"
df_cidaen["Estudios"] = "Máster CIDAEN"

df_all_subjects = pd.concat([df_grado, df_master, df_cidaen], ignore_index=True)

snowflake_snowpro_image = Image.open(SNOWFLAKE_SNOWPRO_CORE)
aws_data_engineer_image = Image.open(AWS_DATA_ENGINEER_PIC_PATH)
aws_architect_image = Image.open(AWS_ARCHITECT_PIC_PATH)
psm_scrum_image = Image.open(PSM_SCRUM_PIC_PATH)

st.subheader("Notas medias", help="Trayectoria académica en la UCLM")
col1, col2, col3 = st.columns(3)

col1.metric("Grado Informática", round(df_grado["NOTA"].mean(), 2), border=True)
col2.metric("Máster Informática", round(df_master["NOTA"].mean(), 2), border=True)
col3.metric(
    "Máster CIDAEN",
    round(df_cidaen["NOTA"].mean(), 2),
    help="Master Ciencia e Ingeniería de Datos en la Nube",
    border=True,
)


@st.dialog("Detalle de Trayectoria Académica", width="large")
def mostrar_detalles():
    st.write("Filtra y revisa el desglose de todas las asignaturas cursadas.")

    seleccion = st.multiselect(
        "Filtrar por estudios:",
        options=df_all_subjects["Estudios"].unique(),
        default=df_all_subjects["Estudios"].unique(),
    )

    df_filtrado = df_all_subjects[df_all_subjects["Estudios"].isin(seleccion)]

    st.dataframe(df_filtrado, use_container_width=True, hide_index=True)
    st.caption(f"Mostrando {len(df_filtrado)} asignaturas en total.")


if st.button("🔍 Ver desglose de asignaturas", use_container_width=True):
    mostrar_detalles()

st.subheader("Idiomas")
for l, col in zip(LANGUAGES.keys(), st.columns(3)):
    col.metric(l, LANGUAGES[l], border=True)

st.subheader("Certificaciones")
col1, col2, col3, col4 = st.columns(4)
col1.image(snowflake_snowpro_image)
col2.image(aws_architect_image)
col3.image(aws_data_engineer_image)
col4.image(psm_scrum_image)
