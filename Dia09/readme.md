
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
Ex: **index=network sourcetype=cisco_wsa_squid | stats sum(sc_bytes) as Bytes by usage**

* Os resultados da avaliação devem ser definidos para um campo novo ou existente
* Neste exemplo:
    - Calcule o número de bytes para cada tipo de uso
    - Crie um novo campo chamado
    - largura de banda
    - Converta os valores do campo Bytes em MB, dividindo os valores do campo Bytes por (1024 * 1024)
Ex: **index=network sourcetype=cisco_wsa_squid | stats sum(sc_bytes) as Bytes by usage | eval bandwidth = Bytes(1024*1024)**

* Os resultados da largura de banda são difíceis de ler com tantos pontos decimais
* a função round (campo/número, decimais) define o valor de um campo para o número de decimais que você especificar
* Neste exemplo:
    - Divida o valor do campo Bytes por (1024 * 1024)
    - Arredonde o resultado para duas casas decimais
* Se o número de decimais não for especificado, o resultado é um número inteiro
Ex: **index=network sourcetype=cisco_wsa_squid | status sum(sc_bytes) as Bytes by usage | eval bandwidth = round(Bytes(1024*1024),2) | sort - bandwidth | rename bandwidth as "BandWidth (MB)"**

* O campo "Largura de banda (MB)" contém os dados no formato desejado
* O campo Bytes não é mais necessário
    - O campo Bytes pode ser removido
Ex: **index=network sourcetype=cisco_wsa_squid | status sum(sc_bytes) as Bytes by usage | eval bandwidth = round(Bytes(1024*1024),2) | sort - bandwidth | rename bandwidth as "BandWidth (MB)" | fields -Bytes**

* Você pode executar funções matemáticas em campos com valores numéricos de campo
* Neste exemplo, o stats calculam o preço de lista total e o preço de venda total por product_name
* eval calcula a porcentagem de desconto e formata o campo de desconto
* Classificar lista os itens com maior desconto primeiro
* eval converte Desconto em uma string e concatena o caractere%
* rename fornece títulos fáceis de usar
Ex: **index=web sourcetype=access_combined product_name=* action=purchase | stats sum(price) as tp, sum(sale_price) as tsp by product_name | eval Discount = round(((tp - tsp)/ tp)*100) | sort -Discount | eval Discount = Discount."%" | rename tp as "Total List Price", tsp as "Total Sale Price", product_name as Product**

* tostring converte um valor de campo numérico em uma string **tostring (campo, "opção")**

* Opções:
    - "commas": aplica vírgulas
        - Se o número incluir decimais, ele será arredondado para duas casas decimais
    - "duration": formata o número como "hh: mm: ss"
    - "hex": formata o número em hexadecimal
Ex: 

