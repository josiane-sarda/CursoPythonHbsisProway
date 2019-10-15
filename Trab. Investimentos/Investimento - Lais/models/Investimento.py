from datetime import date
class Investimento():   
    def __init__(self, cat, tipo, aporte, rent, periodo):
        self.categoria = cat
        self.tipo = tipo
        self.aporte = float(aporte)
        self.rentabilidade = float(rent)
        self.periodo_rentabilidade = periodo