import csv
from clases import Automovil


def guardar(nombre_archivo, Automovil):
    archivo = open(nombre_archivo, "w")
    datos = [(Automovil.__class__, Automovil.__dict__)]
    archivo_csv = csv.writer(archivo, lineterminator='\n')
    archivo_csv.writerows(datos)
    archivo.close()


def recuperar(nombre_archivo):
    vehiculos = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = csv.reader(archivo)
    for vehiculo in archivo_csv:
        vehiculos.append(vehiculo)
    archivo.close()
    return vehiculos


automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
guardar("ejemplo.csv", automovil)
automoviles = recuperar("ejemplo.csv")

for automovil in automoviles:
    print(automovil)
