from flask import Flask, render_template, request, redirect
from models.Investimento import Investimento
from datetime import date
from metodos import Metodos

app=Flask(__name__)
metodos = Metodos()
investimentos = []

@app.route('/')
def inicio():
    return render_template('principal.html', titulo_pagina = 'Home')
    

@app.route('/cadastrar-investimento')
def cadastrarInvestimento():
    return render_template('cadastro_investimento.html')


@app.route('/salvar-investimento',  methods=['POST'])
def salvarInvestimento():
    categoria = request.form['categoria']
    tipo = request.form['tipo']
    aporte = request.form['aporte']
    rentabilidade = request.form['rentabilidade']
    periodo = request.form['periodo']

    invest = Investimento(categoria, tipo, aporte, rentabilidade, periodo)
    investimentos.append(invest)
    
    metodos.set_arquivo(invest)

    return redirect('/listar-investimento')
    

@app.route('/listar-investimento')
def listaInvestimento():
    lista_invest = metodos.get_arquivo()
    return render_template('listagem_investimento.html', lista = lista_invest)


app.run()