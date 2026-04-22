def calculos (a, b):
     a= int (input("valor 1: "))
     b=  int (input("valor 2: "))
     calc= str(input("some = 1, sub = 2, div = 3, multi = 4, potencia = 5: "))
     if calc ==  "1":
         resultado = a + b
     elif calc == "2":
         resultado = a - b
     elif calc == "3":
         resultado = a / b
     elif calc == "4":
         resultado = a * b
     elif calc == "5":
         resultado = a ** b
     print (resultado)
     print ("\n ----adeus usuario---- \n")

def userdata ():
    username = input("insira nome: ")
    senha= input ("insira senha: ")
    
    if username == "admin" and senha == "0000":
        print ("acesso permitido")
        calculos(0, 0)
        
    else:
        print ("acesso negado")
        
def intro():
    print ("\nBem vindo a calculadora 2.0\n")
    print ("essa é a melhor calculadora que você jamais verá na sua vida\n")
    print ("por favor, insira o nome e senha de usuario para proseguir:\n")
    
intro()

userdata()