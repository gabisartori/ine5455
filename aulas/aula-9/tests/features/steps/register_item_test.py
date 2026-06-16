from behave import *
from mercado_leilao import MercadoLeilao
from produto import Produto
from lance import Lance


@given(u'o cadastro do usuario Ernani Cesar foi realizado')
def step_impl(context):
  context.mercado = MercadoLeilao()
  context.mercado.cadastra_usuario("Ernani Cesar", "Campus Universitario", "ernani.santos@posgrad.ufsc.br", "055.761.919-00")

@given(u'o nome do produto sofa')
def step_impl(context):
  context.produto_nome = "sofa"

@given(u'a descricao do produto amarelo')
def step_impl(context):
  context.produto_descricao = "amarelo"

@given(u'e o lance 100')
def step_impl(context):
  context.lance_valor = 100


@given(u'e o cpf do leiloador 055.761.919-00')
def step_impl(context):
  context.lance_dono = "055.761.919-00"


@when(u'cadastrar o produto')
def step_impl(context):
  try:
    context.mercado.cadastra_produto(
      context.produto_nome,
      context.produto_descricao,
      context.lance_valor,
      context.lance_dono,
      1111
    )
    context.mensagem = "Produto cadastrado com sucesso"
  except Exception as e:
    context.mensagem = str(e)


@then(u'o sistema cadastra com sucesso')
def step_impl(context):
  assert context.mercado.existe_produto("sofa")


@given(u'sofa amarelo ja foi cadastrado')
def step_impl(context):
  context.mercado = MercadoLeilao()
  context.mercado.cadastra_usuario("Ernani Cesar", "Campus Universitario", "ernani.santos@posgrad.ufsc.br", "055.761.919-00")
  context.produto = Produto("sofa", "amarelo")
  context.lance_inicial = Lance(100, "055.761.919-00")
  context.mercado.cadastra_produto(
    context.produto.nome,
    context.produto.descricao,
    context.lance_inicial .valor,
    context.lance_inicial .dono,
    1111
  )


@then(u'o sistema mostra a mensagem O produto ja existe ou o leiloador nao esta cadastrado.')
def step_impl(context):
  assert context.mensagem == "O produto ja existe ou o leiloador nao esta cadastrado."