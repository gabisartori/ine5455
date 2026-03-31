import unittest
from sistema_bancario import *

class TestHelper():
    @staticmethod
    def create_ammount(ammount: int) -> Dinheiro:
        return Dinheiro(Moeda.BRL, 1500, 0)

    @staticmethod
    def create_valor_monetario_fracionado(quantia: int) -> ValorMonetario:
        return ValorMonetario(Moeda.BRL, quantia)

class TestCriacao(unittest.TestCase):
    def test_cria_100_reais_em_dinheiro(self):
        # Inline fixture setup
        moeda = Moeda.BRL
        # SUT Exercise
        cem_reais = Dinheiro(moeda, 100, 0)
        # Result Verification
        self.assertEqual(100, cem_reais.inteiro)
        # Fixture Teardown

    def test_cria_100_reais_em_valor_monetario(self):
        # Inline fixture setup
        moeda = Moeda.BRL
        valor_esperado = Dinheiro(moeda, 100, 0)
        # SUT Exercise
        dinheiro = ValorMonetario(moeda, 100*100)
        # Result Verification
        self.assertEqual(dinheiro.obter_quantia(), valor_esperado)
        # Fixture Teardown

    def test_cria_banco(self):
        # Inline Fixture Setup
        sistema = SistemaBancario()
        # SUT Exercise
        banco = sistema.criar_banco("Banco teste", Moeda.BRL)
        # Result Verification
        self.assertEqual(banco.nome, "Banco teste")
        self.assertEqual(banco.moeda, Moeda.BRL)

    def test_cria_agencia(self):
        # Inline Fixture Setup
        sistema = SistemaBancario()
        banco = sistema.criar_banco("Banco teste", Moeda.BRL)
        # SUT Exercise
        agencia = banco.criar_agencia("Agência teste")
        # Result Verification
        self.assertEqual(agencia.nome, "Agência teste")
        # Fixture Teardown

    def test_formatacao_moeda(self):
        # Inline Fixture Setup
        moeda = Moeda.BRL
        # SUT Exercise
        nome = moeda.simbolo()
        # Result Verification
        self.assertEqual(moeda.simbolo(), "R$")
        # Fixture Teardown

    def test_valor_monetario_com_fracao_suficiente_para_completar_unidades_parte_inteira(self):
        # Delegated Fixture Setup
        valor = TestHelper.create_valor_monetario_fracionado(1050).obter_quantia()
        # SUT Exercise
        parte_inteira = valor.inteiro
        # Result Verificaton
        self.assertEqual(parte_inteira, 10)
        # Fixture Teardown

    def test_valor_monetario_com_fracao_suficiente_para_completar_unidades_parte_fracionaria(self):
        # Delegated Fixture Setup
        valor = TestHelper.create_valor_monetario_fracionado(1050).obter_quantia()
        # SUT Exercise
        parte_fracionada = valor.fracionado
        # Result Verificaton
        self.assertEqual(parte_fracionada, 50)
        # Fixture Teardown

    def test_soma_entre_valores_monetarios(self):
        # Delegated Fixture Setup
        valor_1 = TestHelper.create_valor_monetario_fracionado(100)
        valor_2 = TestHelper.create_valor_monetario_fracionado(100).obter_quantia()
        # SUT Exercise
        soma = valor_1.somar(valor_2)
        # Result Verification
        self.assertEqual(soma.obter_quantia(), Dinheiro(Moeda.BRL, 2, 0))
        # Fixture Teardown

    def test_criar_transacao(self):
        # Inline Fixture Setup
        valor = Dinheiro(Moeda.BRL, 1500, 0)
        # SUT Exercise
        transaction = Entrada(valor)
        # Result Verificaton
        self.assertEqual(Dinheiro(Moeda.BRL, 1500, 0), transaction.obter_valor_monetario().obter_quantia())
        # Fixture Teardown

    def test_sinal_negativo_para_valor_monetario(self):
        # Inline Fixture Setup
        valor = ValorMonetario(Moeda.BRL, -1500*100)
        # SUT Exercise
        is_negative = valor.negativo()
        # Result Verification
        self.assertTrue(is_negative)
        # Fixture Teardown

    def test_formatacao_reais_valor_monetario(self):
        # Inline Fixture Setup
        valor = ValorMonetario(Moeda.BRL, 100)
        # SUT Exercise
        string = valor.formatado()
        # Result Verification
        self.assertEqual(string, "+1,00 BRL")
        # Fixture Teardown

    def test_formatacao_dolares_valor_monetario(self):
        # Inline Fixture Setup
        valor = ValorMonetario(Moeda.USD, 100)
        # SUT Exercise
        string = valor.formatado()
        # Result Verification
        self.assertEqual(string, "+1,00 USD")
        # Fixture Teardown

    def test_somar_moedas_diferentes_deve_dar_erro(self):
        # Inline Fixture Setup
        valor_real = ValorMonetario(Moeda.BRL, 100)
        valor_dolar = ValorMonetario(Moeda.USD, 100).obter_quantia()
        # SUT Exercise
        with self.assertRaises(Exception):
            valor_real.somar(valor_dolar)
        # Result Verification
        # Fixture Teardown

