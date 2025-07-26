# banker_sistem_3
# 💰 Sistema Bancário em Python

Este projeto é um **sistema bancário simples**, desenvolvido em Python, que simula operações bancárias como criação de usuários, contas, depósitos, saques e exibição de extratos.

## 📋 Funcionalidades

- Criar usuários (Pessoa Física)
- Criar contas bancárias (Conta Corrente)
- Realizar **depósitos** e **saques**
- Emitir **extrato de transações**
- Limites de saque diários configuráveis
- Histórico completo das transações realizadas

## 🛠️ Tecnologias utilizadas

- Python 3.x
- Programação orientada a objetos (POO)
- `abc` (Abstract Base Classes)
- Módulo `datetime` para registrar data/hora das transações
- `textwrap` (para formatação de texto no terminal)

## 📁 Estrutura do Código

- `Cliente`: Classe base para representar um cliente genérico.
- `PessoaFisica`: Herda de `Cliente`, representa um usuário com CPF.
- `Conta`: Classe base com métodos para saque e depósito.
- `ContaCorrente`: Herda de `Conta`, com limites de saque e número de saques diários.
- `Transacao`: Classe abstrata para operações financeiras.
- `Saque` e `Deposito`: Herdam de `Transacao` e implementam a lógica de cada operação.
- `Historico`: Armazena o histórico de transações por conta.

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado:
    ```bash
    python --version
    ```

2. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/sistema-bancario-python.git
    cd sistema-bancario-python
    ```

3. Execute o script:
    ```bash
    python sistema_bancario.py
    ```

4. Utilize o menu para interagir com o sistema:

    ```
    ===Menu===
    1 - EXTRATO
    2 - DEPÓSITO
    3 - SAQUE
    4 - CRIAR USUÁRIO
    5 - CRIAR CONTA
    6 - LISTAR CONTAS
    7 - SAIR
    ========================
    ```

## ⚠️ Observações

- Cada usuário pode ter múltiplas contas.
- O limite padrão de saque é de R$ 500, com 3 saques por dia.
- O sistema não salva os dados entre execuções (sem persistência em arquivo ou banco de dados).



## 👨‍💻 Autor

Desenvolvido por Thiago Pereira do Vale  
📧 Email: [thiagovallyfinances@outlook.com](mailto:thiagovallyfinances@outlook.com)  
💼 LinkedIn: [thiagovally](https://www.linkedin.com/in/thiagovally)
