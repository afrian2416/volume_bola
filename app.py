import math
import streamlit as st

st.title("Kalkulator Volume Bola")

radius = st.number_input("Masukkan jari-jari bola (r):", min_value=0.0, format="%.2f")

def volume_bola(radius):
    return (4/3) * math.pi * radius**3

if st.button("Hitung Volume"):
    volume = volume_bola(radius)
    st.success(f"Volume bola dengan jari-jari {radius:.2f} adalah {volume:.2f} unit kubik.")
