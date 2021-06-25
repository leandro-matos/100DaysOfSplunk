
### trendline Command

* Permite que você sobreponha uma média móvel calculada em um gráfico
* A linha de tendência calcula as médias móveis de um campo:
    - **trendline <trendtype><period>(field) [AS	newfield]**

* trendtype:
    – **sma** - simple moving average
    – **ema** - exponential moving average
    – **wma** - weighted moving average

* Deve definir o período durante o qual calcular a tendência

* O período deve ser um número inteiro entre 2 e 10.000:
    - Por exemplo, **sma2(sales)** é válido
    - Mas sma(sales) falhará, pois está faltando um número inteiro, o período de definição

### Ver os resultados como um mapa: 

* ClusterMap, Choropleth Map

### iplocation Command

* Use o iplocation para pesquisar e adicionar informações de localização a um evento
    - Essas informações incluem cidade, país, região, latitude e
longitude

* Nem todas as informações estão disponíveis para todos os intervalos de endereços IP

* Define automaticamente os campos **lat** e **lon** padrão exigidos por **geostats**
    - **index=security sourcetype=linux_secure (fail* OR invalid) | iplocation src_ip**

### geostats Command

* Use **geostats** para calcular funções estatísticas e renderizar um mapa de cluster
    - geostats	[latfield=string]	[longfield=string]	[stats-agg- term]*	[by-clause]

* Os dados devem incluir valores de latitude e longitude

* Defina o **latfield** e o **longfield** apenas se eles diferirem dos campos **lat** e **lon** padrão

* Para controlar a contagem de colunas:
    - Em um nível global, use o argumento **globallimit**
    - Em um nível local, dependendo de onde seu foco está (ou seja, onde você ampliou), use o argumento do **locallimit**
    - **index=security sourcetype=linux_secure (fail* OR invalid) | iplocation src_ip | geostats globallimit=5 count by user**

### Choropleth Map

* Usa sombreamento para mostrar métricas relativas, como vendas, invasores de rede, etc. para regiões geográficas predefinidas

* Para definir limites regionais, você deve ter:
    - Arquivo KML (Keyhole Markup Language)
    - Arquivo KMZ (Keyhole Markup Language compressed)

* O Splunk é fornecido com:
    – geo_us_states, United States
    – geo_countries, countries of the world
    - …| geom [featureCollection] [featureIdField=string]
    - index=sales sourcetype=vendor_sales | stats count as Sales by VendorCountry | geom_countries featureField=VendorCountry

### Visualizando os resultados como um Single Value

* As visualizações de valor único fornecem várias opções de formatação
* Defina a cor usando a IU ou com o comando do medidor
* Opcionalmente, especifique informações de formato de número para o valor único na guia Formato de Número

* Com o comando **timechart**, você pode adicionar um minigráfico e uma tendência
* O **sparkline** é um gráfico embutido
    - Ele é projetado para exibir tendências baseadas no tempo associadas à chave primária

* O **trend** mostra a direção em que os valores estão se movendo
    - Parece à direita do valor único

### Adicionando Totals Usando Opções de Formato

* Totalize automaticamente todas as colunas usando as opções de formato

* Ao usar esta abordagem, você:
    - Não é possível indicar qual coluna totalizar; todas as colunas são sempre totalizadas
    - Não é possível adicionar rótulos

* Usando a guia **Summary**, você pode adicionar uma linha % ao final da tabela de estatísticas
* Todas as colunas são usadas para calcular a porcentagem - ou seja, todas as porcentagens de todas as colunas combinadas serão iguais a aproximadamente 100%

### addtotals Command

* Alternativamente, use o comando addtotals para:
    - Calcule a soma de todos os campos numéricos selecionados para cada coluna e coloque o total na última linha
    - Calcule a soma de todos os campos numéricos selecionados para cada linha e coloque o total na última coluna
    - **addtotals [row=bool] [fieldname=field] [col=bool][labelfield=field]	[label=string]	field-list**

* Row Options:
    - **row=true/false (Default= true)**: É criada uma coluna que contém totais numéricos para cada linha.
    - **fieldname=field (Default=Total)**: Define uma string usada para criar um nome de campo para a coluna de totais.

* Column Options:
    - **col=true/false (Default= false)**: É criada uma linha que contém totais numéricos para cada coluna.
    - **label=string (Default=Total)**:	Define uma string usada para nomear a linha de totais.
    - **labelfield=fieldname**:	Define onde a string do rótulo é colocada. (Geralmente, você deve tornar esta a primeira coluna.)

* General Options
    - **field-list=one or more numeric fields. (Default: all numeric fields)**: Define os campos numéricos a serem totalizados.

* **row=t (default)** conta os campos em cada linha em uma coluna chamada "Total por produto"
* **col=t** conta os campos em cada linha em uma linha chamada "Total por país"
    - index=sales | chart count over product_name by Country | addtotals fieldname="Total" col=t label=Total Per Country" labelfield=product_name

* Não totalize as linhas Total de colunas, Adicione o rótulo total, Coloque o rótulo sob a coluna do host, Totalize apenas a coluna Bytes:
    - index=web | stats sum(bytes) as Bytes, avg(bytes) as avgBytes, count as total by host | addtotals row=f col=t label=total labelfield=host Bytes
