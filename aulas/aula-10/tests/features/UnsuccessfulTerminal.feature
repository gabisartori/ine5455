Feature: SC_AAA_BBB Unsuccessful Termination
Background:
Given o contrato foi criado
  And o cliente AAA consultoria empresarial LTDA
  And o fornecedor BBB TECNOLOGIA LTDA
  And Tarefa retirar os 3 cards da tela inicial
  And Tarefa adptar o aplicativo
  And Tarefa definir quais informações dinâmicas serão carregadas no aplicativo
  And o contrato foi ativado

Scenario: Unsuccessful termination #1 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
  And Tarefa retirar os 3 cards da tela inicial não está completa
When o contrato foi fechado
Then o estado do contrato é "Encerrado sem Sucesso"

Scenario: Unsuccessful termination #2 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
  And Tarefa adptar o aplicativo não está completa
When o contrato foi fechado
Then o estado do contrato é "Encerrado sem Sucesso"

Scenario: Unsuccessful termination #3 of SC_AAA_BBB contract
Given as informações do contrato estão definidas
  And Tarefa definir quais informações dinâmicas serão carregadas no aplicativo não está completa
When o contrato foi fechado
Then o estado do contrato é "Encerrado sem Sucesso"
