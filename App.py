import streamlit as st

st.title("🏎️ Mi Circuito Matemático")

# Configuración en la barra lateral
st.sidebar.header("Ajustes")
u_inicial = st.sidebar.number_input("Valor inicial de U", value=250.0)
limite = st.sidebar.number_input("Límite de la bolsa", value=1000.0)

# Lógica del circuito
u_actual = u_inicial
limite_restante = limite
vueltas = []

while limite_restante > 0:
    # Cálculos
    b = u_actual * 663
    d = b / 550
    z = d * 0.945 # Esto es restar el 5.5%
    
    if z > limite_restante:
        break
        
    limite_restante -= z
    u_final_vuelta = z / 1.04
    
    vueltas.append({
        "Vuelta": len(vueltas) + 1,
        "U inicial": round(u_actual, 2),
        "Z (Resta)": round(z, 2),
        "Bolsa": round(limite_restante, 2)
    })
    u_actual = u_final_vuelta

# Mostrar resultados
st.write(f"### Vueltas completadas: {len(vueltas)}")
st.table(vueltas)
st.metric("Lo que sobró en la bolsa", round(limite_restante, 2))
