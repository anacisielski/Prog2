from flask import Flask, render_template, request, session, redirect

app=Flask(__name__)

app.config["SECRET_KEY"] = "camelo"

class Pessoa:
    def __init__(self,nome,endereco,telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone



lista_de_pessoas=[Pessoa("Joao","Rua da arvore","33447698"),
                  Pessoa("Brisola","Sem casa","2244552367"),
                  Pessoa("Dj guuga","Na sua cama","6783346"),
                  Pessoa("Kapela","Sem dona","171")]


@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html",geral = lista_de_pessoas)    

@app.route("/inserir_pessoa")
def inserir_pessoas():
    return render_template("form_inserir_pessoa.html")  

@app.route("/alterar_pessoas")
def alterar_pessoas():
    return render_template("form_alterar_pessoa.html")  

@app.route("/exibir_mensagem")
def exibir_mensagem():
    return render_template("exibir_mensagem.html")

@app.route("/cadastrar_pessoa")
def add():
    endereco = request.args.get("endereco")
    nome = request.args.get("nome")
    lista = ([Pessoa(nome,endereco,"23454")])
    lista_de_pessoas.append(Pessoa(nome,endereco,"23454"))
    return render_template ("listar_pessoas.html", teste = lista, geral = lista_de_pessoas)

@app.route("/excluir_pessoa")
def excluir():
    achou = None
    nome = request.args.get("nome")
    for p in lista_de_pessoas:
        if p.nome == nome:
            achou = p
            break
    if achou != None:
        lista_de_pessoas.remove(achou)
    return listar_pessoas()

@app.route("/login")
def login():
    login = request.args.get("login")
    senha = request.args.get("senha")
    if login == "Ana" and senha == "123":
        session["usuario"] = login
        return redirect("/")
    else:
        return "login/senha inválidos"

@app.route("/form_login")
def form_login():
   return render_template("form_login.html")


@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/")
    
app.run()