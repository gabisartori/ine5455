from behave import *
from unittest import TestCase

from solcx import compile_standard, install_solc
import json
from web3 import Web3

address = "0xb9BED692c281fD4C58A1D404c83A43Cfc82a9FD1"
private_key = "0xf1448606ead1e4b5c2ff86954b000db30cc0983b98291abfba0a1df14325a139"

smart_contract = None
w3 = None
chain_id = 1337


def __deploy_contract(client, supplier, creation_date):
    global smart_contract
    global w3

    # Endereço do diretório onde está o smart contract AAABBBContract
    with open("src/resources/ClientContractorContract.sol", "r") as file:
        smart_contract_file = file.read()
    _solc_version = "0.8.0"
    install_solc(_solc_version)
    # Considerando o smart contract ProductSaleContract
    compiled_sol = compile_standard({"language": "Solidity", "sources": {"ClientContractorContract.sol": {"content": smart_contract_file}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]} } }, }, solc_version=_solc_version,)
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
    bytecode = compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["evm"]["bytecode"]["object"]
    abi = json.loads(compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["metadata"])["output"]["abi"]
    # Rodando o ganache localmente...
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    smart_contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.get_transaction_count(address)
    # Parâmetros do construtor do smart contract
    transaction = smart_contract.constructor(client, supplier, creation_date).build_transaction(
        {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    # Referência para o smart contract
    smart_contract = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)


@given(u'o cliente {client}')
def step_impl(context, client):
    context.client = "AAA"


@given(u'o fornecedor {supplier}')
def step_impl(context, supplier):
    context.supplier = supplier


@given(u'data de criação {date}')
def step_impl(context, date):
    context.creation_date = int(date)

@given(u'I have created and deployed the smart contract')
def step_impl(context):
    __deploy_contract(context.client, context.supplier, context.creation_date)


@when(u'I activate the smart contract')
def step_impl(context):
    transaction = smart_contract.functions.activate().build_transaction({"chainId": chain_id,
                                                                         "gasPrice": w3.eth.gas_price,
                                                                         "from": address,
                                                                         "nonce": w3.eth.get_transaction_count(address)})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    

@then(u'the smart contract is activated')
def step_impl(context):
    status = smart_contract.functions.getStatus().call()
    TestCase.assertEqual(TestCase(), 1, status)  # Status.InEffect = 1


@then(u'creation date is {date}')
def step_impl(context, date):
    TestCase.assertEqual(TestCase(), int(date), smart_contract.functions.getCreationDate().call())

@given(u'obrigação {obligation}')
def step_impl(context, obligation):
    smart_contract.functions.add_obligation(obligation)

@when(u'está completa obrigação {obligation}')
def step_impl(context, obligation):
    smart_contract.functions.set_obligation_as_complete(obligation)

@when(u'não está completa obrigação {obligation}')
def step_impl(context, obligation):
    pass

@when(u'o contrato foi criado')
def step_impl(context):
    pass

@given(u'o contrato foi criado')
def step_impl(context):
    pass

@given(u'as informações do contrato estão definidas')
def step_impl(context):
    pass


@when(u'I have created and deployed the smart contract')
def step_impl(context):
    __deploy_contract(context.client, context.supplier, context.creation_date)

@then(u'o estado do contrado é "Criado"')
def step_impl(context):
    assert smart_contract.functions.is_created()


@then(u'o contrato não está ativado')
def step_impl(context):
    assert not smart_contract.functions.is_in_effect()


@then(u'o estado do contrato é "Ativado"')
def step_impl(context):
    assert smart_contract.functions.is_in_effect()


@then(u'todas as tarefas do contrato estão ativadas')
def step_impl(context):
    for status in smart_contract.obligation_status:
        print(status)


@given(u'I activate the smart contract')
def step_impl(context):
    transaction = smart_contract.functions.activate().build_transaction({"chainId": chain_id,
                                                                         "gasPrice": w3.eth.gas_price,
                                                                         "from": address,
                                                                         "nonce": w3.eth.get_transaction_count(address)})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)


@when(u'o contrato foi fechado')
def step_impl(context):
    smart_contract.functions.close()


@then(u'o estado do contrato é "Encerrado com Sucesso"')
def step_impl(context):
    assert smart_contract.functions.is_successful()


@then(u'o estado do contrato é "Encerrado sem Sucesso"')
def step_impl(context):
    assert smart_contract.functions.is_unsuccessful()