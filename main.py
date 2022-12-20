from entities.usuario import Usuario
from config import *


@app.route("/")
def index():
    return "tela inicial"

@app.route('/login')
def login():

    log = request.args.get('log')

    return render_template('login.html', log=log)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    
    usuario = Usuario.query.filter_by(usu=request.form['usuario']).first()

    if usuario:

        if request.form['senha'] == usuario.senha:

            session['usuario_logado'] = usuario.usuario

            flash(usuario.usuario + ' Logado')

            log_proximo = request.args.get('log')

            return redirect(log_proximo)
        
    else:
        flash('Usuario ou senha Incorretos')

        return redirect(url_for('login'))

@app.route('/')
def index():
    lista = Produtos.query.order_by(Produtos.id)
    return render_template("lista.html", titulo = 'produtos', produtos = lista)

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    marca = request.form['marca']
    unidade = request.form['unidade']
    preco = request.form['preco']

    produto = Produtos.query.filter_by(nome=nome).first()

    if produto:
        flash('Produto Ja Existente!')
        return redirect(url_for('index'))


    novo_produto = Produtos(nome=nome, marca=marca, unidade=unidade, preco=preco)

    db.session.add(novo_produto)

    db.session.commit()

    return redirect(url_for('index'))
