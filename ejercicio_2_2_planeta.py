from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    def __init__(
        self, nombre, cantidad_satelites, masa, volumen, diametro,
        distancia_sol, tipo, es_observable
    ):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satelites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diametro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.value}")
        print(f"Es observable = {self.es_observable}")

    def calcular_densidad(self):
        return self.masa / self.volumen

    def es_planeta_exterior(self):
        limite = 149_597_870 * 3.4
        return self.distancia_sol > limite


def main():
    p1 = Planeta(
        "Tierra", 1, 5.9736e24, 1.08321e12, 12742,
        150_000_000, TipoPlaneta.TERRESTRE, True
    )
    p2 = Planeta(
        "Jupiter", 79, 1.899e27, 1.4313e15, 139820,
        750_000_000, TipoPlaneta.GASEOSO, True
    )

    for planeta in (p1, p2):
        planeta.imprimir()
        print(f"Densidad del planeta = {planeta.calcular_densidad()}")
        print(f"Es planeta exterior = {planeta.es_planeta_exterior()}")
        print()


if __name__ == "__main__":
    main()
