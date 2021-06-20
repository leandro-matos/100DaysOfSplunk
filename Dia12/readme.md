
### Criação e gerenciamento de Fields
    * Revisando Field Extractor (FX):
        – Regex
        – Delimiter
    * Identifique as diferentes opções para chegar ao extrator de campo
        – Settings
        – Fields sidebar
        – Event actions
    * Revise o processo de extração de campos manualmente usando expressões regulares
    * Use o Field Extraction Manager para modificar os campos extraídos


### Field Auto-Extraction
* O Splunk descobre automaticamente muitos campos com base nos sourcetypes e pares de chave/valor encontrados nos dados
* Antes do momento da pesquisa, alguns campos já estão armazenados com o evento no índice
    - Metacampos, como host, source e sourcetype
    - Campos internos como _time e _raw
* No momento da pesquisa, a descoberta de campo descobre campos diretamente relacionados aos resultados da pesquisa
* O Splunk também pode extrair outros campos de dados de eventos brutos que não estão diretamente relacionados à pesquisa


### Performing Field Extractions
* Além dos muitos campos de extração automática do Splunk, você também pode extrair seus próprios campos com o Field Extractor (FX)
* Use FX para extrair campos que são estáticos e que você usa frequentemente em pesquisas
    - UI gráfica
    - Extraia campos de eventos usando regex ou delimiter
    - Os campos extraídos persistem como knowledge objects
    - Pode ser compartilhado e reutilizado em várias pesquisas
* Acesse o FX por meio de Settings, Fields Sidebar or Event Actions Menu

### Field Extraction
* Regex
    - Use esta opção quando o seu evento contiver dados não estruturados, como um arquivo de log do sistema
    - FX tenta extrair campos usando uma expressão regular que corresponde a eventos semelhantes
* Delimiter
    - Use esta opção quando o seu evento contiver dados estruturados como um arquivo .csv
    - Os dados não têm cabeçalhos e os campos devem ser separados por delimitadores (espaços, vírgulas, barras verticais, tabulações, etc)

### Field Extraction Workflows - Regex from Settings
* Settings -> Fields -> Field Extractions -> Open Field Extractor
    - 1. Selecionar o Data Type
        - sourcetype
        - source
    - 2. Selecionar o SourceType
    - 3. Selecione um evento de amostra clicando nele e clicar em próximo
    - 5. Selectionar Expressão Regular e clicar em Próximo
    - 6. Selecione o(s) valor(es) que deseja extrair.
    - 7. Forneça um nome de campo
    - 8. Clicar em Add Extraction
    - 9. Visualize os eventos de amostra e clicar em próximo
    - 10. Valide se os valores de campo adequados são extraídos e clique em Avançar
    - 11. Revise o nome dos campos recém-extraídos e defina as permissões e clique em Finish
        - Ex: Um nome de extração é fornecido por padrão. No entanto, esse nome pode ser alterado.

### Editando Regex for Field Extractions
    - 1. Em Select Method, clique em Regular Expression, Next
    - 2. Selectionr o campo para extração
    - 3. Providenciar o nome do campo e clicar em Add Extraction
    - 4. Clicar em Mostrar Expressão Regular e depois em Editar a Expressão Regular
    - 5. Atualizar a expressão regular e clicar em salvar
        - Ex: Depois de editar a expressão regular, você não pode voltar para a Field Extractor UI.
    - 6. Revisar o nome e setar as permissões e clicar em finalizar

### Delimited Field Extractions
* Use extrações de campos delimitados quando o registro de eventos não tiver um cabeçalho e os campos forem separados por espaços, vírgulas ou caracteres
* Settings, Fields Sidebar, Event Actions

### Delimited Field Extractions from Settings
* Settings -> Fields -> Field Extractions -> Open Field Extractor
    - 1. Selecionar o Data Type
        - sourcetype
        - source
    - 2. Selecionar o SourceType
    - 3. Selecione um evento de amostra clicando nele e clicar em próximo
    - 5. Selectionar Delimiters e clicar em Próximo
    - 6. Selecione o Delimitador usado em seu evento
    - 8. Clique no ícone ao lado do nome do campo padrão
    - 9. Insira um novo nome de campo e clicar em Rename Field e Next
    - 10. Confirmar o nome da extração e clicar em Finish