class Automovil:
    def __init__(self, marca: str, modelo: str, velocidad_max: float, nivel_combustible: float, año_fabricacion: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

    @property
    def año_fabricacion(self) -> int:
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor: int):
        if not (1886 <= valor <= 2026):
            raise ValueError(f"Año de fabricación inválido ({valor}). Debe estar entre 1886 y 2026.")
        self._año_fabricacion = int(valor)

    @property
    def nivel_combustible(self) -> float:
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor: float):
        if not (0.0 <= valor <= 100.0):
            raise ValueError(f"Nivel de combustible inválido ({valor}%). Debe estar entre 0.0 y 100.0.")
        self._nivel_combustible = float(valor)

    @property
    def velocidad_max(self) -> float:
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float):
        if valor <= 0:
            raise ValueError(f"Velocidad máxima inválida ({valor} km/h). Debe ser mayor a 0.")
        self._velocidad_max = float(valor)

    def tiempo_llegada(self, distancia_km: float) -> float:
        return distancia_km / self.velocidad_max

    def __str__(self) -> str:
        return (f"Automóvil: {self.marca} {self.modelo} ({self.año_fabricacion}) | "
                f"Vel. Máx: {self.velocidad_max} km/h | Combustible: {self.nivel_combustible:.1f}%")


if __name__ == "__main__":
    auto = Automovil("Toyota", "Corolla", 180.0, 75.0, 2022)
    print(auto)
    print(f"Tiempo estimado para recorrer 360 km: {auto.tiempo_llegada(360):.2f} horas\n")

    # Demostración de captura de errores mediante try/except
    print("--- Demostración de validación de propiedades ---")
    try:
        auto.año_fabricacion = 1800
    except ValueError as e:
        print(f"Excepción capturada correctamente: {e}")