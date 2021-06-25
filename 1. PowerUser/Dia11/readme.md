
### Introdução aos objetos de conhecimento
    * Identificar as categorias de objetos de conhecimento
    * Definir o papel de um gerente de conhecimento
    * Identificar convenções de nomenclatura
    * Permissões de revisão
    * Gerenciar objetos de conhecimento
    * Descrever o Splunk Common Information Model (CIM)

### O que é Knowledge Objects ?
    * Knowledge Objects são ferramentas que você usa para descobrir e analisar vários aspectos de seus dados
        - Interpretação de dados - Fields, field extractions
        - Classificação de dados - Event Types
        - Enriquecimento de dados - Lookups e workflow actions
        - Normalização - Tags, field aliases
        - Conjuntos de dados - Data Models
    * Shareable:
        - Pode ser compartilhado entre usuários
    * Reusable:
        - Objetos persistentes que podem ser usados ​​por várias pessoas ou aplicativos, como macros e relatórios
    * Searchable:
        - Uma vez que os objetos são persistentes, eles podem ser usados ​​em uma pesquisa


### O que é Knowledge Manager ?
    * Supervisiona a criação e o uso de objetos de conhecimento para um grupo ou implantação
    * Normaliza os dados do evento
    * Cria data models para Pivot Users


### Definindo Convenções de Nomenclatura
    * uso de uma convenção de nomenclatura em seu ambiente de produção é recomendado. Por exemplo:
        – Grupo: Corresponde ao (s) grupo (s) de trabalho do usuário salvando o objeto (exemplos: SEG. NEG. OPS. NOC)
        – Tipo de objeto: indica o tipo de objeto (alerta, relatório, resumo-índice-preenchimento) (exemplos: Alerta, Relatório, Resumo)
        – Descrição: Uma descrição significativa do contexto e da intenção da pesquisa, limitada a uma ou duas palavras, se possível;
        - Então, por exemplo: **SEG_Alert_WinEventlogFailures**

### Revendo Permissões:
    * Private 
        - Descrição: Apenas a pessoa que criou o objeto pode usá-lo e editá-lo. 
        - Criação: User Power Admin 
        - Read: Pessoa que o criou, Admin 
        - Write: Pessoa que o criou, Admin

    * This app only 
        - Descrição: Objeto persiste no contexto de um aplicativo específico 
        - Create: Power Admin 
        - Read: User* Power* Admin
        - Write: User* Power* Admin

    * All apps
        - O objeto persiste globalmente em todos os aplicativos 
        - Create: User* Power* Admin 
        - Write: User* Power* Admin
    
    * Permissão para ler e/ou escrever se o criador der permissão para essa função

    * Quando um objeto é criado, Exibir para é definido como **Owner** por padrão;
    * Quando as permissões do objeto são definidas para **App** ou **All apps**, todas as funções recebem permissão de leitura
        - A permissão de gravação é reservada para o administrador e o criador do objeto, a menos que o criador edite as permissões
    * Apenas a função de administrador pode promover um objeto para **All Apps**
        - Outras funções têm o botão **All Apps** esmaecido


### Gerenciando Knowledge Objects
    * Knowledge Objects são gerenciados centralmente em Seetings -> Knowledge
    * Sua função e permissões determinam sua capacidade de modificar as configurações de um objeto
    * Por padrão, os objetos de todos os proprietários são listados.


### Utilizando Splunk Common Information Model (CIM)
    * Metodologia para normalizar dados
    * Correlacione facilmente dados de diferentes fontes e tipos de fontes
    * Alavancagem para criar vários objetos, tais como field extractions, fields aliases, event types, tags
