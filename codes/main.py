import datetime

class Usuario:
    """Un usuario de nuestra plataforma. Por ahora
    sólo recolectamos nombre y cumpleaños.
    Pero pronto tendremos mucho más que eso."""

    def __init__(self, nombre_completo, cumple):
        self.nombre_c = nombre_completo
        self.cumple = cumple

        self.llamadas = 0

        # Extraer partes
        piezas_nombre = nombre_completo.split(" ")
        self.nombre = piezas_nombre[0]
        self.apellido = piezas_nombre[-1]

    def edad(self):
        """Regresa la edad de nuestro usuario en años."""
        hoy = datetime.date.today()
        año = int(self.cumple[0:4])
        mes = int(self.cumple[4:6])
        dia = int(self.cumple[6:8])
        fecha_cumple = datetime.date(año, mes, dia)
        edad_dias = (hoy-fecha_cumple).days
        edad_años = edad_dias/365
        return int(edad_años)

    def __str__(self):
        return self.nombre_c + '  tiene ' + str(self.edad()) + ' años'

    def __call__(self):
        self.llamadas += 1
        return (self.llamadas)


# Ejecución de una tarea por defecto en una instancia de clase: call
Neo = Usuario("Thomas Anderson", "19620311")
# print(Neo)
# print(Neo())
# print(Neo())

# Atributos Intrínsicos de clases y objetos


# print('Atributos de clase\n')
# print('Nombre de la clase: ', Usuario.__name__)
# print('\n Módulo: ', Usuario.__module__)
# print('\n Documentación:\n', Usuario.__doc__)
# print('\nDiccionario de la clase: \n', Usuario.__dict__)
# print('\nClases Base: ', Usuario.__bases__)
# print('\nAtributos del objeto Neo\n')
# print('Clase: ', Neo.__class__)
# print('\n Diccionario: ', Neo.__dict__)


# Herencia de clases
class Lector(Usuario):
    pass


# help(Lector)
l = Lector("Daniel Montenegro", "19901026")
print(l.nombre_c)
print(l.edad())
