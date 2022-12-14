class Usuario:

    def __init__(self, username, password):
        self.username = username
        self.password = password

#    def inicializar(self, username, password):
#        self.username = username
#        self.password = password


user1 = Usuario('Alexis','alexis123')
user2 = Usuario('Alexis','alexis123')

#user1.inicializar('Alexis','alexis123')
#user2.inicializar('Miguel','miguel123')

print(user1.__dict__)
print(user2.__dict__)