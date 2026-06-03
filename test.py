import streamlit as st
import seaborn as sns
import plotly.express as px


# CARGA DE DATOS
# ----------------------------------------------------
df = sns.load_dataset("tips")

# Renombramos columnas para facilitar la explicación
df = df.rename(columns={
    "total_bill": "cuenta_total",
    "tip": "propina",
    "sex": "sexo",
    "smoker": "fumador",
    "day": "dia",
    "time": "momento",
    "size": "personas"
})

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------
with st.sidebar:
    st.title("Menú lateral")
    st.write("Este espacio puede usarse como panel de navegación.")
    



    variable_grafico = st.selectbox(
        "Selecciona la variable para graficar:",
        ["Ventas", "Costos", "Utilidad", "Clientes"]
    )

    mostrar_datos = st.checkbox("Mostrar tabla de datos", value=True)

    mes_seleccionado = st.selectbox(
        "Selecciona un dia:",
        df["dia"].unique()
    )
    st.write("Más adelante aquí podremos conectar estos botones para filtrar la data")

# ----------------------------------------------------
# TÍTULO PRINCIPAL
# ----------------------------------------------------
st.title("Introducción a Streamlit")
st.write(
    """
    Esta aplicación muestra cómo estructurar una interfaz básica con Streamlit.
    El objetivo es comprender cómo organizar contenido usando columnas, pestañas,
    gráficos, tablas e imágenes.
    """
)

# ----------------------------------------------------
# COLUMNAS CON INDICADORES GENERALES
# ----------------------------------------------------
st.subheader("Indicadores generales")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Cantidad de registros", len(df))

with col2:
    st.metric("Cuenta promedio", f"${df['cuenta_total'].mean():.2f}")

with col3:
    st.metric("Propina promedio", f"${df['propina'].mean():.2f}")

# ----------------------------------------------------
# PESTAÑAS PRINCIPALES
# ----------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "Presentación",
    "Datos",
    "Gráficos",
    "Imágenes"
])

# ----------------------------------------------------
# TAB 1: PRESENTACIÓN
# ----------------------------------------------------
with tab1:
    st.header("¿Qué es Streamlit?")

    st.write(
        """
        Streamlit es una librería de Python que permite crear aplicaciones web
        interactivas de manera rápida y sencilla.

        Su principal ventaja es que permite construir interfaces usando solo Python,
        sin necesidad de programar directamente en HTML, CSS o JavaScript.
        """
    )

    st.subheader("¿Qué se puede crear con Streamlit?")

    col_a, col_b = st.columns(2)

    with col_a:
        st.write("Aplicaciones posibles:")
        st.write("- Dashboards")
        st.write("- Visualizadores de datos")
        st.write("- Interfaces para modelos predictivos")
        st.write("- Reportes interactivos")
        st.write("- Prototipos de análisis")

    with col_b:
        st.write("Elementos que se pueden incluir:")
        st.write("- Textos")
        st.write("- Tablas")
        st.write("- Gráficos")
        st.write("- Imágenes")
        st.write("- Botones")
        st.write("- Formularios")
        st.write("- Filtros")

# ----------------------------------------------------
# TAB 2: DATOS
# ----------------------------------------------------
with tab2:
    st.header("Visualización de datos")

    st.write(
        """
        En esta sección mostramos el dataset `tips` de Seaborn.
        Cada fila representa una cuenta de restaurante.
        """
    )

    st.dataframe(df, use_container_width=True)

    st.subheader("Primeras filas del dataset")
    st.table(df.head())

# ----------------------------------------------------
# TAB 3: GRÁFICOS
# ----------------------------------------------------
with tab3:
    st.header("Creación de gráficos")

    st.write(
        """
        Streamlit permite insertar gráficos creados con distintas librerías de Python.
        En este ejemplo usamos Plotly para construir gráficos interactivos.
        """
    )

    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        st.subheader("Relación entre cuenta y propina")

        fig1 = px.scatter(
            df,
            x="cuenta_total",
            y="propina",
            color="dia",
            title="Cuenta total vs propina"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col_graf2:
        st.subheader("Cuenta promedio por día")

        resumen_dia = (
            df
            .groupby("dia", as_index=False, observed=True)
            .agg(cuenta_promedio=("cuenta_total", "mean"))
        )

        fig2 = px.bar(
            resumen_dia,
            x="dia",
            y="cuenta_promedio",
            title="Cuenta promedio por día"
        )

        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Distribución de propinas")

    fig3 = px.box(
        df,
        x="dia",
        y="propina",
        color="dia",
        title="Distribución de propinas por día"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ----------------------------------------------------
# TAB 4: IMÁGENES
# ----------------------------------------------------
with tab4:
    st.header("Uso de imágenes")

    st.write(
        """
        Streamlit también permite mostrar imágenes dentro de una aplicación.
        Esto puede utilizarse para incorporar logos, fotografías, diagramas,
        capturas de pantalla o resultados visuales.
        """
    )

    st.subheader("Imagen desde una URL")

    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        caption="Logo de Streamlit",
        use_container_width=True
    )

    st.subheader("Cargar una imagen desde el computador")

    imagen = st.file_uploader(
        "Sube una imagen",
        type=["png", "jpg", "jpeg"]
    )

    if imagen is not None:
        st.image(
            imagen,
            caption="Imagen cargada por el usuario",
            use_container_width=True
        )
    else:
        st.info("Cuando el usuario cargue una imagen, aparecerá en esta sección.")