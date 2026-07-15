import mysql.connector

# Conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_bancario"
)
cursor = conexao.cursor()
usuario_atual = 'usuario_teste'

def obter_saldo(usuario):
    """Busca o saldo atualizado no banco de dados."""
    query = "SELECT saldo FROM contas WHERE usuario = %s"
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()
    return float(resultado[0]) if resultado else 0.0

def atualizar_saldo(usuario, novo_saldo):
    """Atualiza o saldo no banco de dados."""
    query = "UPDATE contas SET saldo = %s WHERE usuario = %s"
    cursor.execute(query, (novo_saldo, usuario))
    conexao.commit()  # Salva a alteração no banco

while True:
    opcao = int(input("1 - Ver saldo\n2 - Depositar\n3 - Sacar\n4 - Sair\n"))
    
    if opcao == 1:
        saldo = obter_saldo(usuario_atual)
        print(f"Seu saldo é: R${saldo:.2f}\n")

    elif opcao == 2:
        deposito = float(input("Quanto deseja depositar?\n"))
        if deposito <= 0:
            print("Depósito inválido")
        else:
            saldo_atual = obter_saldo(usuario_atual)
            novo_saldo = saldo_atual + deposito
            atualizar_saldo(usuario_atual, novo_saldo)
            print(f"Depósito realizado! Novo saldo: R${novo_saldo:.2f}\n")

    elif opcao == 3:
        sacar = float(input("Quanto deseja sacar?\n"))
        saldo_atual = obter_saldo(usuario_atual)
        
        if sacar <= 0:
            print("Valor de saque inválido")
        elif sacar > saldo_atual:
            print("Saldo insuficiente")
        else:
            novo_saldo = saldo_atual - sacar
            atualizar_saldo(usuario_atual, novo_saldo)
            print(f"Saque realizado! Novo saldo: R${novo_saldo:.2f}\n")
            
    elif opcao == 4:
        print("Sistema encerrado")
        break
    else:
        print("Opção inválida")

# Conexões fechadas ao sair do programa
cursor.close()
conexao.close()