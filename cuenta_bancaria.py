class cuenta_bancaria:
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        
    def deposito_bancario(self, amount):
        self.balance += amount
        return self
    def retiro_bancario(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Retiro Invalido (No puede quedar en negativo)")
        return self
    def mostrar_info_cuenta(self):
        print(f"Tasa de interes: {self.tasa_interes}, Balance: {self.balance}")
    def generar_interes(self):
        interes = (self.tasa_interes / 100) * self.balance
        self.balance += interes 
        return self

usuario1 = cuenta_bancaria(5, 0)
usuario2 = cuenta_bancaria(15, 100)

usuario1.deposito_bancario(50).deposito_bancario(30).deposito_bancario(100).retiro_bancario(70).generar_interes().mostrar_info_cuenta()
usuario2.deposito_bancario(550).deposito_bancario(120).retiro_bancario(80).retiro_bancario(30).retiro_bancario(110).retiro_bancario(50).generar_interes().mostrar_info_cuenta()


