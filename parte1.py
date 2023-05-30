from clases import Automovil


def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Ingrese un número válido")
            continue
        else:
            return userInput


while True:
    vehiculos = []
    cantidad = inputNumber("Cuantos vehículos desea insertar: ")
    for i in range(cantidad):
        print(f"\nDatos del automóvil {i+1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        n_ruedas = inputNumber("Inserte el número de ruedas: ")
        velocidad = inputNumber("Inserte la velicidad en km/h: ")
        cilindrada = inputNumber("Inserte el cilindraje en cc: ")
        vehiculos.append(Automovil(marca, modelo, n_ruedas, velocidad, cilindrada))
    break

if vehiculos:
    print("\nImprimiendo por pantalla los vehículos: ")
    for index, value in enumerate(vehiculos):
        print(f"Datos del automóvil {index+1}: ", end="")
        print(f"Marca {value.marca}", end=", ")
        print(f"Modelo {value.modelo}", end=", ")
        print(f"{value.n_ruedas} ruedas", end=", ")
        print(f"{value.velocidad} Km/h", end=", ")
        print(f"{value.cilindrada} cc")
