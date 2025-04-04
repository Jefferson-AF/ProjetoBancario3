"""
PROJETO BANCÁRIO - TERCEIRA ATUALIZAÇÃO

Melhorias Implementadas:
- Organização em Classes: Separei o código em classes (Banco, Conta, Usuario)
- Registro de Data/Hora: Adicionei registro para todas as transações
- Histórico de Transações: Extrato com dicionários contendo mais informações
- Validação Melhorada: Captura de erros de digitação
- Nome personalizável para o banco
- Mensagens padronizadas

Futuras melhorias:
- Implementar criação de usuários e contas
- Conectar operações às contas específicas
- Autenticação de usuário
- Persistência de dados
- Transferências entre contas
- Investimentos e empréstimos
- Relatórios gerenciais
- Interface gráfica (ainda não estou estudando isso, mas futuramente)

"""

import textwrap
from datetime import datetime

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.agencia = "0001"
        self.usuarios = []
        self.contas = []
        
    def executar(self):
        self.menu_principal()
    
    @staticmethod
    def formatar_data():
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    def menu_principal(self):
        menu = f"""
        ============= {self.nome.upper()} =============
        [{self.formatar_data()}]
        
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q] Sair
        
        => """
        
        return input(textwrap.dedent(menu))
    
    @staticmethod
    def validar_valor(valor):
        try:
            valor = float(valor)
            if valor <= 0:
                raise ValueError("O valor deve ser positivo")
            return valor
        except ValueError:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return None

class Conta:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500
    
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.saques_realizados = 0
    
    def depositar(self, valor):
        valor = Banco.validar_valor(valor)
        if valor:
            self.saldo += valor
            self.extrato.append({
                "tipo": "Depósito",
                "valor": valor,
                "data": Banco.formatar_data()
            })
            print("\n=== Depósito realizado com sucesso! ===")
    
    def sacar(self, valor):
        valor = Banco.validar_valor(valor)
        if not valor:
            return
        
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
        elif valor > self.LIMITE_VALOR_SAQUE:
            print(f"\n@@@ Operação falhou! Limite por saque: R$ {self.LIMITE_VALOR_SAQUE:.2f} @@@")
        elif self.saques_realizados >= self.LIMITE_SAQUES:
            print(f"\n@@@ Operação falhou! Limite de {self.LIMITE_SAQUES} saques diários atingido. @@@")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append({
                "tipo": "Saque",
                "valor": -valor,
                "data": Banco.formatar_data()
            })
            print("\n=== Saque realizado com sucesso! ===")
    
    def ver_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for mov in self.extrato:
                print(f"{mov['data']} - {mov['tipo']}:\tR$ {mov['valor']:.2f}")
        print(f"\nSaldo atual:\tR$ {self.saldo:.2f}")
        print("=" * 40)

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

def main():
    sistema_bancario = Banco("PyBank")
    
    while True:
        opcao = sistema_bancario.menu_principal().lower()
        
        if opcao == "q":
            print("\nObrigado por usar o PyBank. Até logo!")
            break
        
        elif opcao == "d":
            valor = input("Informe o valor do depósito: ")
            # Implementar lógica de depósito
            
        elif opcao == "s":
            valor = input("Informe o valor do saque: ")
            # Implementar lógica de saque
            
        elif opcao == "e":
            # Implementar lógica de extrato
            pass
            
        elif opcao == "nu":
            # Implementar criação de usuário
            pass
            
        elif opcao == "nc":
            # Implementar criação de conta
            pass
            
        elif opcao == "lc":
            # Implementar listagem de contas
            pass
            
        else:
            print("\n@@@ Operação inválida. Por favor, tente novamente. @@@")

if __name__ == "__main__":
    main()

import textwrap
from datetime import datetime

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.agencia = "0001"
        self.usuarios = []
        self.contas = []
        
    def executar(self):
        self.menu_principal()
    
    @staticmethod
    def formatar_data():
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    def menu_principal(self):
        menu = f"""
        ============= {self.nome.upper()} =============
        [{self.formatar_data()}]
        
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q] Sair
        
        => """
        
        return input(textwrap.dedent(menu))
    
    @staticmethod
    def validar_valor(valor):
        try:
            valor = float(valor)
            if valor <= 0:
                raise ValueError("O valor deve ser positivo")
            return valor
        except ValueError:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return None

class Conta:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500
    
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.saques_realizados = 0
    
    def depositar(self, valor):
        valor = Banco.validar_valor(valor)
        if valor:
            self.saldo += valor
            self.extrato.append({
                "tipo": "Depósito",
                "valor": valor,
                "data": Banco.formatar_data()
            })
            print("\n=== Depósito realizado com sucesso! ===")
    
    def sacar(self, valor):
        valor = Banco.validar_valor(valor)
        if not valor:
            return
        
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
        elif valor > self.LIMITE_VALOR_SAQUE:
            print(f"\n@@@ Operação falhou! Limite por saque: R$ {self.LIMITE_VALOR_SAQUE:.2f} @@@")
        elif self.saques_realizados >= self.LIMITE_SAQUES:
            print(f"\n@@@ Operação falhou! Limite de {self.LIMITE_SAQUES} saques diários atingido. @@@")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append({
                "tipo": "Saque",
                "valor": -valor,
                "data": Banco.formatar_data()
            })
            print("\n=== Saque realizado com sucesso! ===")
    
    def ver_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for mov in self.extrato:
                print(f"{mov['data']} - {mov['tipo']}:\tR$ {mov['valor']:.2f}")
        print(f"\nSaldo atual:\tR$ {self.saldo:.2f}")
        print("=" * 40)

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

def main():
    sistema_bancario = Banco("PyBank")
    
    while True:
        opcao = sistema_bancario.menu_principal().lower()
        
        if opcao == "q":
            print("\nObrigado por usar o PyBank. Até logo!")
            break
        
        elif opcao == "d":
            valor = input("Informe o valor do depósito: ")
            # Implementar lógica de depósito
            
        elif opcao == "s":
            valor = input("Informe o valor do saque: ")
            # Implementar lógica de saque
            
        elif opcao == "e":
            # Implementar lógica de extrato
            pass
            
        elif opcao == "nu":
            # Implementar criação de usuário
            pass
            
        elif opcao == "nc":
            # Implementar criação de conta
            pass
            
        elif opcao == "lc":
            # Implementar listagem de contas
            pass
            
        else:
            print("\n@@@ Operação inválida. Por favor, tente novamente. @@@")

if __name__ == "__main__":
    main()