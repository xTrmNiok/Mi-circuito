import streamlit as st

st.set_page_config(page_title="Simulador de Circuito", layout="wide")

st.title("🏎️ Mi Circuito Matemático Personalizado")

# --- BARRA LATERAL: AQUÍ PUEDES CAMBIAR TODO ---
st.sidebar.header("⚙️ Parámetros de la Fórmula")

# Variables iniciales
u_inicial = st.sidebar.number_input("Valor inicial de U", value=250.0)
limite = st.sidebar.number_input("Límite de la bolsa (Z)", value=1000.0)

st.sidebar.divider()

# Parámetros de los Bloques
n1 = st.sidebar.number_input("Bloque 1: Multiplicar por", value=663.0)
n2 = st.sidebar.number_input("Bloque 2: Dividir entre", value=550.0)
p3 = st.sidebar.number_input("Bloque 3: Restar porcentaje (%)", value=5.5)
n4 = st.sidebar.number_input("Bloque 4: Dividir entre (final)", value=1.04)

# --- LÓGICA DEL CIRCUITO ---
u_actual = u_inicial
limite_restante = limite
vueltas = []

while limite_restante > 0:
    # Bloque 1: U * N1
    b = u_actual * n1
    # Bloque 2: B / N2
    d = b / n2
    # Bloque 3: D - P3%
    z = d * (1 - (p3 / 100))
    
    # Si lo que hay que restar supera lo que queda en la bolsa, paramos
    if z > limite_restante:
        break
        
    limite_restante -= z
    # Bloque 4: Z / N4 (Este resultado es el nuevo U para la siguiente vuelta)
    u_proximo = z / n4
    
    vueltas.append({
        "Vuelta": len(vueltas) + 1,
        "U inicial": round(u_actual, 4),
        "Z (Resta)": round(z, 4),
        "Bolsa": round(limite_restante, 4)
    })
    u_actual = u_proximo

# --- MOSTRAR RESULTADOS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📊 Vueltas completadas: {len(vueltas)}")
    st.table(vueltas)

with col2:
    st.metric("Lo que sobró en la bolsa", round(limite_restante, 4))
    st.info(f"El próximo valor de Z sería {round(u_actual * n1 / n2 * (1 - p3/100), 2)}, por eso se detuvo.")
