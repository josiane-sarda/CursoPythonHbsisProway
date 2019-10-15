from models.Investimento import Investimento
from datetime import datetime
#import pandas as pd

class Metodos:

    def set_arquivo(self, investimentos):
        with open('investimentos.txt', 'a') as invest:
            invest.write(f'{investimentos.categoria},{investimentos.tipo},{investimentos.aporte},{investimentos.rentabilidade},{investimentos.periodo_rentabilidade}\n', )

    def get_arquivo(self):
        with open('investimentos.txt', 'r') as invest: 
            lista_objetos = []    
            for i in invest:
                inv = i.strip().split(',')     
                #date = datetime.strptime(inv[4], '%Y-%m-%d').date()  
               # date = date.strftime("%d/%m/%Y")            
                lista_objetos.append(Investimento(inv[0], inv[1], float(inv[2]), float(inv[3]), inv[4]))
            return lista_objetos


'''
importar a biblioteca pandas
date = datetime.strptime(date, '%Y-%m-%d').date() --> converte a string date em data 
d1 = pd.datetime.now().date() --> pega a data do dia atual
dias = abs((date - d1).days)  --> calcula a data inicial menos a final e retorna em dias
'''