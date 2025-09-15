import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

# =============================
# Estilos personalizados y CSS
# =============================
st.markdown(
    """
    <style>
        /* Fondo degradado y tipografía moderna */
        body {
            background: linear-gradient(135deg, #1c1c1c, #3a3a3a);
            font-family: 'Arial', sans-serif;
        }
        .main { 
            background-color: transparent; 
            color: #FFFFFF; 
        }
        /* Botones estilizados */
        .stButton>button, .stDownloadButton>button {
            color: #FFFFFF; 
            background-color: #0055a2; 
            border-radius: 8px; 
            padding: 12px 24px;
            transition: all 0.3s ease; 
            font-weight: bold; 
            border: none;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .stButton>button:hover, .stDownloadButton>button:hover {
            background-color: #003366; 
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.5);
        }
        /* Encabezados de sección con animación */
        .section-header {
            font-size: 36px; 
            font-weight: bold; 
            color: #00aaff; 
            margin-top: 20px;
            animation: slideIn 1s ease-out;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        @keyframes slideIn {
            from { transform: translateX(-50px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        /* Imagen de la barra lateral */
        .sidebar-image {
            border-radius: 50%; 
            width: 180px; 
            height: 180px; 
            display: block; 
            margin: 0 auto 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
        }
        .sidebar-image:hover {
            transform: scale(1.1);
        }
        /* Estilos para "cards" en secciones */
        .card {
            background-color: #2c2c2c; 
            padding: 20px; 
            border-radius: 10px; 
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .card h3 {
            margin-top: 0;
            color: #00aaff;
        }
        .card a {
            color: #00aaff;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True
)

st.set_page_config(page_title='Portafolio-SandroLescieur')

# =============================
# Barra lateral: Información y CV
# =============================
st.sidebar.title("Sandro Lescieur López")
st.sidebar.image("files/foto.jpeg", width=220, caption="Data Scientist | Matemático")
st.sidebar.markdown("**📍 Ubicación:** CDMX")
st.sidebar.markdown("**📞 Teléfono:** 553-516-3043")
st.sidebar.markdown("**📧 Correo:** sandrolescieurlopez@gmail.com")

# Rutas de archivos de CV
cv_es_path = "files/CV-SandroLescieurLopez.pdf"
cv_en_path = "files/CV-SandroLescieurLopez-EN.pdf"

# Función para descargar CVs
def crear_boton_descarga(file_path, label, file_name, unique_key):
    if Path(file_path).is_file():
        with open(file_path, "rb") as file_data:
            st.sidebar.download_button(
                label=label,
                data=file_data,
                file_name=file_name,
                mime="application/pdf",
                key=unique_key,
            )

crear_boton_descarga(cv_es_path, "📄 Descargar CV en Español", "CV-SandroLescieurLopez.pdf", unique_key="boton_es_cv")
crear_boton_descarga(cv_en_path, "📄 Download CV in English", "CV-SandroLescieurLopez-EN.pdf", unique_key="boton_en_cv")

# =============================
# Navegación: Pestañas
# =============================
tabs = st.tabs(["Inicio", "Experiencia", "Educación", "Cursos y certificaciones", "Habilidades"])

# =============================
# Página de Inicio
# =============================
with tabs[0]:
    st.title("Sandro Lescieur López")
    st.markdown("## Data Scientist | Data Analyst")
    st.write(
            "¡Bienvenido a mi portafolio!"
        )
    st.write(
            "Apasionado por la ciencia de datos, con una sólida formación en matemáticas y un enfoque orientado a transformar datos en estrategias y soluciones que impulsen el crecimiento y la innovación.", 
            "He trabajado en diversos proyectos en los que he aplicado y fortalecido mis conocimientos en análisis y ciencia de datos."
        )
    st.write(
            "Te invito a explorar mi portafolio para conocer más sobre mi trayectoria académica y profesional."
        )

# =============================
# Experiencia Profesional
# =============================
with tabs[1]:
    st.markdown("<div class='section-header'>Experiencia Profesional</div>", unsafe_allow_html=True)
    experiences = [
        {
            "role": "CIentífico de datos",
            "company": "Instituto de Ciencias de la Atmósfera y Cambio Climático (UNAM)",
            "description": "Desarrollo de tesis sobre modelado de la calidad del aire de la Zona Metropolitana del Valle de México (ZMVM) mediante técnicas de Machine Learning. Se realizó el análisis de datos end-to-end con el objetivo de aplicar el modelo XGBoost para reducir el sesgo de los modelos numéricos en producción."
        },
        {
            "role": "Ingeniero de datos",
            "company": "Badak (Consultoría de Software)",
            "description": "Automaticé procesos de ingesta y transformación de datos desde múltiples fuentes hacia Google Cloud Platform, garantizando su disponibilidad, accesibilidad y seguridad. Utilicé herramientas y tecnologías como Python para el desarrollo de scripts, BigQuery para análisis de datos a gran escala y SQL para consultas y manipulación de datos."
        },
        {
            "role": "Ayudante de profesor",
            "company": "Facultad de Ciencias (UNAM)",
            "description": "Presenté explicaciones frente a grupo de los códigos realizados en la asignatura Solución Numérica de Ecuaciones Diferenciales Ordinarias, facilitando la comprensión de los conceptos teóricos mediante ejemplos prácticos en Python."
        },
        {
            "role": "Asistente de Cómputo científico",
            "company": "Instituto de Ciencias Físicas (UNAM)",
            "description": "Durante mi servicio social en el programa Simulaciones Numéricas de Ecuaciones Diferenciales Ordinarias, analicé y revisé el código fuente así como la documentación de las librerías taylormodels.jl e intervalarithmetic.jl, enfocadas en el análisis riguroso de soluciones de ecuaciones diferenciales ordinarias. Propuse e implementé mejoras en la funcionalidad y documentación de ambas paqueterías para facilitar su uso."
        }
    ]
    for exp in experiences:
        st.markdown(
            f"<div class='card'><h3>{exp['role']} - {exp['company']}</h3><p>{exp['description']}</p></div>",
            unsafe_allow_html=True
        )

# =============================
# Educación
# =============================
with tabs[2]:
    st.markdown("<div class='section-header'>Educación</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'><h3>Diplomado en Ciencia de Datos</h3>"
        "<p>Universidad Nacional Autónoma de México (UNAM) (2023 - 2024)</p>"
        "<p>Complementé mi formación con este diplomado, en el que se trataron temas como modelación supervisada, modelación no supervizada y big data, aplicados a problemas reales de negocio.</p>"
        "<p>Herramientas y tecnologías utilizadas: Python, SQL, PySpark, Linux, Google Cloud Platform, Scikit-learn, TensorFlow.</p></div>",
        unsafe_allow_html=True
    )

with tabs[2]:
    st.markdown(
        "<div class='card'><h3>Licenciatura en Matemáticas</h3>"
        "<p>Universidad Nacional Autónoma de México (UNAM) (2017 - 2022)</p>"
        "<p>Formación integral en probabilidad y estadística, complementando con cursos avanzados en programación, análisis de datos e inteligencia artificial. </p></div>",
        unsafe_allow_html=True
    )

# =============================
#  Cursos y Certificaciones
# =============================
with tabs[3]:
    st.markdown("<div class='section-header'>Cursos Destacados</div>", unsafe_allow_html=True)
    cursos = [
        "Optimización de hiperparámetros y ensamble de modelos de machine learning - 1er Congreso Internacional de Inteligencia Artificial 2025",
        "Big Data y Spark: ingeniería de datos con Python y Pyspark - Udemy",
        "Curso Maestro: Visualizaciones y Análisis de Datos en Python - Udemy",
        "GCP - Google Cloud Professional Data Engineer Certification - Udemy",
        "Linux Administration: The Complete Linux Bootcamp - Udemy",
        "SQL - Curso completo de Bases de Datos - de 0 a Avanzado - Udemy",
        "GitHub Universe 2023 Cloud Skills Challenge - Microsoft",
        "Introducción a la ciencia de datos utilizando Python - DGTIC, UNAM",
        "Análisis de datos con Python y Pandas - Unidad de Cómputo, Facultad de Ingeniería, UNAM",
    ]
    for cert in cursos:
        st.markdown(f"<div class='card'><p>{cert}</p></div>", unsafe_allow_html=True)
    
    drive_url = "https://drive.google.com/drive/folders/1k6UIGmPaXocN6PvBtU7IQKw9Sqb70rmq?usp=sharing"
    st.markdown(
        f"<div class='card'><p><a href='{drive_url}' target='_blank' style='color:#00aaff; font-weight:bold;'>Ver más cursos y certificaciones</a></p></div>",
        unsafe_allow_html=True
    )

# =============================
# Habilidades Técnicas
# =============================
with tabs[4]:
    st.markdown("<div class='section-header'>Habilidades Técnicas</div>", unsafe_allow_html=True)

    skills = """
- **Lenguajes:** Python, R  
- **Frameworks y bibliotecas:** Numpy, Pandas, TensorFlow, PyTorch, Scikit-Learn, PySpark  
- **Bases de datos:** SQL  
- **Visualización:** Power BI, Tableau, Matplotlib, Pandas, Seaborn, Plotly
- **Cloud y DevOps:** Linux, Google Cloud Platform, Git, Docker  
    """
    st.markdown(skills)
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# Habilidades Blandas
# =============================
with tabs[4]:
    st.markdown("<div class='section-header'>Habilidades Blandas</div>", unsafe_allow_html=True)
    skills = """
- **Gestión del tiempo**  
- **Gestión de proyectos**  
- **Atención a los detalles**
- **Trabajo en equipo**
- **Proactividad**
- **Inteligencia emocional**
- **Comunicación asertiva**
- **Adaptabilidad**
    """
    st.markdown(skills)
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# FIN DE LA PARTE 1
# =============================
# PARTE 2: Secciones adicionales
# =============================

tabs_extra = st.tabs(["Visualizaciones Interactivas", "Descargas de CVs y proyectos en GitHub"])

with tabs_extra[0]:
    st.markdown("<div class='section-header'>Visualizaciones Interactivas</div>", unsafe_allow_html=True)
    st.write(
        "Explora mis visualizaciones de datos que muestran mi dominio en el análisis e interpretación de información."
    )

    # Gráfico de radar para mostrar dominio de habilidades técnicas
    data = pd.DataFrame({
    "Habilidad": ["Python", "Visualización", "SQL", "Machine Learning", "Cloud"],
    "Nivel": [95, 95, 90, 85, 80]
    })
    fig_radar = px.line_polar(data, r='Nivel', theta='Habilidad', line_close=True, title='Dominio de Habilidades Técnicas', labels={"Nivel": "Porcentaje (%)"})
    # Cambiar colores de fondo y líneas
    fig_radar.update_layout(
        polar=dict(
            bgcolor="#003366",   # color fondo del radar
            radialaxis=dict(
                range=[0, 100],
                gridcolor="black",   # color líneas concéntricas
                linecolor="#fcfcfc"   # color línea radial central 
            ),
            angularaxis=dict(
                gridcolor="#6f747a",   #  color líneas angulares
            )
        ),
        paper_bgcolor="black",   # color fondo del canvas
        font=dict(color="white") # color del texto
    )
    st.plotly_chart(fig_radar)

# -----------------------------
# Descargas de CVs
# -----------------------------
with tabs_extra[1]:
    # Descargas de CVs
    st.markdown("<div class='section-header'>Descargas de CVs</div>", unsafe_allow_html=True)
    st.write(
        "Descarga mi CV en el idioma que prefieras para conocer más detalles sobre mi experiencia y formación profesional."
    )
    col1, col2 = st.columns(2)
    with col1:
        if Path(cv_es_path).is_file():
            with open(cv_es_path, "rb") as file_data:
                st.download_button(
                    label="📄 Descargar CV en Español",
                    data=file_data,
                    file_name="CV-SandroLescieurLopez.pdf",
                    mime="application/pdf",
                    key="cv_es_extra"
                )
    with col2:
        if Path(cv_en_path).is_file():
            with open(cv_en_path, "rb") as file_data:
                st.download_button(
                    label="📄 Download CV in English",
                    data=file_data,
                    file_name="CV-SandroLescieurLopez-EN.pdf",
                    mime="application/pdf",
                    key="cv_en_extra"
                )

    # Link a GitHub
    st.markdown("<div class='section-header'>Proyectos en GitHub</div>", unsafe_allow_html=True)
    st.write(
        "Explora mis proyectos en mi perfil de GitHub:"
    )
    st.markdown(f"""<a href="https://github.com/SandroLescieur" target="_blank" class="stDownloadButton">
                    <button>💻 Ir a GitHub</button></a>""", unsafe_allow_html=True)
