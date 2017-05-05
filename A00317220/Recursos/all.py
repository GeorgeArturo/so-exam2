from modelo import db
from modelo import Datos
from logica import memoria, get_espacioDisco, get_cpu, getEstado

db.create_all()

datos = Datos(get_cpu()[2],memoria()[0],get_espacioDisco()[1],getEstado()[0] )

db.session.add(datos)
db.session.commit()

var=Datos.query.all()
print(var)
