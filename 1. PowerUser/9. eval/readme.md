
### Use o comando eval para:
    - Faça cálculos
    - Converter valores
    - Valores redondos
    - Valores de formato
    - Use declarações condicionais

#### Use os comandos search e where para filtrar os resultados calculados
#### Use o comando fillnull

### eval Command – Overview
* eval permite calcular e manipular valores de campo em seu relatório
    - **eval fieldname1 = expression1 [, fieldname2 = expression2 ...]**
* Suporta uma variedade de funções
* Os resultados do eval são gravados em um campo novo ou existente que você especificar
    - Se o campo de destino existe, os valores do campo são substituídos pelos resultados da avaliação
    - Os dados indexados não são modificados e nenhum dado novo é gravado no índice
    - Os valores dos campos são tratados diferenciando maiúsculas de minúsculas

* O comando eval permite que você:
    - Calcular expressões
    - Coloque os resultados em um campo
    - Use esse campo em pesquisas ou outras expressões

* Operadores de tipo Aritmética: + - * /% 
* Concatenação: +.
* Booleano: AND OR NOT XOR
* Comparação: <> <=> =! = = == LIKE

Mais Informações: http://docs.splunk.com/Documenta tion/Splunk/latest/SearchReferenc e/CommonEvalFunctions

* Este relatório de exemplo exibe a soma dos bytes usados ​​para cada categoria de uso
* É difícil determinar quanta largura de banda está sendo usada olhando para bytes
* Primeiro, use eval para converter o valor de bytes em megabytes
    - Ex: **index=network sourcetype=cisco_wsa_squid | stats sum(sc_bytes) as Bytes by usage**

* Os resultados da avaliação devem ser definidos para um campo novo ou existente
* Neste exemplo:
    - Calcule o número de bytes para cada tipo de uso
    - Crie um novo campo chamado
    - largura de banda
    - Converta os valores do campo Bytes em MB, dividindo os valores do campo Bytes por (1024 * 1024)
    - Ex: **index=network sourcetype=cisco_wsa_squid | stats sum(sc_bytes) as Bytes by usage | eval bandwidth = Bytes(1024*1024)**

* Os resultados da largura de banda são difíceis de ler com tantos pontos decimais
* a função round (campo/número, decimais) define o valor de um campo para o número de decimais que você especificar
* Neste exemplo:
    - Divida o valor do campo Bytes por (1024 * 1024)
    - Arredonde o resultado para duas casas decimais
* Se o número de decimais não for especificado, o resultado é um número inteiro
    - Ex: **index=network sourcetype=cisco_wsa_squid | status sum(sc_bytes) as Bytes by usage | eval bandwidth = round(Bytes(1024*1024),2) | sort - bandwidth | rename bandwidth as "BandWidth (MB)"**

* O campo "Largura de banda (MB)" contém os dados no formato desejado
* O campo Bytes não é mais necessário
    - O campo Bytes pode ser removido
    - Ex: **index=network sourcetype=cisco_wsa_squid | status sum(sc_bytes) as Bytes by usage | eval bandwidth = round(Bytes(1024*1024),2) | sort - bandwidth | rename bandwidth as "BandWidth (MB)" | fields -Bytes**

* Você pode executar funções matemáticas em campos com valores numéricos de campo
* Neste exemplo, o stats calculam o preço de lista total e o preço de venda total por product_name
* eval calcula a porcentagem de desconto e formata o campo de desconto
* Classificar lista os itens com maior desconto primeiro
* eval converte Desconto em uma string e concatena o caractere%
* rename fornece títulos fáceis de usar
    - Ex: **index=web sourcetype=access_combined product_name=* action=purchase | stats sum(price) as tp, sum(sale_price) as tsp by product_name | eval Discount = round(((tp - tsp)/ tp)*100) | sort -Discount | eval Discount = Discount."%" | rename tp as "Total List Price", tsp as "Total Sale Price", product_name as Product**

### eval Command - tostring Function
* tostring converte um valor de campo numérico em uma string **tostring (campo, "opção")**

* Opções:
    - "commas": aplica vírgulas
        - Se o número incluir decimais, ele será arredondado para duas casas decimais
    - "duration": formata o número como "hh: mm: ss"
    - "hex": formata o número em hexadecimal
    - Ex: **index=web sourcetype=access_combined | stats count(price) as NumberOfLostSales, avg(price) as AverageLostSales, sum(price) as TotalLostRevenue | eval AverageLostSales = "$" + tostring(AverageLostSales, "commas"), TotalLostRevenue = "$" + tostring(TotalLostRevenue, "commas")**

* Este exemplo mostra "duration" opção de função **tostring**
    - stats calcula sessionTime para cada sessão (JSESSIONID)
    - Use a função de intervalo para retornar a diferença entre os valores máximos e mínimos de _time
    - Ex: **index=web sourcetype=access_combined | stats range(_time) as sessionTime by JSESSIONID | sort 5 -sessionTime | eval duration=tostring(sessionTime,"duration")**

