import streamlit as st

st.title("Subir Documento")
st.write("Selecciona un archivo para subir.")

st.markdown("""
<style>
div[data-testid="stButton"] > button {
    background-color: #28a745 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 12px 32px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}
div[data-testid="stButton"] > button:hover {
    background-color: #218838 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

if "mostrar" not in st.session_state:
    st.session_state.mostrar = False

if st.button("📂 Subir documento"):
    st.session_state.mostrar = True

if st.session_state.mostrar:
    archivo = st.file_uploader("", type=["pdf", "docx", "txt", "xlsx"], label_visibility="collapsed")
    if archivo is not None:
        st.success(f"✅ Archivo cargado: **{archivo.name}**")
        st.write(f"Tipo: `{archivo.type}` | Tamaño: `{archivo.size / 1024:.1f} KB`")
