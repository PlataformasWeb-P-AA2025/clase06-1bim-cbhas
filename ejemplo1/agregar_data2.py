from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine
from csv import DictReader

Session = sessionmaker(bind=engine)
session = Session()

with open("data/saludos_mundo.csv", "r") as archivo:
    csv = DictReader(archivo, delimiter='|')
    for fila in csv:
        miSaludo = Saludo2()
        miSaludo.mensaje = fila["mensaje"]
        miSaludo.tipo = fila["tipo"]
        miSaludo.origen = fila["origen"]

        session.add(miSaludo)


session.add(miSaludo)

session.commit()
