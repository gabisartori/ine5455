Feature: SC_AAA_BBB Unsuccessful Termination
Background:
Given o contrato foi criado
  And o cliente AAA consultoria empresarial LTDA
  And o fornecedor BBB TECNOLOGIA LTDA
  And data de criação 1
  And I have created and deployed the smart contract
  And obrigação da contratada Prestar os serviços contratados
  And obrigação da contratada Enviar fatura e relatório das horas prestadas
  And obrigação do contratante Indicar um colaborador responsável pelos contato
  And obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido na assinatura do contrato
  And obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido trinta dias após o início dos trabalhos
  And I activate the smart contract

Scenario: Unsuccessful termination #1 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato foi fechado
  And não está completa obrigação da contratada Prestar os serviços contratados
Then o estado do contrato é "Encerrado sem Sucesso"

Scenario: Unsuccessful termination #2 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato foi fechado
  And não está completa obrigação da contratada Enviar fatura e relatório das horas prestadas
Then o estado do contrato é "Encerrado sem Sucesso"

Scenario: Unsuccessful termination #3 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato foi fechado
  And não está completa obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido na assinatura do contrato
Then o estado do contrato é "Encerrado sem Sucesso"

Scenario: Unsuccessful termination #4 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato foi fechado
  And não está completa obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido trinta dias após o início dos trabalhos
Then o estado do contrato é "Encerrado sem Sucesso"
