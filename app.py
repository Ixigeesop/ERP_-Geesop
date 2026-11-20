
import streamlit as st
import pandas as pd

# CONFIGURACIÓN GENERAL
st.set_page_config(
    page_title="GEESOP | ERP Industrial",
    page_icon="🏭",
    layout="wide"
)

# ESTILO
st.title("🏭 GEESOP")
st.subheader("Sistema Integrado de Gestión Industrial")

st.markdown("---")

# MENÚ LATERAL
st.sidebar.title("GEESOP ERP")
st.sidebar.caption("Gestión Empresarial")

modulo = st.sidebar.radio(
    "MENÚ PRINCIPAL",
    [
        "Dashboard",
        "Ventas",
        "Compras",
        "Proveedores",
        "Producción",
        "Inventarios",
        "Calidad"
    ]
)

# DASHBOARD
if modulo == "Dashboard":

    st.header("Panel de control")

    st.write(
        "Bienvenido al sistema de gestión empresarial."
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Ventas", "S/ 25,000")
    col2.metric("Producción", "1,200 und.")
    col3.metric("Inventario", "850 und.")
    col4.metric("Rechazos", "3.2 %")

    st.markdown("---")

    st.subheader("Resumen de producción")

    datos = pd.DataFrame({
        "Mes": ["Enero", "Febrero", "Marzo",
                "Abril", "Mayo", "Junio"],
        "Producción": [150, 180, 200, 170, 220, 280]
    })

    st.bar_chart(
        datos,
        x="Mes",
        y="Producción"
    )

    st.info(
        "Los datos mostrados son demostrativos. "
        "Posteriormente conectaremos los módulos "
        "con nuestra base de datos."
    )

else:
    st.header(modulo)
    st.info(
        f"El módulo de {modulo} se encuentra "
        "en desarrollo."
    )

st.sidebar.markdown("---")
st.sidebar.caption("GEESOP ERP | Versión 1.0")

