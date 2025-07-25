from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def fazer_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nas, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nas = data_nas
        self.cpf = cpf


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            print("Operação não realizada! Saldo insuficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso.")
            return True
        else:
            print("Operação não realizada! Valor inválido.")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("Operação não realizada! Valor inválido.")
        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saques_realizados = len(
            [t for t in self.historico.transacoes if t["tipo"] == "Saque"]
        )
        if valor > self.limite:
            print("Operação não realizada! Limite de valor excedido.")
        elif saques_realizados >= self.limite_saques:
            print("Operação não realizada! Limite de saques excedido.")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f"Agência: {self.agencia}\nConta: {self.numero}\nTitular: {self.cliente.nome}"


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):



    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


def validar(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, Digite uma opçao válida.\ 033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[Usuario não digiteou opção. \033[m")
            return 0 
        else:
            return n 


def linha(tam = 10):
    return '===' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista):
    cabecalho("Menu")
    c = 1 
    for item in lista:
        print(f"{c} - {item}")
        c += 1 
    print(linha())
    opc = validar("Digite um Opção: ")
    return opc

def exibir_extrato(saldo, /, *, extrato):
    print(f"========== EXTRATO ============" )
    for moviento in extrato:
        print(moviento)
    print(f"Saldo Total ********* R$ {saldo}")

def recuperar_conta_usuario(clientes):
    if not cliente.conta:
        print("Cliente não encontrado")
        return

def depositar(clientes):
    cpf = input("Dgite o CPF do Cliente: ")
    cliente = filtrar_usuario(cpf, clientes)

    if not cliente:
        print("Cliente não Encontrado!!!")
        return
    valor = float(input("digite o valor a ser depositado: "))

    transacao = Deposito(valor)
    
    conta = recuperar_conta_usuario(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def saque():
    excedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("saldo insuficiente!!")
    elif execedeu_limite:
        print("Operação invalida você excedeu o limite de valor!!!")

    elif excedeu_saques:
        print("Excedeu o limite total de saques!!")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque ********** R$ {valor}")
        print("Saque realizado com sucesso")
    
    else:
        print("Operação invalida!! Digite um valor valido!!!")

    return saldo, extrato



def filtrar_usuario(cpf, usuarios):
        usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    cpf = input("Informe seu CPF(somente numero): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuario com esse CPF")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd - mm - aaaa:  ")
    endereço = input("Informe seu Endereço(Logradouro, Nº - Bairro - Cidade): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})

    print("Usuaro Criado com Sucesso!!!!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta Criada com Sucesso!!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, criação de conta encerrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\ 
        Agencia: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
    """
        
        print("=" * 42)
        print(linha)


while True:
    resposta = menu(["ExTRATO", "DEPÓSITO", "SAQUE", "CRIAR USUARIO", "CRIAR CONTA", "LISTAR CONTAS", "SAIR"])

    if resposta == 1:
        exibir_extrato(saldo, extrato=extrato)

    elif resposta == 2:
        valor = float(input("Digite o valor a ser depositado: R$ "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif resposta == 3:
        valor = float(input("Qual o valor do saque: R$ "))
        saque(saldo=saldo, valor=valor,extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)
    elif resposta == 4:
        criar_usuario(usuarios)
    
    elif resposta == 5 :
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
            
    elif resposta == 6:
        listar_contas(contas)
            
    
    elif resposta == 7:
        print("Sair do sistema")
        break
    else:
        print("digite uma opção valida")