from datetime import date
from src.modelo.Trabajador import Trabajador
from src.modelo.Bonificacion import Bonificacion
from src.modelo.Descuento import Descuento
from src.modelo.declarative_base import Base, engine, Session

# create a new session
session = Session()
# 3 - extract all movies
trabajadores = session.query(Trabajador).all()

# Imprimir trabajadores
print('\n### Todos los trabajadores:')
for trabajador in trabajadores:
    print(f'Id: {trabajador.id} - Mes-Año: {trabajador.mesAnio} - Nombre: {trabajador.nombreTrabajador:25} - Sueldo básico: {trabajador.sueldoBasico}')
print('')

print("Join 1: Trabajador, Descuento")
result = session.query(Trabajador).join(Descuento).all()
for row in result:
   for des in row.descuento:
            print (row.id, des.id)

print("Join 2: Trabajador, Descuento")
for c, i in session.query(Trabajador, Descuento) \
    .filter(Trabajador.id == Descuento.id) \
    .all():
    print (f"Id: {c.id} Días Falta: {i.diasFalta}")
print('')

print("Join: Trabajador, Descuento, Bonificacion:")
for c, i, x in session.query(Trabajador, Descuento, Bonificacion) \
    .filter(Trabajador.id == Descuento.id) \
    .filter(Trabajador.id == Bonificacion.id) \
    .all():
   print(f'Id: {c.id} Días de falta: {i.diasFalta} Movilidad: {x.movilidad} ')
