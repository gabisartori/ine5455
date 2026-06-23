Feature: SC_AAA_BBB Creation
Background:
Given o contrato foi criado
  And o cliente AAA consultoria empresarial LTDA
  And o fornecedor BBB TECNOLOGIA LTDA
  And escopo do contrato aplicativo
  And Tarefa retirar os 3 cards da tela inicial
  And Tarefa adptar o aplicativo para carregar conforme o cadastro da empresa do usuário logado
  And Tarefa definir quais informações dinâmicas serão carregadas no aplicativo, por exemplo, labels, cores e outros. Apontas no aplicativo onde deve ser alterado

Scenario: Create the SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato é criado
Then o estado do contrado é "Criado"
  And o contrato não está ativado 

Scenario: Activate the SC_AAA_BBB contract
Given as informações do contrato estão definidas
When o contrato é ativado
Then o estado do contrato é "Ativado"
  And todas as tarefas do contrato estão ativadas
