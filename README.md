# 100DaysOfSplunk

### Splunk é uma ferramenta de pesquisa e análise de Dados. "Google for LogFiles"

* Faz uso do conceito de Big-Data, e banco de dados no-sql, indexando diariamente os dados dos sistemas.
* Basicamente o Splunk trabalha de duas formas: Indexando e Consultando dados;

Como funciona ?
* SPL (Search Processing Languange) - Basicamente o conceito é encadear comandos sequencialmente, filtrando, transformando, incluindo e até mesmo excluindo dados.

Como ele salva as informações ?
* Em pastas chamadas de "Indexers", criando dois tipos de arquivos (RawData e MetaData)
* Juntos esses arquivos constituem o INDEX;

* Sourcetype - Padrão do Log
* props.conf e transform.conf - Arquivos de Configurações para definições de padrões

Como funciona a idade de um arquivo ?
* Cada diretório do index é chamado de BUCKET, o mesmo é dividido por vários estágios de "velhice". 
* Quando um arquivo ultrapassa uma certa idade, ele é movido de um Bucket para o outro.

Bucket:
* Hot - Contains newly indexed data. Open for writing. One or more hot buckets for each index.
* Warm - Data rolled from hot. There are many warm buckets. Data is not actively written to warm buckets.
* Cold - Data rolled from warm. There are many cold buckets.
* Frozen - Data rolled from cold. The indexer deletes frozen data by default, but you can choose to archive it instead.
* Thawed - Data restored from an archive. If you archive frozen data, you can later return it to the index by thawing it.

Licenciamento:
* Faz uso do conceito de big-data, e banco de dados no-sql, indexando diariamente os dados dos sistemas.
* Sua licença é comercializada na forma de volume de dados indexado diariamente.
* 1.800,00 Doláres - 01GB por dia;
* 1.800,00 Doláres - 10GB por dia;
* 760,00 Doláres   - 50GB por dia;
* 600,00 Doláres   - 100GB por dia;

Conceito de Apps:
* Apps são módulos, pronto para uso com poucos cliques.

Search: earliest e latest
* earliest representa a data do evento mais antigo
* latest representa a data do evento mais recente

Ex: **search index=main usuario earliest=-5d@d latest=-1d@d**

Job:
* Vida útil de um job em torno de 10 minutos
* | loadjob NomeDoEvento

