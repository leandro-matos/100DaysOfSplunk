
### Principais funções do PowerUser
* Usuário avançado do Splunk com um elevado conhecimento na parte de administração do Splunk a nível de Usuário;
* As responsabilidades são fornecer informações aos usuários em toda a empresa e criar e gerenciar os objetos de conhecimento do Splunk para as partes interessadas;
* Implementar as melhores práticas para as convenções de nomenclatura de todos os objetos de conhecimento;
* Coletar dados e estatísticas e relatar sobre Segurança, Operações de TI, Inteligência Operacional, etc.


### Basic Search Review
* Keywords:
Por exemplo, pesquise uma única palavra (por exemplo, **error**) ou grupo de palavras (por exemplo, **error password**)

* Booleans:
**NOT, OR, AND**; AND está implícito; DEVE estar em letras maiúsculas; pode usar ()'s para forçar a precedência
Ex: **sourcetype = vendor_sales OR (sourcetype = access_combined action = purchase)**

* Phrases:
**"web error"** é diiferente de **web** AND **error**

* Field searches:
status=404,	user=admin

* Wildcard (*):
status=40* corresponde a 40, 40a, 404, etc.
Iniciar palavras-chave com um caractere curinga é muito ineficiente, por exemplo: *dmin, *assword, *ailure

* Comparisons:
=, !=, <, <=, >=, >	
status>399,	
user!=admin

* **table**: retorna a tabela contendo apenas campos especificados no conjunto de resultados
* **rename**: renomeia um campo nos resultados
* **fields**: inclui ou exclui campos especificados
* **dedup**: remove duplicados dos resultados
* **sort**: classifica os resultados por campo especificado
* **lookup**: adiciona valores de campo de fonte externa (por exemplo, arquivos .csv)


### Case-sensitive - Sensitive
* Operadores Booleanos (Maiúsculos): 
    * AND, OR, NOT (Operadores Booleanos) and, or, not (palavras-chave literais)

* Field names	
    * productId vs. productid
    * eval cs_username = "Total	Access"

* Field values from lookup (default, but configurable)	
    * product_name="Tulip Bouquet" vs. product_name="tulip bouquet"

* Expressões Regulares:	
    * \d\d\d vs. \D\D\D

