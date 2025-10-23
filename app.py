import streamlit as st
from PIL import Image

# --- Título principal ---
st.title("💿 Página Oficial de Blessd")

# --- Encabezado ---
st.header("El talento urbano de Medellín 🇨🇴")
st.write("""
Blessd, también conocido como **Stiven Mesa Londoño**, es uno de los artistas más destacados del género urbano en Colombia.  
Su música combina ritmos de reggaetón, trap y flow callejero, con letras que reflejan su historia, su barrio y su visión de la vida.  
Con éxitos como *Medallo*, *Instagram Remix* y *Si Sabe*, Blessd ha logrado posicionarse como una de las nuevas voces más influyentes del movimiento latino.
""")

# --- Imagen principal ---
image = Image.open('blessd.jpg')
st.image(image, caption='Blessd — El Bendecido', use_column_width=True)

# --- Opinión del usuario ---
st.subheader("🎧 ¿Qué opinas sobre Blessd?")
texto = st.text_input('Escribe tu opinión aquí:', '')

if texto:
    st.success('¡Gracias por compartir tu opinión sobre Blessd! 🔥')
    st.write(f"Tu opinión: *{texto}*")

# --- Información adicional ---
st.markdown("---")
st.subheader("📀 Datos rápidos:")
st.write("""
- **Nombre real:** Stiven Mesa Londoño  
- **Ciudad:** Medellín, Colombia  
- **Género musical:** Reggaetón / Trap latino  
- **Colaboraciones:** Feid, Ryan Castro, Maluma, entre otros  
- **Frase icónica:** *“Bendecido y afortunado, gracias a Dios y al barrio.”*
""")


