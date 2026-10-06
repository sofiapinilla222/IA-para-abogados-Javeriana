import os
import streamlit as st
import requests

# Configuración de página
st.set_page_config(
    page_title="ReclamaIA — Asistente de Protección al Consumidor",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Advertencia obligatoria (Parte 6 del proyecto)
ADVERTENCIA_LEGAL = "⚠️ Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado."

# Rutas del corpus
CORPUS_DIR = os.path.join(os.path.dirname(__file__), "corpus")

def cargar_corpus():
    """Lee todos los archivos markdown del directorio corpus/ para alimentar el RAG."""
    documentos = {}
    if os.path.exists(CORPUS_DIR):
        for nombre_archivo in os.listdir(CORPUS_DIR):
            if nombre_archivo.endswith(".md") and nombre_archivo != "README.md":
                ruta = os.path.join(CORPUS_DIR, nombre_archivo)
                try:
                    with open(ruta, "r", encoding="utf-8") as f:
                        documentos[nombre_archivo] = f.read()
                except Exception as e:
                    st.sidebar.error(f"Error al leer {nombre_archivo}: {e}")
    return documentos

def buscar_contexto_relevante(consulta, documentos):
    """
    Recuperador RAG: selecciona los fragmentos del corpus normativo
    más relevantes según las palabras clave jurídicas de la consulta.
    """
    consulta_lower = consulta.lower()
    fragmentos = []

    # Identificar temas clave
    es_retracto = any(palabra in consulta_lower for palabra in ["retracto", "internet", "web", "online", "distancia", "arrepentimiento", "devuelv", "cambio de opinión"])
    es_garantia = any(palabra in consulta_lower for palabra in ["garantía", "garantia", "falla", "daño", "despegó", "rompió", "descuento", "promoción", "defecto", "calidad", "reparación", "arreglo"])
    es_sic = any(palabra in consulta_lower for palabra in ["sic", "superintendencia", "no responde", "silencio", "15 días", "demanda", "queja"])

    texto_ley = documentos.get("ley_1480_de_2011_consumidor.md", "")
    texto_sic = documentos.get("guias_sic_proteccion_consumidor.md", "")

    if es_retracto or not (es_garantia or es_sic):
        # Extraer sección de retracto
        if "### Artículo 47. Derecho de retracto" in texto_ley:
            inicio = texto_ley.find("### Artículo 47. Derecho de retracto")
            fin = texto_ley.find("### Artículo 51. Reversión del pago", inicio)
            fragmentos.append(texto_ley[inicio:fin if fin != -1 else inicio + 2500])

    if es_garantia or not (es_retracto or es_sic):
        # Extraer artículos clave de garantía
        if "## TÍTULO II: DE LA CALIDAD, IDONEIDAD Y GARANTÍA LEGAL" in texto_ley:
            inicio = texto_ley.find("## TÍTULO II: DE LA CALIDAD, IDONEIDAD Y GARANTÍA LEGAL")
            fin = texto_ley.find("## TÍTULO VII: DE LA PROTECCIÓN CONTRACTUAL", inicio)
            fragmentos.append(texto_ley[inicio:fin if fin != -1 else inicio + 3000])

    if es_sic or True:
        # Extraer artículo 58 y guías SIC
        if "### Artículo 58. Procedimiento ante la Superintendencia" in texto_ley:
            inicio = texto_ley.find("### Artículo 58. Procedimiento ante la Superintendencia")
            fragmentos.append(texto_ley[inicio:])
        if texto_sic:
            fragmentos.append(texto_sic[:2500])

    return "\n\n---\n\n".join(fragmentos)

def consultar_modelo(prompt_sistema, consulta_usuario, api_key, modelo):
    """Realiza la llamada a OpenRouter API con el prompt del sistema y el contexto RAG."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://javeriana.edu.co",
        "X-Title": "ReclamaIA Javeriana"
    }
    
    payload = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": consulta_usuario}
        ],
        "temperature": 0.2
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=60
    )
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        error_msg = response.text
        try:
            error_json = response.json()
            if "error" in error_json and "message" in error_json["error"]:
                error_msg = error_json["error"]["message"]
        except Exception:
            pass
        raise Exception(f"Error {response.status_code} de OpenRouter: {error_msg}")

# --- INTERFAZ DE USUARIO ---

# Banner de advertencia obligatoria arriba
st.warning(ADVERTENCIA_LEGAL)

# Título y encabezado
col1, col2 = st.columns([1, 6])
with col1:
    st.title("🛡️")
with col2:
    st.title("ReclamaIA")
    st.caption("**Entiende tus derechos. Reclama con respaldo.** · Pontificia Universidad Javeriana")

st.markdown("""
Bienvenido/a a **ReclamaIA**, el asistente jurídico para consumidores colombianos.  
Describe tu caso en tus propias palabras y la herramienta identificará si te aplica la **Garantía Legal** o el **Derecho de Retracto**, citará las normas de la **Ley 1480 de 2011** y te generará un **borrador formal de reclamación directa**.
""")

# Barra lateral
with st.sidebar:
    st.header("⚙️ Configuración del Modelo")
    
    # Obtener API key de variables de entorno o input del usuario
    env_api_key = os.getenv("OPENROUTER_API_KEY", "")
    api_key = st.text_input(
        "OpenRouter API Key:",
        value=env_api_key,
        type="password",
        help="Obtén tu clave gratuita en https://openrouter.ai/keys"
    )
    
    modelo = st.selectbox(
        "Modelo (OpenRouter Free):",
        options=[
            "meta-llama/llama-3.3-70b-instruct:free",
            "google/gemini-2.0-flash-exp:free",
            "mistralai/mistral-small-3.1-24b-instruct:free"
        ],
        index=0
    )
    
    st.divider()
    st.header("📚 Corpus Jurídico Conectado")
    documentos = cargar_corpus()
    st.success(f"✅ {len(documentos)} documentos normativos cargados en `/corpus`")
    for doc in documentos.keys():
        st.markdown(f"- 📄 `{doc}`")
        
    st.divider()
    st.markdown("**Proyecto Final:** Derecho e Inteligencia Artificial")
    st.markdown("**Estudiante:** Sofia Catalina Pinilla Barrios")
    st.markdown("**Docente:** Pedro Ardila")

# Formulario de consulta
with st.container():
    st.subheader("📝 Cuéntanos tu caso")
    
    tipo_compra = st.radio(
        "¿Cómo realizaste la compra?",
        ["Internet / Página web / WhatsApp (Venta a distancia)", "Tienda física (Presencial)"],
        horizontal=True
    )
    
    col_dias, col_motivo = st.columns([1, 2])
    with col_dias:
        dias = st.number_input("¿Hace cuántos días recibiste el producto?", min_value=1, max_value=365, value=3)
    with col_motivo:
        motivo = st.selectbox(
            "¿Cuál es el motivo principal de tu reclamo?",
            [
                "El producto tiene una falla, defecto o no funciona bien",
                "Quiero devolverlo porque no me gustó, no me cupo o me arrepentí",
                "El comercio no me ha respondido mi reclamo y ya pasaron más de 15 días"
            ]
        )
    
    detalles = st.text_area(
        "Describe en detalle qué compraste, a qué empresa y qué te dijeron:",
        placeholder="Ejemplo: Compré hace 3 días un televisor por la página web de una tienda, pero al llegar a mi casa me di cuenta de que no cupo en mi mueble. Está nuevo en su caja original y en la tienda me dicen que como funciona bien no me devuelven mi dinero...",
        height=120
    )

    btn_analizar = st.button("⚖️ Analizar mi caso y generar reclamación", type="primary", use_container_width=True)

# Procesamiento de la consulta
if btn_analizar:
    if not detalles.strip():
        st.error("Por favor describe los detalles de tu caso para poder orientarte.")
    elif not api_key:
        st.warning("⚠️ Ingresa tu API Key de OpenRouter en la barra lateral izquierda para realizar la consulta en vivo. Puedes obtener una gratuita en [openrouter.ai](https://openrouter.ai).")
    else:
        with st.spinner("Consultando el corpus normativo de la Ley 1480 de 2011 y las guías de la SIC..."):
            try:
                # 1. Recuperar contexto del corpus (RAG)
                consulta_completa = f"Modalidad de compra: {tipo_compra}. Días transcurridos: {dias}. Motivo: {motivo}. Hechos: {detalles}"
                contexto_normativo = buscar_contexto_relevante(consulta_completa, documentos)
                
                # 2. Construir Prompt del Sistema con RAG inyectado
                prompt_sistema = f"""Eres ReclamaIA, un asistente jurídico académico de protección al consumidor en Colombia.

REGLA OBLIGATORIA #1: Al inicio y al final de tu respuesta debes incluir:
"{ADVERTENCIA_LEGAL}"

REGLA OBLIGATORIA #2: No uses datos personales reales. Usa marcadores [Nombre del Consumidor], [Cédula], [Nombre del Proveedor].

REGLA OBLIGATORIA #3: Debes fundamentarte EXCLUSIVAMENTE en el siguiente CORPUS NORMATIVO RECUPERADO. Cita siempre el artículo específico de la Ley 1480 de 2011 o la guía de la SIC. Si no está en el corpus, di que no tienes información suficiente.

CORPUS NORMATIVO RECUPERADO (RAG):
{contexto_normativo}

MISIÓN:
1. Explica si aplica Garantía Legal (Arts. 7, 8, 11) o Derecho de Retracto (Art. 47) o si opera alguna excepción o trámite ante la SIC (Art. 58 num. 5).
2. Cita textualmente la norma y explica los plazos exactos.
3. Genera un borrador formal de Reclamación Directa completo para radicar ante el proveedor.
4. Explica la ruta ante la SIC si no responden en 15 días hábiles.
"""

                # 3. Invocar modelo
                respuesta = consultar_modelo(prompt_sistema, consulta_completa, api_key, modelo)
                
                # 4. Mostrar resultado
                st.success("✅ Análisis jurídico completado con éxito con base en el corpus normativo.")
                st.markdown(respuesta)
                
                # Botón para descargar el borrador
                st.download_button(
                    label="📥 Descargar borrador de reclamación (.txt)",
                    data=respuesta,
                    file_name="reclamacion_directa_reclamaia.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Ocurrió un error al procesar la solicitud: {str(e)}")

# Pie de página
st.divider()
st.caption(f"{ADVERTENCIA_LEGAL} · Desarrollado con Vibe Coding por Sofia Catalina Pinilla Barrios")
