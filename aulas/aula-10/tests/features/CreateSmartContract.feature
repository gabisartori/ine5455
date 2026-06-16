Feature: SC_AAA_BBB Creation
Background:
Given o contrato foi criado
  And o cliente AAA consultoria empresarial LTDA
  And o fornecedor BBB TECNOLOGIA LTDA

Scenario: Create the SC_AAA_BBB contract
Given escopo do contrato aplicativo
  And Tarefa retirar os 3 cards da tela inicial
  And Tarefa adptar o aplicativo para carregar conforme o cadastro da empresa do usuário logado
  And Tarefa definir quais informações dinâmicas serão carregadas no aplicativo, por exemplo, labels, cores e outros. Apontas no aplicativo onde deve ser alterado
  And Requisito Backend do app utiliza Go como linguagem de programação, como será necessário criar um endpoint para retornar as informações dinâmicas da base de dados, pode ocorrer algum empecilho devido à falta de conhecimento da linguagem.
  And escopo portal empresa
  And Tarefa criar CRUD para salvar informações administrativas para apresentar no aplicativo
  And Tarefa Definir quais informações serão salvas nesta tela
When o contrato é 
Then <assure that the contract is correctly initialized and not activated>

Scenario: Activate the SC_AAA_BBB contract
Given <all information about the smart contract>
And <the contract is created>
When <the contract is activated>
Then <assure that the contract is correctly initialized and activated>
