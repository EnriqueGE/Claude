import streamlit as st

st.title("Subir Documento")
st.write("Selecciona un archivo para subir.")

st.markdown("""
<style>
/* Ocultar el file_uploader original */
[data-testid="stFileUploader"] {
    display: none;
}

/* Botón verde personalizado */
.boton-verde {
    display: inline-block;
    background-color: #28a745;
    color: white !important;
    padding: 12px 28px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    border: none;
    text-align: center;
    margin: 10px 0;
}
.boton-verde:hover {
    background-color: #218838;
}
</style>

<label for="file-input" class="boton-verde">📂 Seleccionar archivo</label>
<input id="file-input" type="file" accept=".pdf,.docx,.txt,.xlsx"
    style="display:none"
    onchange="handleFile(this)">

<div id="resultado" style="margin-top:16px; font-size:15px;"></div>

<script>
function handleFile(input) {
    const file = input.files[0];
    if (file) {
        const kb = (file.size / 1024).toFixed(1);
        document.getElementById('resultado').innerHTML =
            '<div style="padding:12px;background:#d4edda;border-radius:8px;color:#155724;">'
            + '✅ <strong>Archivo cargado:</strong> ' + file.name
            + '<br>Tipo: <code>' + file.type + '</code> | Tamaño: <code>' + kb + ' KB</code>'
            + '</div>';
    }
}
</script>
""", unsafe_allow_html=True)
