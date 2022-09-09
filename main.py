from Usuario import Usuario

user1 = Usuario("Adrien",'adrien@codingdojo.com')
user2 = Usuario("Mr Nibbles",'nibbles@codingdojo.com')
user3 = Usuario("Michael",'michael@codingdojo.com')

# user1: 3 depositos, 1 giro, mostrar balances
user1.hacer_deposito(500)
user1.hacer_deposito(250)
user1.hacer_deposito(50) # 800 total
user1.hacer_retiro(360) # -360
user1.mostrar_balance_usuario() # 440

# user2: 2 depositos, 2 giros, mostrar balances
user2.hacer_deposito(1000)
user2.hacer_deposito(820) # 1820 total
user2.hacer_retiro(900)
user2.hacer_retiro(5) # 915
user2.mostrar_balance_usuario()

# user3: 1 deposito, 3 giros, mostrar balances
user3.hacer_deposito(5000)
user3.hacer_retiro(150)
user3.hacer_retiro(380)
user3.hacer_retiro(2800) # 1670
user3.mostrar_balance_usuario()

# user1: transferir a user3, mostrar sus balances
user1.transfer_dinero(user3,440)
user1.mostrar_balance_usuario() # 0
user3.mostrar_balance_usuario() # 2110