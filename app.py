import streamlit as st

st.title("Subir Documento")
st.write("Selecciona un archivo para subir.")

st.markdown("""
<style>
[data-testid="baseButton-secondary"] {
    background-color: #28a745 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}
[data-testid="baseButton-secondary"]:hover {
    background-color: #218838 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

archivo = st.file_uploader("", type=["pdf", "docx", "txt", "xlsx"], label_visibility="collapsed")

if archivo is not None:
    st.success(f"✅ Archivo cargado: **{archivo.name}**")
    st.write(f"Tipo: `{archivo.type}` | Tamaño: `{archivo.size / 1024:.1f} KB`")
