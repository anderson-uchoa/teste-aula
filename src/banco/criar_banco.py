from src.banco.banco_lista import BancoLista
from src.conta.conta import Conta


class CriarBanco:
    if __name__ == '__main__':
        conta_origem = Conta("21.342-7")
        conta_destino = Conta("21.342-8")

        banco = BancoLista()

        banco.cadastrar(conta_origem)
        banco.cadastrar(conta_destino)

        banco.creditar(conta_origem.get_numero(), 550.50)
        banco.creditar(conta_destino.get_numero(), 50.50)

        banco.transferir(conta_origem.get_numero(), conta_destino.get_numero(), 500.00)

        print(banco.saldo(conta_origem.get_numero()))
        print(banco.saldo(conta_destino.get_numero()))
