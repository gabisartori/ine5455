Feature: SC_AAA_BBB Successful Termination

Scenario: Successful termination #1 of SC_AAA_BBB contract
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
  And I activate the smart contract
When o contrato foi fechado
  And está completa obrigação da contratada Prestar os serviços contratados
  And está completa obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido na assinatura do contrato
  And está completa obrigação do contratante Realizar o pagamento de 50% do serviço desenvolvido trinta dias após o início dos trabalhos
Then o estado do contrato é "Encerrado com Sucesso"
  
