Feature: SC_AAA_BBB Creation
Background:
Given o cliente AAA consultoria empresarial LTDA
  And o fornecedor BBB TECNOLOGIA LTDA
  And data de criação 1
  And I have created and deployed the smart contract
  And obrigação da contratada Prestar os serviços contratados
  And obrigação da contratada Enviar fatura e relatório das horas prestadas
  And obrigação do contratante Indicar um colaborador responsável pelos contato
  And obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido na assinatura do contrato
  And obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido trinta dias após o início dos trabalhos

Scenario: Create the SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato foi criado
Then o estado do contrado é "Criado"
  And o contrato não está ativado 

Scenario: Activate the SC_AAA_BBB contract
Given I have created and deployed the smart contract
When I activate the smart contract
Then o estado do contrato é "Ativado"
  And todas as tarefas do contrato estão ativadas
