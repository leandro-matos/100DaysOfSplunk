
### Criação e Uso de Workflow Actions
* Crie uma ação de Workflow Action (GET, POST e Search)

### Conceito:
* Executar Workflow Actions de um evento em seus resultados de pesquisa para interagir com recursos externos ou executar outra pesquisa
    - GET - recuperar informações de um recurso externo
    - POST - enviar valores de campo para um recurso externo
    - Pesquisa - use os valores dos campos para realizar uma pesquisa secundária

### Criando um Workflow Action do tipo GET
* Settings > Fields > Workflow Actions > New Workflow Action
    1. Selecione o aplicativo
    2. Nomeie o Workflow Action sem espaços ou caracteres especiais
    3. Defina o label, que aparecerá no menu Ação do evento
    4. Determine se sua Workflow Action se aplica a um campo ou tipo de evento
    5. Na lista escolhe Show Action, depois selecione o menu Evento
    6. Depois selecione o link
    7. Insira o URI para onde o usuário será direcionado
    8. Especifique se o link deve ser aberto em uma nova janela ou janela atual
    9. Selecione o método Link para obter
    10. Salvar
    11. Para testar basta executar a consulta e procurar dentro do evento pelo nome dado ao Workflow Action

### Criando um Workflow Action do tipo POST
* Settings > Fields > Workflow Actions > New Workflow Action
    - Conclua as etapas 1 a 6 conforme descrito no exemplo anterior, Criando uma ação de fluxo de trabalho GET
    7. Insira o URI para onde o usuário será direcionado
    8. Abra o link em uma nova janela ou janela atual
    9. Selecione o método Link de postagem
    10. Forneça parâmetros de pós-argumento
    11. Salvar

### Criando um Workflow Action do tipo SEARCH
* Settings > Fields > Workflow Actions > New
    - Conclua as etapas 1 a 5 conforme descrito no exemplo anterior, Criando uma ação de fluxo de trabalho GET
    6. Na lista suspensa Tipo de ação, selecione **search**
    7. Digite a string de pesquisa
    8. Selecione o aplicativo se for diferente do aplicativo atual
    9. Digite o nome da search onde a pesquisa será executada
    10. Indique se a pesquisa deve ser executada em uma nova janela ou na janela atual
    11. Insira o intervalo de tempo para a pesquisa ou escolha usar o mesmo intervalo de tempo da pesquisa
    12. Salvar
    13. Para testar basta executar a consulta e procurar dentro do evento pelo nome dado ao Workflow Action, será redirecionado para a search.

