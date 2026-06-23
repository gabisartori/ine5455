Feature: SC_AAA_BBB Unsuccessful Termination
Background:
Given o contrato foi criado
  And o cliente AAA consultoria empresarial LTDA
  And o fornecedor BBB TECNOLOGIA LTDA
  And data de criação 1
  And obrigação da contratada Prestar os serviços contratados
  And obrigação da contratada Enviar fatura e relatório das horas prestadas
  And obrigação do contratante Indicar um colaborador responsável pelos contato
  And obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido na assinatura do contrato
  And obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido trinta dias após o início dos trabalhos
  And o contrato foi criado
  And o contrato foi ativado

Scenario: Unsuccessful termination #1 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato foi fechado
  And obrigação da contratada Prestar os serviços contratados não está completa
Then o estado do contrato é "Encerrado sem Sucesso"

Scenario: Unsuccessful termination #2 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato foi fechado
  And obrigação da contratada Enviar fatura e relatório das horas prestadas não está completa
Then o estado do contrato é "Encerrado sem Sucesso"

Scenario: Unsuccessful termination #3 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato foi fechado
  And obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido na assinatura do contrato não está completa
Then o estado do contrato é "Encerrado sem Sucesso"

Scenario: Unsuccessful termination #4 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato foi fechado
  And obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido trinta dias após o início dos trabalhos não está completa
Then o estado do contrato é "Encerrado sem Sucesso"
