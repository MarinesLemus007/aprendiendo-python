#Atributo de clase
#Atributo de instancia 

class Usuario:
    #Atributo de clase
    username = "Domarys Flores"
    email = ""

#__dict__

user1 = Usuario()
#1. Verifica si el atributo existe dentro del objeto
#2. Verifica si el atributo existe dentro de la clase - > solo podrá leerlo no lo modifiica
#3. Lanzará un error

print(user1.username)
print(id(user1.username))
print(id(Usuario.username))