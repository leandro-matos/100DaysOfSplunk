
## Criação de Field Aliases e Calculated Fields

### Field Aliases
* Uma maneira de normalizar os dados sobre qualquer campo padrão (host, source ou sourcetype)
* Vários aliases podem ser aplicados a um campo
* Aplicado após field extractions, antes de lookups
* Pode aplicar field aliases a lookups

### Exemplo Field Alias
* Vários sourcetypes contêm algum tipo de campo de nome de usuário
* Para tornar a correlação e pesquisa de dados mais fácil, normalize o campo de nome de usuário
* Settings > Fields > Field Aliases > New Field Alias
    1. Selecione o aplicativo associado ao field alias
    2. Insira um nome para o field alias
    3. Aplique o field alias a um campo padrão:
        • Host
        • Source
        • Sourcetype
    4. Insira o nome do campo existente e o novo alias
        Ex: Neste exemplo, um field alias usado para novos campos de "usuário" em vários sourcetypes
        Ex: Novo field alias necessário para cada sourcetype

### Testando the Field Alias
* Depois que o alias de campo for criado, execute uma pesquisa usando o novo field alias
* Quando você cria um field alias, o campo original não é afetado
* Ambos os campos aparecem nas listas Todos os Campos e Campos Interessantes, se aparecerem em pelo menos 20% dos eventos

### Field Aliases e Lookups
* Depois de definir seus field aliases, você pode referenciá-los em uma lookup

### O que é um Calculated Field?
* Atalho para realizar transformações repetitivas, longas ou complexas usando o comando **eval**
* Deve ser baseado em um extracterd field
    Ex: **index=network | eval mb = sc_bytes(1024*1024) | stats sum(mb) as MegaBytes by usage**
    Nota: Os campos de saída de uma lookup ou campos/colunas gerados a partir de uma string de pesquisa não são suportados.

### Criando Calculated Field
* Settings > Fields > Calculated Fields > New Calculated Field
    1. Selecione o app que usará o calculated field
    2. Selecione host, source ou sourcetype para aplicar aos calculated fields e especifique o nome relacionado
    3. Definir o nome e a expressão (eval)
    4. Depois de criar um calculated field, você pode usá-lo em uma pesquisa como qualquer outro extractec field