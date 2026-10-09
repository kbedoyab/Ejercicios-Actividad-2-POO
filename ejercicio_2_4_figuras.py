import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * self.base + 2 * self.altura


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo(self):
        hipotenusa = self.calcular_hipotenusa()
        lados = (self.base, self.altura, hipotenusa)

        if math.isclose(self.base, self.altura) and math.isclose(self.base, hipotenusa):
            return "Equilatero"
        if math.isclose(self.base, self.altura) or math.isclose(self.base, hipotenusa) or math.isclose(self.altura, hipotenusa):
            return "Isosceles"
        return "Escaleno"


def main():
    figura1 = Circulo(2)
    figura2 = Rectangulo(1, 2)
    figura3 = Cuadrado(3)
    figura4 = TrianguloRectangulo(3, 4)

    print(f"El area del circulo es = {figura1.calcular_area()}")
    print(f"El perimetro del circulo es = {figura1.calcular_perimetro()}")

    print(f"El area del rectangulo es = {figura2.calcular_area()}")
    print(f"El perimetro del rectangulo es = {figura2.calcular_perimetro()}")

    print(f"El area del cuadrado es = {figura3.calcular_area()}")
    print(f"El perimetro del cuadrado es = {figura3.calcular_perimetro()}")

    print(f"El area del triangulo es = {figura4.calcular_area()}")
    print(f"El perimetro del triangulo es = {figura4.calcular_perimetro()}")
    print(f"El triangulo es = {figura4.determinar_tipo()}")


if __name__ == "__main__":
    main()
