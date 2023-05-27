from clases import Automovil

while True:
    vehiculos = []
    cantidad = int(input("Cuantos vehículos desea insertar: "))
    for i in range(cantidad):
        print(f"\nDatos del automóvil {i+1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        n_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velicidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        vehiculos.append(Automovil(marca, modelo, n_ruedas, velocidad, cilindrada))

    print("\nImprimiendo por pantalla los vehículos: ")
    for index, value in enumerate(vehiculos):
        print(f"Datos del automóvil {index+1}: ", end="")
        print(f"Marca {value.marca}", end=", ")
        print(f"Modelo {value.modelo}", end=", ")
        print(f"{value.n_ruedas} ruedas", end=", ")
        print(f"{value.velocidad} Km/h", end=", ")
        print(f"{value.cilindrada} cc")
    break
