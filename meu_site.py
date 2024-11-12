from flask import Flask, render_template  #Para carregar o template

app = Flask(__name__)

#Criar a 1 pagina do site

# route
# função
# template
@app.route("/") #como é a homepage uso somente a /
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuarios/<nome_usuario>")  #<> para o usúario ser dinâmico
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario) #

#Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) #pra não ficar precisando rodar o código toda vez
