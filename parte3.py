from clases import Particular, Carga, Bicicleta, Vehiculo, Motocicleta

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

particular.guardar_datos_csv("vehiculos.csv")
carga.guardar_datos_csv("vehiculos.csv")
bicicleta.guardar_datos_csv("vehiculos.csv")
motocicleta.guardar_datos_csv("vehiculos.csv")

automoviles = Vehiculo.recuperar_datos_csv("vehiculos.csv")
Vehiculo.imprimir_por_clase(automoviles)