### Formatando e Classificando Valores
* eval com caracteres adicionados converte valores de campos numéricos em strings
* Para ordenar numericamente, primeiro classifique e, em seguida, use eval:
    - Ex: **index=web price=* | stats values(price) as price by product_name | eval price = "$".price | sort -price**
    - Ex: **index=web price=* | stats values(price) as price by product_name | sort -price | eval price = "$".price**

### Comandos eval com múltiplas expressões
* Múltiplas expressões podem ser combinadas em um comando eval
* Cada expressão subsequente faz referência aos resultados de expressões anteriores
* As expressões devem ser separadas por vírgulas
    - Ex: **eval fieldname1 = expression1, fieldname2 = expression2, nomedocampo3 = expressão3 ...**
    - Ex: **index=web price=* | stats values(price) as list_price, values(sales_price) as current_sale_price by product_name | eval current_discount = round(list_price - current_sale_price)/list_price*100,2), new_discount = (current_discount - 5), new_sale_price = list_price - (list_price * new_discount/100))**

### Comando eval - sintaxe da função if
* if (X, Y, Z)
    - A função if leva três argumentos
    - O primeiro argumento, X, é uma expressão booleana
    - Se for TRUE, o resultado será avaliado como o segundo argumento, Y
    - Se for avaliado como FALSE, o resultado será avaliado como o terceiro argumento, Z
* Os valores não numéricos devem ser colocados entre "aspas duplas"
* Os valores dos campos são tratados diferenciando maiúsculas de minúsculas
    - Ex: **index=sales sourcetype=vendor_sales | eval SalesTerritory = if((VendorID  >=  7000  AND  VendorID  <  8000),  "Asia",  "Rest  of  the  World") | stats sum(price) as TotalRevenue by SalesTerritory | eval TotalRevenue = "$" + tostring(TotalRevenue, "commas")**

### Comando eval - função case
* case(X1,Y1,X2,Y2...)
    - O primeiro argumento, X1, é uma expressão booleana
    - Se for TRUE, o resultado será Y1
    - Se for FALSO, a próxima expressão booleana, X2, é avaliada, etc.
    - Se você quiser uma cláusula “de outra forma”, apenas teste uma condição que você sabe que é verdadeira no final (por exemplo, 0 = 0)
    - Ex: **index=web | eval rating=case(productId LIKE "WC%", "Teen", productId LIKE "FS%", Mature", 0=0, "Unrated")**
* Para contar o número de eventos que contêm um valor de campo específico, use as funções de contagem e avaliação
    - Usado em um comando de transformação, como estatísticas
    - Requer uma cláusula as
    - As aspas duplas são necessárias para os valores dos campos de caracteres
    - Os valores dos campos diferenciam maiúsculas de minúsculas
    - Ex: **index=security vendor_action=* | stats count(eval(vendor_action="Accepted")) as Accepted, count(eval(vendor_action="Failed)) as Failed**

### Filtrando resultados - search e where
* search
    - Pode ser mais fácil se você estiver familiarizado com a sintaxe de pesquisa básica
    - Trata os valores dos campos sem fazer distinção entre maiúsculas e minúsculas
    - Permite pesquisar por palavra-chave
    - Pode ser usado em qualquer ponto do pipeline de pesquisa
* where
    - Pode comparar valores de dois campos diferentes
    - Funções estão disponíveis, como **isnotnull()**
    - Trata valores de campo diferenciando maiúsculas de minúsculas
    - Não pode aparecer antes do primeiro tubo no pipeline de pesquisa

### Comando search
* Para filtrar os resultados, use search em qualquer ponto do pipeline de pesquisa
* Se comporta exatamente como as strings de pesquisa antes do primeiro tubo
    - Usa o caractere curinga "*"
    - Trata os valores dos campos sem fazer distinção entre maiúsculas e minúsculas
    Ex: **index=web status=200 | status(price) as sales by product_name | search sales>500 | sort -sales**

### Comando where
* Usa a mesma sintaxe de expressão do comando eval
* Usa expressões booleanas para filtrar os resultados da pesquisa e apenas mantém os resultados que são verdadeiros
* Strings entre aspas duplas são interpretadas como valores de campo
    - Trata valores de campo diferenciando maiúsculas de minúsculas
* Strings sem aspas ou entre aspas simples são tratadas como campos
    - Ex: **index=web | timechart count(eval(action="changequantity")) as changes, count(eval(action="remove")) as removals**

### Comando Where com operador like
* Pode fazer pesquisas curinga com onde comando
* Use (_) para um caractere e (%) para vários caracteres
* Deve usar o operador like com curingas
    - Ex: **index=security | stats count by src_ip | where src_ip like "10_.%"**

### Comando fillnull
* Use fillnull para substituir valores nulos em campos
* Use value=string para especificar uma string que você deseja exibir
    - Exemplo: fillnull value=NULL
* Se nenhum valor=cláusula, o valor de substituição padrão é 0
* Opcionalmente, restrinja a quais campos o fillnull se aplica, listando-os no final do comando
    - Exemplo: **index=sales | chart sum(price) over product_name by VendorCountry**
    - Exemplo: **index=sales | chart sum(price) over product_name by VendorCountry | fillnull value="No Value"**



