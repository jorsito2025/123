class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def cambiar_nombre(self):
        nuevo_nombre = input(f"Ingrese el nuevo nombre para {self.nombre}: ")
        if nuevo_nombre:  # Verificamos que no esté vacío
            nombre_anterior = self.nombre
            self.nombre = nuevo_nombre
            print(f"El nombre de {nombre_anterior} ha sido cambiado a {self.nombre}.")
        else:
            print("El nombre no puede estar vacío.")

    def cumplir_anios(self):
        incremento_str = input(f"Ingrese cuántos años ha cumplido {self.nombre}: ")
        if incremento_str.isdigit():
            incremento = int(incremento_str)
            if incremento > 0:
                self.edad += incremento
                print(f"{self.nombre} ahora tiene {self.edad} años.")
            else:
                print("La edad debe incrementarse en un valor positivo.")
        else:
            print("Entrada inválida. Por favor, ingrese un número para los años.")

# Crear un objeto Mascota pidiendo la información al usuario
nombre_mascota = input("Ingrese el nombre de su mascota: ")
especie_mascota = input("Ingrese la especie de su mascota: ")
edad_mascota_str = input("Ingrese la edad de su mascota: ")

if edad_mascota_str.isdigit():
    edad_mascota = int(edad_mascota_str)
    mi_mascota = Mascota(nombre_mascota, especie_mascota, edad_mascota)

    print("\nInformación de la mascota creada:")
    print(f"Nombre: {mi_mascota.nombre}")
    print(f"Especie: {mi_mascota.especie}")
    print(f"Edad: {mi_mascota.edad} años")

    # Llamar a los métodos
    mi_mascota.cambiar_nombre()
    mi_mascota.cumplir_anios()

else:
    print("Entrada inválida para la edad. El programa no puede continuar.")