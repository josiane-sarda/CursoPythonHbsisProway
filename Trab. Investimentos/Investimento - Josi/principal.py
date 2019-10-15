from flask import Flask, render_template, redirect, request

class Investimento:
    def __init__ (self, categoria, tipo, aporte, rentabilidade, periodo_rentabilidade, valor):
        self.categoria = categoria
        self.tipo = tipo 
        self.aporte = aporte
        self.rentabilidade = rentabilidade
        self.periodo_rentabilidade = periodo_rentabilidade
        self.valor = valor

class Carteira_Investimento:
    def __init__ (self, investimento, quantidade, rentabilidade_mensal, rentabilidade_anual):
        self.investimento = investimento
        self.quantidade = quantidade
        self.rentabilidade_mensal = rentabilidade_mensal
        self.rentabilidade_anual = rentabilidade_anual

lista_investimento = []

def salvar_investimento(investimento1):    #metodo criado para azer a interpolacao dos atributos e armazenar as informaçoes dadas pelo usuario
    with open('novo.txt','a') as arquivo:    #no arquivo txt.
        arquivo.write(f'{investimento1.categoria},{investimento1.tipo},{investimento1.aporte},{investimento1.rentabilidade},{investimento1.periodo_rentabilidade},{investimento1.valor} \n')

def listar_investimento():      #metodo que pega os dados do arquivo, separa cada atribudo dentro de vetor
    with open('novo.txt','r') as arquivo:
        for i in arquivo:                                  #split: cada virula encontrada, separar como atributos.
            investimento_recebido = i.strip().split(',')  #variavel que recebe o vetor e separa em cada atributo.
            investimento1 = Investimento(investimento_recebido[0], investimento_recebido[1], investimento_recebido[3], investimento_recebido[4], investimento_recebido[5], investimento_recebido[6])
            lista_investimento.append(investimento1)  #colocando os objetos formados na lista.
    return lista_investimento #retornado a lista... guardando as informaçoes desse objeto na lista

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('home.html', titulo_pagina = 'Abc Invest')

@app.route('/investimentos')
def investimentos():
    return render_template('investimentos.html', titulo_pagina = 'Investimentos')

@app.route('/carteira_de_investimentos')
def carteira_de_investimentos():
    return render_template('carteira.html', titulo_pagina = 'Carteira de Investimentos')

@app.route('/lista')
def lista():
    return render_template('lista.html', titulo_pagina = 'Lista de Investimentos')

@app.route('/salvar-investimento', methods=['POST']) #post: pega os dados que o usuario informou e salva
def salvar():
    categoria = request.form['categoria']
    tipo = request.form['tipo']
    aporte = request.form['aporte']
    rentabilidade = request.form['rentabilidade']
    periodo_rentabilidade = request.form['periodo_rentabilidade']
    valor = request.form['valor']
    investimento1 = Investimento(categoria, tipo, aporte, rentabilidade, periodo_rentabilidade, valor)
    salvar_investimento(investimento1) #chamando o metodo que grava as irformaçoes dentro do arquivo
    return redirect('/lista')

app.run()

