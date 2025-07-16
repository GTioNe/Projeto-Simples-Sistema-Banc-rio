Sistema Bancário Simples em Python

Este é um sistema bancário simples desenvolvido em Python, que permite aos usuários realizar operações básicas como depósito, saque e visualização de extrato. O sistema inclui verificações de segurança para saques e mantém um histórico de todas as transações.

Funcionalidades

•
Depósito: Adiciona fundos à conta. Valida que o valor do depósito seja positivo.

•
Saque: Retira fundos da conta. Inclui as seguintes verificações de segurança:

•
Saldo suficiente.

•
Limite máximo de R$ 500,00 por operação.

•
Limite máximo de R$ 1000,00 por dia.



•
Extrato: Exibe o saldo atual da conta e um histórico detalhado de todas as transações (depósitos e saques), com data e hora.

Como Executar

1.
Pré-requisitos: Certifique-se de ter o Python 3 instalado em seu sistema.

2.
Download: Baixe o arquivo main.py para o seu computador.

3.
Execução: Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo main.py e execute o seguinte comando:

4.
Interação: Siga as instruções no menu interativo para realizar as operações bancárias.

Estrutura do Código

O sistema é composto por uma classe principal ContaBancaria que gerencia o saldo, o histórico de transações e as regras de negócio para depósito e saque. A interface de usuário é baseada em texto, com um menu simples para interação.

Exemplo de Uso

Plain Text


--- MENU BANCÁRIO ---
1. Depositar
2. Sacar
3. Extrato
4. Sair
---------------------
Escolha uma opção: 1
Digite o valor para depósito: 1000
Depósito de R$1000.00 realizado com sucesso.
--- MENU BANCÁRIO ---
1. Depositar
2. Sacar
3. Extrato
4. Sair
---------------------
Escolha uma opção: 2
Digite o valor para saque: 200
Saque de R$200.00 realizado com sucesso.
--- MENU BANCÁRIO ---
1. Depositar
2. Sacar
3. Extrato
4. Sair
---------------------
Escolha uma opção: 3
--- EXTRATO BANCÁRIO ---
Conta: 12345-6
Titular: João Silva
Saldo Atual: R$800.00
Histórico de Transações:
  [DD/MM/AAAA HH:MM:SS] Deposito: R$1000.00
  [DD/MM/AAAA HH:MM:SS] Saque: R$200.00
------------------------
