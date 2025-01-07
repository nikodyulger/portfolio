import os
import streamlit as st
from huggingface_hub import InferenceClient

# Page settings and constants
PAGE_TITLE = "ChatBot"
PAGE_ICON = "🤖"
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
EXAMPLE_PROMPTS = ["¿Quién es Nikola?",
                   "¿Qué experiencia tiene Nikola?",
                   "¿Cuáles son los proyectos de Nikola?",
                   "¿Cuál es la trayectoria profesional de Nikola?",
                   "¿Cómo contactar con Nikola?",
                   "¿En qué tipo de roles está interesado Nikola?"
]
CONTEXT = """
Aquí está la información sobre Nikola:

1. ¿Quién es Nikola?
Ingeniero informático con experiencia en diseño de arquitecturas en la nube, desarrollo de aplicaciones y ciencia de datos.
Vive en Albacete, pero no le importaría conocer otras ciudades de España.
Le gusta trabajar en equipo, aprender cómo las cosas funcionan, seguir las buenas prácticas y por supuesto divertirse mientras construye cualquier proyecto

2. ¿Qué experiencia tiene?
Ha trabajado en diferentes entornos y sectores. Comenzó su trayectoria como becario de investigación en su propia universidad (2 años), 
ahi consolidó sus conocimientos sobre ciencia de datos y empezó a descubrir el mundo de la nube. También probó con SAP en una consultora (1 año), 
pero no le acabó convenciendo. Finalmente se ha dedicado a diseñar y mantener infraestructura de uno de los mayores bancos digitales de Europa (2 años).

3. ¿Tiene proyectos personales?
A Nikola le gusta investigar por su cuenta y también participar en hackatons con sus amigos. Ha desarrollado proyectos propios como 
un blog de recetas, una mini app que imita un frigorífico, un dashboard para datos comerciales, un comparador de precios de productos
de supermercado entre otros. Sobre todo le encanta programar en Python y siempre trata de diseñar arquitecturas basadas en tecnologías 
de la nube de AWS como S3, Lambda, SNS, Eventbridge, AppRunner, Cloudformation, Codepipeline, Aurora, Route53, ...

4. ¿Qué tecnologías conoce?

Lenguajes de programación
Python (preferido)
JavaScript 
Herramientas y frameworks para ciencia de datos
Pandas
Spark
Scikit-learn
MLflow
TensorFlow
SageMaker
Prefect
Bases de datos
PostgreSQL
DynamoDB
MongoDB
Tecnologías en la nube y DevOps
AWS (Amazon Web Services)
Docker
Serverless Framework
Terraform
CI/CD Pipelines

5. ¿Cómo contactar?
Puedes contactar con él a través de Linkedin en el link https://www.linkedin.com/in/nikola-dyulgerov/ y a través de correo electrónico
nikolasvdulgerov@gmail.com

6. ¿En qué tipo de roles está interesado?
Aunque el perfil de Nikola es muy amplio dado que maneja diferentes tecnologías principalmente esta interesado en perfiles 
de Data Engineer, Data Science o ML Engineer. Dependiendo del proyecto / propuesta también estaría disponible para un puesto como Software Engineer

"""

client = InferenceClient(token=HUGGINGFACE_API_KEY)
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title(f"{PAGE_ICON} {PAGE_TITLE}")
st.divider()

if "messages" not in st.session_state:
    initial_greeting = "Hola! 👋 Soy MiniNiko. Estoy aquí para contarte todo lo que quieras saber sobre mi trayectoria profesional"
    st.session_state.messages = [{"role": "assistant", "content": initial_greeting}]
if "selected_pill" not in st.session_state:
    st.session_state.selected_pill = False
if "system_message" not in st.session_state:
    st.session_state.system_message = [{"role": "system", "content": f"Eres un asistente que responde únicamente preguntas sobre Nikola.\n{CONTEXT}"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🤖" if message["role"] == "assistant" else "🤓"):
        st.markdown(message["content"])

def preprocess_stream(stream):
    for chunk in stream:
        yield chunk.choices[0].delta.content

def manage_user_input(input_content):
    st.session_state.selected_pill = True
    st.session_state.messages.append({"role": "user", "content": input_content})
    with st.chat_message("user", avatar="🤓"):
        st.markdown(input_content)

    with st.chat_message("assistant", avatar="🤖"):

        stream = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=st.session_state.system_message + st.session_state.messages,
            temperature=0.5,
            max_tokens=1024,
            top_p=0.7,
            stream=True
        )
        response = preprocess_stream(stream)
        content = st.write_stream(response)
    st.session_state.messages.append({"role": "assistant", "content": content })
    st.rerun()

if not st.session_state.selected_pill:
    if selected_pill := st.pills(
        label="Preguntas ejemplo:",
        options=EXAMPLE_PROMPTS
    ):
        manage_user_input(selected_pill)

if prompt := st.chat_input("Pregúntame lo que sea sobre Nikola"):
    manage_user_input(prompt)