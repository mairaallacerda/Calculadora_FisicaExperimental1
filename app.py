from flask import Flask, render_template

app = Flask(__name__)

# Página inicial onde o usuário escolhe o tipo de cálculo
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de escolha do sólido
@app.route('/choose_solid')
def choose_solid():
    return render_template('choose_solid.html')
 
# Rotas para cada página de cálculo de sólido
@app.route('/paralelepipedo')
def paralelepipedo():
    return render_template('paralelepipedo.html')

@app.route('/cubo')
def cubo():
    return render_template('cubo.html')

@app.route('/circulo')
def circulo():
    return render_template('circulo.html')

@app.route('/circulo_vazado')
def circulo_vazado():
    return render_template('circulo_vazado.html')

# Rota para a página da Lei de Hooke
@app.route('/lei_de_hooke')
def lei_de_hooke():
    return render_template('lei_de_hooke.html')

@app.route ('/escolha2')
def escolha2():
    return render_template('escolha2.html')

@app.route('/paralelepipedo1')
def paralelepipedo1():
    return render_template('paralelepipedo1.html')

@app.route('/cilindro')
def cilindro():
    return render_template('cilindro.html')

@app.route('/piramide')
def piramide():
    return render_template('piramide.html')

@app.route('/decomposicao_de_forcas')
def decomposicao_de_forcas():
    return render_template('decomposicao_de_forcas.html')


if __name__ == '__main__':
    app.run(debug=True)
