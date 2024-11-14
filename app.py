from flask import Flask, render_template, request, flash, redirect, url_for  #Para carregar o template
from forms import ContactForm

app = Flask(__name__)

#Criação da chave segura
app.secret_key = 'chave_segura'

#Criar a 1 pagina do site

# route
# função
# template


    
@app.route("/") #como é a homepage uso somente a /
def homepage():
    return render_template("homepage.html")

@app.route("/contatos", methods=["GET", "POST"])

def contatos():
    form = ContactForm()
    
    if form.validate_on_submit(): #Verifica se foi válido e submetido
        flash("Formulario enviado com sucesso!", "success")
        
        #Redireciona para essa página
        return redirect(url_for('contatos'))
    
    return render_template("contatos.html", form=form)


@app.route("/usuarios/<nome_usuario>")  #<> para o usúario ser dinâmico
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario) #

#Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) #pra não ficar precisando rodar o código toda vez
