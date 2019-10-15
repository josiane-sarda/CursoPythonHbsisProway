from flask import Flask, render_template, request, redirect
from models.cerveja import Cerveja
from models.pedidos import Pedido

app=Flask(__name__)
lista_cervejas = []
lista_pedido = []

@app.route('/')
def inicio():
    return render_template('index.html', titulo_pagina = 'Home')

@app.route('/listar')
def listar():
    return render_template('listar.html', titulo_pagina = 'Listar', lista = lista_cervejas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo_pagina = 'Cadastrar')

@app.route('/fazer_pedido')
def fazer_pedido():
    return render_template('fazer_pedido.html', titulo_pagina = 'Fazer_pedido', lista = lista_pedido)

@app.route('/salvar', methods=['POST'])
def salvar(): 
    nome  = request.form['nome']
    tipo  = request.form['tipo']
    preco  = request.form['preco']
    validade  = request.form['validade']
    nova_cerveja = Cerveja(nome, tipo, preco, validade)
    lista_cervejas.append(nova_cerveja)
    return redirect('/listar')

@app.route('/salvar_pedido', methods=['POST'])
def salvar_pedido(): 
    item  = request.form['item']
    quantidade  = request.form['quantidade']
    novo_pedido = Pedido(item, quantidade)
    lista_pedido.append(novo_pedido)
    return redirect('/fazer_pedido')


app.run()