* eval and where commands	
    * eval action=if(action=="view",...) where action="Purchase" stats count(eval(action="view") as…

* Tags 
    * tag=DMZ vs. tag=dmz

* Command names:
    * STATS, **stats**, sTaTs

* Command clauses:
    * AS used by stats,	rename,	...;
    * BY used by stats,	chart, top,	...; 
    * WITH used	by replace

* Search terms:
    * failed, FAILED, Failed

* Statistical functions:
    * **avg**, AVG,	Avg	used by	**stats**, **chart**, …

* Field values:
    * host=www1, host=WWW1 (A menos que venha de uma pesquisa)



### Como o Splunk faz pesquisas ? - Buckets
* Conforme os eventos chegam, o Splunk os coloca em um balde **hot** de índice (apenas gravavel);
* Conforme os baldes envelhecem, eles passam do **quente** para o **warm** e para o **cold**
* Cada intervalo tem seus próprios dados brutos, metadados e arquivos de índice
* Metadata files track source, sourcetype, and host
* Os administradores podem adicionar mais

### Como o Splunk faz pesquisas ? - Procurando
* Quando você pesquisa, o Splunk usa o intervalo de tempo para escolher quais buckets pesquisar e, em seguida, usa os índices de bucket para encontrar eventos de qualificação
* Quando você pesquisa por **index=web password fail *** durante as últimas 24 horas:
    - O Splunk identifica os baldes das últimas 24 horas;
    - E pesquisa os índices desses baldes para os termos de pesquisa;
    - Hot (Agora até 08 horas); Warm (09 até 48 horas); Cold: (48 até 57 horas, etc.)


### Práticas Gerais de Pesquisa
* Como os eventos são armazenados por hora, o tempo é o filtro mais eficiente;
* Depois de algum tempo, as palavras-chave mais poderosas são host, source, sourcetype;
* Para tornar as pesquisas mais eficientes, inclua o máximo de termos possível. Ex: Pesquisar por **sourcetype=x fail** é melhor do que **fail**
* Use o comando **fields** para extrair (descobrir) apenas os campos de que você precisa
* Exemplo: Pesquisa nos últimos 365 dias, verifica 566.720 eventos (em segundos):
    - **index=web sourcetype=access_combined** Pesquisa: 15.16 segundos
    - **index=web sourcetype=access_combined | fields clientip bytes referrer** Pesquisa: 4.49 segundos


### Práticas Gerais de Pesquisa - Wildcards
* O Splunk pesquisa apenas palavras inteiras, mas caracteres curinga são permitidos
* Apenas os curingas no final fazem uso eficiente do índex:
    - Caracteres curinga no início da sequência de varredura de todos os eventos dentro do prazo;
    - Os curingas no meio da string podem retornar resultados inconsistentes;
    - Portanto, use **fail*** (não *fail ou *fail* ou f*il)
* Caracteres curinga testados após todos os outros termos


### Práticas Gerais de Pesquisa
* A inclusão é geralmente melhor do que a exclusão:
    - Pesquisar por **acesso negado** é mais rápido do que **NOT "acesso concedido"**
* Filtre o mais cedo possível em sua pesquisa:
    - Remover duplicatas e depois classificar é mais rápido do que classificar e remover duplicatas
* Use o modo de pesquisa apropriado:
    - Fast - desempenho acima da integridade
    - Smart [padrão]
    - Verbose - completude sobre o desempenho


### Transforming Search Commands
* Um comando **transforming**:
    - Mensagens de dados brutos em uma tabela de dados
    - 'Transform' valores de células especificados para cada evento em valores numéricos que você pode usar para fins estatísticos
    - É necessário "transformar" os resultados da pesquisa em visualizações
* Transforming commands include:
    –	top, rare, chart, timechart, stats, geostats 


### Revendo o modo de pesquisa - Fast Mode
* Enfatiza o desempenho, retornando apenas dados essenciais e necessários
* Para pesquisas não transformadoras:
    ✓ Events - a barra lateral de campos exibe apenas os campos obrigatórios para a pesquisa
    ✓ Patterns
    ✗  Statistics ou visualizations
* Os conteúdos da barra lateral de campos interessantes são perdidos
* Para transformar pesquisas:
    ✗ Events
    ✗ Patterns
    ✓ Statistics or visualizations


### Revendo o modo de pesquisa – Smart Mode (Default)
* Projetado para dar a você os melhores resultados para a pesquisa
* Combinação dos modos Fast e Verbose
* Para pesquisas não transformadoras [Detalhado]:
    ✓ Events - a barra lateral de campos exibe todos os campos
    ✓ Patterns
    ✗ Statistics ou visualizations
* Para transformar pesquisas:
    ✗ Events
    ✗ Patterns
    ✓ Statistics or visualizations


### Revendo o modo de pesquisa – Verbose Mode (Default)
* Enfatiza a integridade, retornando todos os dados de campo e evento possíveis
* Para pesquisas não transformadoras:
    ✓ Events - a barra lateral de campos exibe todos os campos
    ✓ Patterns
    ✗ Statistics or visualizations
* Para transformar pesquisas:
    ✓ Events
    ✓ Patterns
    ✓ Statistics or visualizations


### Desempenho das pesquisas: 
* Use o modo de pesquisa mais apropriado: **index=web sourcetype=access_combined | chart count by product_name**
* Time range: last 365 days
Mode	Returned Results  Time
Fast	    14	           1.82
Smart	    14	           1.91
Verbose	    14	           15.21


### Desempenho de pesquisa - Tipos de pesquisas

* Dense: 
    - Uma grande porcentagem dos dados corresponde à pesquisa.
    - Casos de uso: estatísticas de computação, relatórios
    - Ex: **index=web sourcetype=access_combined | timechart count**
    - Up to 50K matching EPS (Events per second) CPU bound

* Sparse:
    - Uma pequena porcentagem de dados corresponde à pesquisa
    - Casos de uso: solução de problemas, análise de erros
    - **index=web sourcetype=access_combined  status=404 | timechart count**
    - Up to 5K matching EPS (Events per second) CPU bound

* Super Sparse:
    - Retorna um pequeno número de resultados de cada segmento de índice correspondente à pesquisa
    - I / O intensivo enquanto o indexador examina todos os baldes de um índice
    - Com muitos dados, com muitos baldes, pode levar muito tempo para terminar
    - **index=network sourcetype=cisco_wsa_squid action=denied src_ip=10.2.3.11**
    - Up to 2 seconds per index bucketI/O bound

* Rare:
    - O indexador verifica todos os baldes para encontrar resultados, mas os filtros bloom eliminam os baldes que não incluem resultados de pesquisa
    - Casos de uso: rastreamento do comportamento do usuário
    - **index=web sourcetype=access_combined sessionID=1234**
    - Up to 10-50 index buckets/second I/O bound


### Search Job Inspector
* A ferramenta permite que você examine:
    - Estatísticas gerais de pesquisa (por exemplo, registros processados ​​e retornados, tempo de processamento)
    - Como a pesquisa foi processada
    - Onde Splunk passava seu tempo
* Use para solucionar problemas de desempenho de pesquisa e entender o impacto dos objetos de conhecimento no processamento (por exemplo, tipos de eventos, tags, pesquisas)
* Qualquer trabalho de pesquisa existente (ou seja, não expirado) pode ser inspecionado

### Search Job Inspector – 3 Componentes
* Header: O Search Hop Inspector fornece informações básicas, incluindo o tempo de execução e o número de eventos verificados

* Execution Costs: Fornece detalhes sobre o custo para recuperar resultados, como:
    - **command.search.index**: Hora de pesquisar o índice para o local para ler em arquivos rawdata
    - **command.search.filter**: Tempo para filtrar eventos que não correspondem
    - **command.search.rawdata**: Hora de ler eventos dos arquivos rawdata

* Search Job Properties:
Example: **index=sales sourcetye=vendor_sales VendorID>=7000 AND VendorID<9000**
    - Produces scanCount of 127,201 events
    - Returns resultCount of 2,144 in 3.01 seconds
    - To calculate performance:
        + Do not use resultCount/time	2,144 / 3.01	=	712	Events Per Second
        + Rather, calculate scanCount/time	127,201/ 3.01	=	40,892	Events Per Second
