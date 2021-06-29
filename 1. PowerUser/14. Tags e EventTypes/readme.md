
## Trabalhando com tags e Event Types
    * Criar e usar tags
    * Descrever os event types e seus usos
    * Criar um event type

### Descrevendo Tags
    * Tags são como apelidos que você cria para pares de campo/value pairs
    * As tags tornam seus dados mais compreensíveis e menos ambíguos
    * Você pode criar uma ou mais tags para qualquer combinação de campo/valor
    * As tags diferenciam maiúsculas de minúsculas

### Ciando Tags
    * Para criar uma tag:
        * Clique na seta para detalhes do evento
        * Em Ações, clique na seta para baixo
        * Selecione Editar Tags
        * Nomeie as tags, separadas por **commas**
        * Quando pares de campo/value pairs são selecionados, as tags aparecem:
            - Nos resultados como tags
            - Entre parênteses ao lado do pares de campo/value pairs

### Utilizando e buscando Tags
    * Para usar tags em uma pesquisa, use a sintaxe: **tag=<nome da tag>** 
    * Para pesquisar uma tag associada a um valor: **tag=<tagname>**
    * Para pesquisar uma tag associada a um valor em um campo específico: **tag::<field>=<tagname>
    * Para pesquisar uma tag usando um valor de campo parcial, Utilizar wildcard: tag=p*

### Gerenciando Tags - Lista por Par de Valores de Campo
    * Settings > Tags > List by field value pair
    - Editar permissões
    - Desativar todas as tags para par - desativa a tag nas pesquisas e evita que ela seja listada em Listar por nome de tag e Todos os objetos de tag exclusivos

### Adicionando/Modificando o nome da Tag e Field Value Pair
    * Clique em **List by tag name** de campo para adicionar outra tag ou alterar o nome da tag
    * Clique em **List by tag name** de tag para adicionar ou editar o par de valores de campo para a tag

### Descrevendo Event Types
    * Um método de categorizar eventos com base em uma pesquisa
    * Um método útil para a captura e compartilhamento de conhecimento institucional
    * Pode ser marcado para agrupar tipos semelhantes de eventos

### Criação de um Event Type na página de pesquisa
    * Execute uma pesquisa e verifique se todos os resultados atendem aos critérios de tipo de evento
    * No menu Salvar como, selecione Tipo de evento
    * Forneça um nome para o seu event type (o nome não deve conter espaços)
    * Nos detalhes do evento, selecione Event Actions > Build Event Type
    * Refine os critérios para o seu tipo de evento, como:
        * Seqüência de pesquisa
        * Valores de campo
        * Tags
    * Verifique suas seleções e clique em Salvar

### Utilizando Event Types
    * Para verificar o event type, pesquise por **eventtype=web_error**
    * ‘eventtype’ é exibido na barra lateral Campos e pode ser adicionado como um campo selecionado
    * O Splunk avalia os eventos e aplica os tipos de eventos apropriados no momento da pesquisa
    * Usando a barra lateral de Campos, você pode visualizar facilmente os tipos de eventos individuais, o número de eventos e a porcentagem

### Identificando Event Types
    * Você pode marcar tipos de eventos de duas maneiras:
        - Settings > Event Types
        - Event details > Actions

### Event Types vs. Saved Reports
    * Event Types
        - Categorizar eventos com base em uma string de pesquisa
        - Identifique os event types para organizar os dados em categorias
        - O campo eventtype pode ser incluído em uma string de pesquisa
        - Não inclui um intervalo de tempo
    * Saved Reports
        - Os critérios de pesquisa não mudarão
        - Inclui um intervalo de tempo e formatação dos resultados
        - Pode ser compartilhado com usuários do Splunk e adicionado aos painéis