class TestTransactionsOnBanco1(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaBancario()
        self.banco_test = self.sistema.criar_banco("Banco do Brasil", Moeda.BRL)
        self.agencia_test = self.banco_test.criar_agencia("Trindade")
        self.account_test = self.agencia_test.criar_conta("Sofiascript")

    def test_conta_inicializada_com_saldo_zerado(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        valor_esperado = Dinheiro(Moeda.BRL, 0, 0)
        # SUT Exercise
        nova_conta = self.agencia_test.criar_conta("New user")
        # Result Verificaton
        self.assertEqual(nova_conta.calcular_saldo(), valor_esperado)
        # Fixture Teardown

    def test_conta_com_saldo_apos_receber_transacao(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        entrada = Entrada(Dinheiro(Moeda.BRL, 1500, 0))
        # SUT Exercise
        self.account_test.adicionar_transacao(entrada)
        # Result Verificaton
        self.assertEqual(self.account_test.calcular_saldo(), Dinheiro(Moeda.BRL, 1500, 0))
        # Fixture Teardown

    def test_sacar_em_conta_sem_saldo(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        quantia = Dinheiro(Moeda.BRL, 1500, 0)
        # SUT Exercise
        resultado = self.sistema.sacar(self.account_test, quantia)
        # Result Verificaton
        self.assertEqual(resultado.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)
        # Fixture Teardown

    def test_saldo_apos_deposito(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        valor = TestHelper.create_ammount(1500)
        # SUT Exercise
        self.sistema.depositar(self.account_test, valor)
        # Result Verificaton
        self.assertEqual(self.account_test.calcular_saldo(), Dinheiro(Moeda.BRL, 1500, 0))
        # Fixture Teardown

    def test_transferencia_valida(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        account_2 = self.agencia_test.criar_conta("Usuário 2")
        self.sistema.depositar(account_2, Dinheiro(Moeda.BRL, 1500, 0))
        # SUT Exercise
        self.sistema.transferir(account_2, self.account_test, Dinheiro(Moeda.BRL, 500, 0))
        # Result Verificaton
        self.assertEqual(self.account_test.calcular_saldo(), Dinheiro(Moeda.BRL, 500, 0))
        self.assertEqual(account_2.calcular_saldo(), Dinheiro(Moeda.BRL, 1000, 0))
        # Fixture Teardown

    def test_transferencia_invalida_saldo_insuficiente(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        account_2 = self.agencia_test.criar_conta("Usuário 2")
        self.sistema.depositar(account_2, Dinheiro(Moeda.BRL, 1500, 0))
        # SUT Exercise
        self.sistema.transferir(account_2, self.account_test, Dinheiro(Moeda.BRL, 5000, 0))
        # Result Verificaton
        self.assertEqual(self.account_test.calcular_saldo(), Dinheiro(Moeda.BRL, 0, 0))
        self.assertEqual(account_2.calcular_saldo(), Dinheiro(Moeda.BRL, 1500, 0))

    def test_transferencia_invalida_moeda_errada(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        account_2 = self.agencia_test.criar_conta("Usuário 2")
        self.sistema.depositar(account_2, Dinheiro(Moeda.BRL, 1500, 0))
        # SUT Exercise
        self.sistema.transferir(account_2, self.account_test, Dinheiro(Moeda.USD, 500, 0))
        # Result Verificaton
        self.assertEqual(self.account_test.calcular_saldo().obter_quantia(), Dinheiro(Moeda.BRL, 0, 0))
        self.assertEqual(account_2.calcular_saldo(), Dinheiro(Moeda.BRL, 1500, 0))

if __name__ == "__main__": unittest.main()
