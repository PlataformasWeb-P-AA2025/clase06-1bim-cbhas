import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

saludos = session.query(Saludo2).all()

st.title("Presentación de todos los Saludos")

for saludo  in saludos:
    st.write(saludo)
    st.markdown("---")

st.markdown("---")
st.title("Presentación de todos los Saludos en Tabla")
lista = []

for s in saludos:
    diccionario = {"id": s.id, "mensaje": s.mensaje, "tipo": s.tipo}
    lista.append(diccionario)

st.dataframe(lista)
