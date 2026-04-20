import streamlit as st

st.title("Subir Documento")
st.write("Selecciona un archivo para subir.")

st.markdown("""
<style>
section[data-testid="stFileUploadDropzone"] button {
    background-color: #28a745 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
}
section[data-testid="stFileUploadDropzone"] button:hover {
    background-color: #218838 !important;
}
</style>
""", unsafe_allow_html=True)

archivo = st.file_uploader("", type=["pdf", "docx", "txt", "xlsx"])

if archivo is not None:
    st.success(f"Archivo subido: **{archivo.name}**")
    st.write(f"Tipo: `{archivo.type}` | Tamaño: `{archivo.size / 1024:.1f} KB`")
