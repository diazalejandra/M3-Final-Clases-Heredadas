import csv


class Vehiculo():

    def __init__(self, marca, modelo, n_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas

    def guardar_datos_csv(self, nombre_archivo):
        archivo = open(nombre_archivo, "a")
        datos = [(self.__class__, self.__dict__)]
        archivo_csv = csv.writer(archivo, lineterminator='\n')
        archivo_csv.writerows(datos)
        archivo.close()

    def recuperar_datos_csv(nombre_archivo):
        vehiculos = []
        archivo = open(nombre_archivo, "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            vehiculos.append(vehiculo)
        archivo.close()
        return vehiculos

    def imprimir_por_clase(vehiculos):
        tipos = ["Particular", "Carga", "Bicicleta", "Motocicleta"]
        vehiculos.sort()

        for tipo in tipos:
            print(f"\nLista de Vehículos {tipo}: ")
            for vehiculo in vehiculos:
                class_str = vehiculo[0].split("'")[1].rsplit('.', 1)[1]
                if class_str == tipo:
                    print(vehiculo[1])


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, n_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


class Particular(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, n_puestos):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.n_puestos = n_puestos


class Carga(Automovil):
    def __init__(self, marca, modelo, n_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, n_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga


class Bicicleta(Vehiculo):
    tipos = ["Urbana, Carrera"]

    def __init__(self, marca, modelo, n_ruedas, tipo):
        super().__init__(marca, modelo, n_ruedas)
        self.tipo = tipo


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, n_ruedas, tipo, motor, cuadro, n_radios):
        super().__init__(marca, modelo, n_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.n_radios = n_radios
