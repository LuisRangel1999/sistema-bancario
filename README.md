# Sistema Bancário 🏦

Um projeto pessoal de um sistema bancário via terminal desenvolvido para praticar lógica de programação e integração com banco de dados.

## 🚀 Funcionalidades
* Consulta de saldo em tempo real.
* Operações de depósito com validação de valores positivos.
* Operações de saque com verificação de saldo em conta.
* Persistência de dados: o saldo não é perdido ao fechar o programa.

## 🛠️ Tecnologias Utilizadas
* **Python** (Lógica do sistema e interações via terminal)
* **MySQL** (Armazenamento permanente dos dados da conta)
* **mysql-connector-python** (Biblioteca para conectar o Python ao MySQL)

## ⚙️ Como executar na sua máquina

1. Certifique-se de ter o Python e o MySQL instalados.
2. Crie o banco de dados e a tabela usando o seguinte script SQL:
   ```sql
   CREATE DATABASE sistema_bancario;
   USE sistema_bancario;
   CREATE TABLE contas (
       id INT AUTO_INCREMENT PRIMARY KEY,
       usuario VARCHAR(50) NOT NULL,
       saldo DECIMAL(10, 2) NOT NULL DEFAULT 1000.00
   );
   INSERT INTO contas (usuario, saldo) VALUES ('usuario_teste', 1000.00);
3. Instale a biblioteca de conexão rodando no terminal: **pip install mysql-connector-python**
4. Preencha suas credenciais do banco de dados no arquivo app.py.
5. Execute o programa: python app.py