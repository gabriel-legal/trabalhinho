def calculos (a, b):
     a= int (input("valor 1: "))
     b=  int (input("valor 2: "))
     resultado = a + b
     print (resultado)

def userdata ():
    username = input("insira nome:")
    senha= input ("insira senha:")
    
    if username == "admin" and senha == "0000":
        print ("acesso permitido")
        calculos(0, 0)
        
    else:
        print ("acesso negado")
    
userdata()