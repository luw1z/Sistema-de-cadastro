import sys
nome = ""
email = ""
senha = ""


while True:
    #verificador do nome
    nome = input("digite seu nome: ").lower()
    nomevalid = nome.replace(" ", "").lower()
    if nomevalid.isalpha():
        print(f"Ola, {nome} ")
        break

while True:
    #verificador do email
    email = input("digite seu email: ")
    if email.find("@") == -1 or "." not in email:
        print("email incorreto")
    else:
        print(f"seu email é: {email}")
        break

while True:
    #verificador da qtd de caracteres na senha
    senha = input("digite sua senha: ")
    if len(senha) >= 8:
       print("senha valida")
       break
    else: 
        print("senha curta demais ")
    

print(email.find("@"))
    
usuario1 = {
    "nome": nome ,
    "email": email ,  
    "senha": senha, 
}
print (f"informacoes do usuario: {usuario1}")
