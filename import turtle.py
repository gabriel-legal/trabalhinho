import turtle

screen = turtle.Screen()
screen.title("Calculadora 2.0")
screen.setup(width=600, height=400)
t = turtle.Turtle()
t.hideturtle()

def exibir_mensagem(msg, y=0, cor="black"):
    t.penup()
    t.goto(0, y)
    t.color(cor)
    t.write(msg, align="center", font=("Arial", 14, "bold"))

def calculos():
    t.clear()
    a = screen.numinput("Valor 1", "Insira o primeiro número:")
    b = screen.numinput("Valor 2", "Insira o segundo número:")
    
    msg_menu = "1: Soma, 2: Sub, 3: Div, 4: Mult, 5: Pot"
    calc = screen.textinput("Operação", msg_menu)

    if calc == "1": resultado = a + b
    elif calc == "2": resultado = a - b
    elif calc == "3": resultado = a / b
    elif calc == "4": resultado = a * b
    elif calc == "5": resultado = a ** b
    else: resultado = "Operação Inválida"

    exibir_mensagem(f"Resultado: {resultado}", 0, "blue")
    exibir_mensagem("Adeus usuário!", -50, "red")

def userdata():

    username = screen.textinput("Login", "Insira o nome de usuário:")
    senha = screen.textinput("Senha", "Insira a senha:")
    
    if username == "admin" and senha == "0000":
        t.clear()
        exibir_mensagem("Acesso Permitido!", 50, "green")
        calculos()
    else:
        exibir_mensagem("Acesso Negado!", 0, "red")

def intro():
    exibir_mensagem("Bem-vindo à Calculadora 2.0", 50)
    exibir_mensagem("A melhor que você já viu!", 20)
    userdata()

intro()
screen.mainloop()