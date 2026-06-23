Feature: SC_AAA_BBB Successful Termination

Scenario: Successful termination #1 of SC_AAA_BBB contract
Given o contrato foi criado
  And o cliente AAA consultoria empresarial LTDA
  And o fornecedor BBB TECNOLOGIA LTDA
  And Tarefa retirar os 3 cards da tela inicial
  And Tarefa adptar o aplicativo
  And Tarefa definir quais informações dinâmicas serão carregadas no aplicativo
  And o contrato foi criado
  And o contrato foi ativado
When o contrato foi fechado
Then o estado do contrato é "Encerrado com Sucesso"
  
