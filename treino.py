import sys
nome =("")
idade = 0
cidade = ("")

while True:
    nome = (input("digite seu nome"))
    if nome.isalpha():
        break

while True: 
    idade = (input("digite sua idade"))
    if idade.isnumeric():
        break
        
while True:
    idade = int(idade)
    if idade < 15:
        print ("voce nao atende os requisitos de idade, cadastro cancelado")
        sys.exit()
       

while True:
    cidade = input("digite sua cidade")
    if cidade.isalpha():
        break
    


dados =  {
    "nome" : nome,
    "idade" : idade, 
    "cidade" : cidade,
}

print(dados)