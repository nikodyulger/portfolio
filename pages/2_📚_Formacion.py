import pandas as pd
import streamlit as st

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

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.divider()

df_grado = pd.read_csv('data/grado.csv')
df_master = pd.read_csv('data/master.csv')
df_cidaen = pd.read_csv('data/cidaen.csv')

st.subheader("Grado en Informática")
st.write(df_grado)

