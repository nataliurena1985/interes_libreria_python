
import streamlit as st
import libreria_dmc as DMC

st.title("Aplicacion  de funciones")

monto=st.number_input("Ingrese el monto")
tasa=st.number_input("Ingrese la tasa")
tiempo=st.number_input("Ingrese el tiempo")


resultado = DMC.interes_simple(monto,tasa,tiempo)
st.write(resultado)