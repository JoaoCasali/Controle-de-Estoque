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