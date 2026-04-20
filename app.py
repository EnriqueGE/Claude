import streamlit as st

st.title("Ejemplo de botones personalizados")

st.markdown("""
<style>
/* Botón verde */
div[data-testid="stButton"]:nth-of-type(1) button {
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 8px;
}
div[data-testid="stButton"]:nth-of-type(1) button:hover {
    background-color: #218838;
}

/* Botón azul */
div[data-testid="stButton"]:nth-of-type(2) button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
}
div[data-testid="stButton"]:nth-of-type(2) button:hover {
    background-color: #0056b3;
}

/* Botón naranja */
div[data-testid="stButton"]:nth-of-type(3) button {
    background-color: #fd7e14;
    color: white;
    border: none;
    border-radius: 8px;
}
div[data-testid="stButton"]:nth-of-type(3) button:hover {
    background-color: #e8650a;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Botón Verde"):
        st.success("¡Hiciste clic en Verde!")

with col2:
    if st.button("Botón Azul"):
        st.info("¡Hiciste clic en Azul!")

with col3:
    if st.button("Botón Naranja"):
        st.warning("¡Hiciste clic en Naranja!")
