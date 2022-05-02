from src.conta.conta import Conta
from src.conta.conta_poupanca import ContaPoupanca


class CriarPoupanca:
    if __name__ == '__main__':

        poupanca = ContaPoupanca("21.342-7")
        poupanca.creditar(500.87)
        poupanca.debitar(45.00)
        print(poupanca.get_saldo())
        poupanca.render_juros(0.01)
        print(poupanca.get_saldo())

