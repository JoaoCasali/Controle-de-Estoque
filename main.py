from config import *
from entities.usuario import Usuarios
from entities.produto import Produtos
from entities.estoque import Estoque


@app.route("/")
def Index():
    return render_template("usuario/login.html")


@app.route('/Login')
def Login():
    return render_template('login.html')


@app.route('/Autenticar', methods=['POST',])
def Autenticar():

    usuario = Usuarios.query.filter_by(NOM_PES=request.form['usuario']).first()

    if usuario:

        if request.form['senha'] == usuario.SENHA:

            session['usuario_logado'] = usuario.NOM_PES

            session['usuario_id'] = usuario.ID

            flash(usuario.NOM_PES + ' Logado')

            return redirect(url_for("ListarProduto"))

    else:
        flash('Usuario ou senha Incorretos')

        return redirect(url_for('Index'))


@app.route('/ListarProduto')
def ListarProduto():
    lista = Produtos.query.filter_by(USU_ID=session['usuario_id'])
    return render_template("produto/listar.html", titulo='produtos', produtos=lista)

# @app.route('/Criar', methods=['POST',])
# def Criar():
#     nome = request.form['nome']
#     marca = request.form['marca']
#     unidade = request.form['unidade']
#     preco = request.form['preco']

#     produto = Produtos.query.filter_by(nome=nome).first()

#     if produto:
#         flash('Produto Ja Existente!')
#         return redirect(url_for('index'))


#     # novo_produto = Produtos(nome=nome, marca=marca, unidade=unidade, preco=preco)

#     # db.session.add(novo_produto)

#     db.session.commit()

#     return redirect(url_for('index'))

@app.route('/ListarEstoque')
def ListarEstoque():

    lista = Estoque.query.filter_by(USU_ID=session['usuario_id'])
    return render_template("estoque/listar.html", titulo='estoque', estoques=lista)


@app.route('/logout')
def Logout():
    return redirect(url_for('Index'))

@app.route('/NovoEstoque')
def NovoEstoque():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect (url_for('Login'))

    return render_template('estoque/editar.html', titulo='Novo Estoque', estoque = Estoque(PRO_ID = '', QTD_PRO = ''))

@app.route('/CriarEstoque', methods=['POST'])
def CriarEstoque():
    produto = request.form['produto_id']
    quantidade = request.form['quantidade']

    cadastro_estoque = Estoque(PRO_ID=produto, QTD_PRO=quantidade, USU_ID=session["usuario_id"])

    db.session.add(cadastro_estoque)
    db.session.commit()

    return redirect (url_for('ListarEstoque'))

if __name__ == "__main__":
    app.run(debug=True)
