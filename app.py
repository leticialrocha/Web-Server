from flask import Flask, render_template_string

app = Flask(__name__)

# Página inicial
@app.route('/')
def home():
    return render_template_string("""
        <html>
            <head><title>Meu Site</title></head>
            <body>
                <h1>Bem-vindo ao meu site em Python!</h1>
                <p>Este site foi criado com Flask.</p>
                <a href="/sobre">Ir para Sobre</a>
            </body>
        </html>
    """)

# Página "Sobre"
@app.route('/sobre')
def sobre():
    return render_template_string("""
        <html>
            <head><title>Sobre</title></head>
            <body>
                <h1>Sobre</h1>
                <p>Este site é um exemplo básico com Flask.</p>
                <a href="/">Voltar</a>
            </body>
        </html>
    """)

# Executar o servidor
if __name__ == '__main__':
    app.run(debug=True)
