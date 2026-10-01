class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str, saldo_inicial: float = 0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self._saldo = float(saldo_inicial)

    def depositar(self, monto: float):
        # Corrección aplicada: validar que el monto de depósito sea positivo
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0.")
        self._saldo += monto

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self._saldo -= monto

    def consultar_saldo(self) -> float:
        return self._saldo

    def __str__(self) -> str:
        return f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: S/ {self._saldo:.2f}"


class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, tasa_interes: float, saldo_inicial: float = 0.0):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.tasa_interes = float(tasa_interes)

    def calcular_interes(self) -> float:
        return self.consultar_saldo() * (self.tasa_interes / 100.0)

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Tasa Interés: {self.tasa_interes}% | Interés Anual: S/ {self.calcular_interes():.2f}"


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, limite_sobregiro: float, saldo_inicial: float = 0.0):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.limite_sobregiro = float(limite_sobregiro)

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > (self._saldo + self.limite_sobregiro):
            raise ValueError("El monto solicitado excede el límite de sobregiro permitido.")
        self._saldo -= monto

    def permite_sobregiro(self) -> bool:
        return self._saldo < 0

    def __str__(self) -> str:
        base = super().__str__()
        estado_sobregiro = "Sí" if self.permite_sobregiro() else "No"
        return f"{base} | Límite Sobregiro: S/ {self.limite_sobregiro:.2f} | En sobregiro: {estado_sobregiro}"


if __name__ == "__main__":
    print("--- OPERACIONES CUENTA DE AHORROS ---")
    ahorros = CuentaAhorros("AH-1001", "Ana Torres", tasa_interes=4.5, saldo_inicial=1000.0)
    print(ahorros)
    ahorros.depositar(500.0)
    print(f"Saldo tras depósito: S/ {ahorros.consultar_saldo():.2f}")
    print(f"Interés generado: S/ {ahorros.calcular_interes():.2f}\n")

    print("--- OPERACIONES CUENTA CORRIENTE ---")
    corriente = CuentaCorriente("CC-2002", "Carlos Mendoza", limite_sobregiro=500.0, saldo_inicial=200.0)
    print(corriente)
    corriente.retirar(400.0)  # El saldo pasa a -200.0
    print(corriente)
    print(f"¿Cuenta en sobregiro?: {corriente.permite_sobregiro()}")