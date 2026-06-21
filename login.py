usuario = input("Ingrese su username: ")
password = input("Ingrese su password: ")

if usuario != "" and password != "":
    print("Usuario autenticado")
else:
    print("El usuario y la password no pueden estar vacias")