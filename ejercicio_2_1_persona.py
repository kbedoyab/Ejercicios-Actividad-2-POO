class Persona:
    def __init__(self, nombre, apellidos, numero_documento_identidad, anio_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.anio_nacimiento = anio_nacimiento

    def imprimir(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Numero de documento de identidad = {self.numero_documento_identidad}")
        print(f"Anio de nacimiento = {self.anio_nacimiento}")


def main():
    persona1 = Persona("Pedro", "Perez", "123456789", 2005)
    persona2 = Persona("Maria", "Gomez", "987654321", 2004)

    print("Persona 1")
    persona1.imprimir()
    print()
    print("Persona 2")
    persona2.imprimir()


if __name__ == "__main__":
    main()
