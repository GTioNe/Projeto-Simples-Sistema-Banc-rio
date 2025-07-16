import datetime

class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0
        self.historico_transacoes = []
        self.saque_diario_total = 0.0
        self.ultima_data_saque = None

    def depositar(self, valor):
        # Valida se o valor do depósito é positivo
        if valor <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
            return False
        self.saldo += valor
        # Registra a transação no histórico
        self.historico_transacoes.append({
            'tipo': 'deposito',
            'valor': valor,
            'data': datetime.datetime.now()
        })
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        return True

    def sacar(self, valor):
        # Valida se o valor do saque é positivo
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
            return False
        # Valida se há saldo suficiente
        if valor > self.saldo:
            print("Erro: Saldo insuficiente.")
            return False

        # Limite de saque por operação (exemplo: R$ 500.00)
        if valor > 500.00:
            print("Erro: O valor máximo para saque por operação é R$ 500.00.")
            return False

        # Limite de saque diário (exemplo: R$ 1000.00)
        hoje = datetime.date.today()
        # Reseta o total de saque diário se a data for diferente
        if self.ultima_data_saque != hoje:
            self.saque_diario_total = 0.0
            self.ultima_data_saque = hoje

        # Verifica se o saque excede o limite diário
        if (self.saque_diario_total + valor) > 1000.00:
            print(f"Erro: Limite de saque diário excedido. Você já sacou R${self.saque_diario_total:.2f} hoje. Limite diário: R$ 1000.00.")
            return False

        self.saldo -= valor
        self.saque_diario_total += valor
        # Registra a transação no histórico
        self.historico_transacoes.append({
            'tipo': 'saque',
            'valor': valor,
            'data': datetime.datetime.now()
        })
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
        return True

    def extrato(self):
        print("\n--- EXTRATO BANCÁRIO ---")
        print(f"Conta: {self.numero_conta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo Atual: R${self.saldo:.2f}")
        print("\nHistórico de Transações:")
        # Exibe o histórico de transações ou mensagem se não houver transações
        if not self.historico_transacoes:
            print("Nenhuma transação realizada ainda.")
        else:
            for transacao in self.historico_transacoes:
                data_formatada = transacao['data'].strftime('%d/%m/%Y %H:%M:%S')
                print(f"  [{data_formatada}] {transacao['tipo'].capitalize()}: R${transacao['valor']:.2f}")
        print("------------------------\n")

def exibir_menu():
    print("\n--- MENU BANCÁRIO ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    print("---------------------")

def main():
    # Cria uma instância da conta bancária
    conta = ContaBancaria("12345-6", "João Silva")

    # Loop principal da interface de comando
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")
        elif opcao == '2':
            try:
                valor = float(input("Digite o valor para saque: "))
                conta.sacar(valor)
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Saindo do sistema bancário. Obrigado!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()


