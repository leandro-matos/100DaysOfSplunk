
## Aula 01 - Beyond Search Fundamentals

### Buckets
* A ingestão de dados é o processo usado para carregar os registros de dados de uma ou mais fontes a fim de importar esses dados para o Splunk. Os dados são armazenados em **Buckets*

Bucket's contêm uma série de:
* _raw data
* indexing data

Em suas configurações os buckets possuem alguns padrões, todos ajustados pelos usuários Admin.
* maximum size, maximum time span

Há 03 tipos de Buckets no Splunk
* Hot: Quando os eventos são indexados, eles são armazenados nos hot buckets. Quando atinge a sua capacidade máxima, os dados vão para os Warm Buckets, essa situação ocorre quando atingir o maximum size reached, Time Span reached e Indexer Restarted.
* Warm: Os dados permanecem guardados por alguns dias até a sua capacidade máxima ser atingida e ir para o status de cold.
* Cold: Dados são armazenados geralmente em locais distintos dos outros dois.

Quanto melhor a política de bucket's determinada, a search será mais eficiente e não terá problemas de performance. Pois quanto mais antigo o dado a ser buscado, mais à fundo a pesquisa será realizada nos buckets

### Wildcards
* No começo da string causam problemas de performance na query. Ex: *ailed OR *assword
* No meio da String pode causar problemas de inconsistência de resultados: Ex: fa*led
* O mais importante é ser o mais específico possível para fazer as querys, com isso os resultados serão mais eficientes.

### Search Mode
FastMode: Retorna apenas os dados essenciais, é exibido apenas os campos essenciais. Com isso é uma consulta bem rápida.
VerboseMode: Retorna todos os campos e eventos de dado. Com isso é uma consulta bem mais lenta.
SmartMode: Retorna os melhores resultados da combinação dos dois modos anteriores

### General Best Practices
* Quanto menor o tempo de pesquisa maior a sua eficiência;
* Default fields no indexer: time, index, source, host, sourcetype. Esses campos devem ser utilizados o máximo possível nos filtros
* FastMode para performance, VerboseMode para coisas complexas, SmartMode para combinação de ambos;

### Search Job Inspector
* Muito utilizado para tshoot de performance de searches
