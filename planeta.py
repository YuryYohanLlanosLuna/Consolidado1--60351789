import math

class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float, distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = float(masa)
        self.radio = float(radio)
        self.distancia_al_sol = float(distancia_al_sol)
        self.tiene_vida = tiene_vida

    def calcular_densidad(self) -> float:
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        return self.masa / volumen

    def es_planeta_exterior(self) -> bool:
        return self.distancia_al_sol > 5.2

    def __str__(self) -> str:
        tipo = "Exterior" if self.es_planeta_exterior() else "Interior"
        return (f"Planeta: {self.nombre} | Densidad: {self.calcular_densidad():.2f} kg/m³ | "
                f"Ubicación: {tipo} | Tiene vida: {'Sí' if self.tiene_vida else 'No'}")


if __name__ == "__main__":
    tierra = Planeta(nombre="Tierra", masa=5.972e24, radio=6371000, distancia_al_sol=1.0, tiene_vida=True)
    jupiter = Planeta(nombre="Júpiter", masa=1.898e27, radio=69911000, distancia_al_sol=5.204, tiene_vida=False)

    print(tierra)
    print(jupiter)