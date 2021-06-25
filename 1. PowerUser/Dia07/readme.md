
## Objetivos:
• Explorar os requisitos de estrutura de dados
• Explorar tipos de visualização
• Criar e formatar gráficos
• Criar e formatar gráficos de tempo
• Explicar quando usar cada tipo de comando de relatório

### Tipos de Visualização:
* Quando uma pesquisa retorna valores estatísticos, os resultados podem ser visualizados com uma ampla variedade de tipos de visualização
    - Statistics table
    - Charts: Line, column, pie, etc
    - Single value, gauges
    - Maps
    - Entre outros

### Visualizar os Resultados:
* Nem todas as pesquisas podem ser representadas visualmente
* Uma série de dados é uma sequência de pontos de dados relacionados que são plotados em uma visualização
* A série de dados pode gerar quaisquer resultados estatísticos ou de visualização

### Requisitos de estrutura de dados - Single Series
* A maioria das visualizações requer resultados de pesquisa estruturados como tabelas, com pelo menos duas colunas, uma única série
    - A coluna mais à esquerda fornece os valores do eixo x
    - As colunas subsequentes fornecem valores numéricos do eixo y para cada série no gráfico

### Requisitos de estrutura de dados - Multi-Series
* Para obter tabelas de várias séries, você precisa configurar a pesquisa subjacente com comandos de pesquisa de relatórios, como **chart** ou **timechart**

### Requisitos de estrutura de dados - Time Series
* Time series exibe tendências estatísticas ao longo do tempo
* Pode ser uma série ou várias séries

### Ver os resultados como um gráfico
* Existem sete tipos de gráficos: Line, Area, Column, Bar, Bubble, Scatter, Pie

### Charts - Scatter e Bubble
* Gráficos do tipo **scatter** mostram tendências nas relações entre valores de dados discretos
* Geralmente, mostra valores discretos que não ocorrem em intervalos regulares ou pertencem a uma série
* Gráficos do tipo **Bubble** fornecem uma maneira visual de visualizar uma série tridimensional
* Cada bolha é plotada em duas dimensões nos eixos X e Y
* O tamanho do **bubble** representa o valor do terceiro dimensão

### Viualizações - X e Y Axes
* Para gráficos de linha, área e coluna, o eixo x é horizontal
* Para gráfico de barras, o eixo x é vertical

### chart Command
* O comando **chart** pode exibir qualquer série de dados que você deseja plotar.
* Você decide qual campo traçar no eixo x
    - A função define o valor do eixo y, portanto, deve ser numérico
    - O primeiro campo após a cláusula over é o eixo x
    - Usar as cláusulas over e by divide os dados em subgrupos
    - Os valores da cláusula by são exibidos na legenda
**chart avg(bytes) over host**
    - Os valores do host são exibidos no eixo x
**chart avg(bytes) over host by product_name**
    - O campo do host é o eixo xe a série é dividida por product_name

### chart Command – over field
* função de contagem registra o número de eventos para cada valor no conjunto de resultados:
    - index=security sourcetype=linux_secure | chart count over vendor_action

### chart Command – over field by field
* Você pode usar a cláusula by com a cláusula over para dividir os resultados (**over vendor_action by user**)
* Alternativamente, você pode usar apenas duas cláusulas por (**by vendor_action, user**)
* Você só pode dividir os resultados do gráfico em DUAS dimensões (ao contrário dos resultados de estatísticas)
* É possível definir o stack mode (On ou OFF)

### Incluindo valores NULL e OTHER
* Os comandos **chart** e **timechart** de tempo filtram automaticamente os resultados para incluir os dez valores mais altos
    - Os valores excedentes são agrupados em **OTHER**
* Neste exemplo, os resultados são distorcidos por **NULL** e **OTHER**. 
    - Ex: index=web sourcetype=access_combined status>399 | chart count over host by itemId
    - Esses valores são mostrados por padrão

### Omitindo valores NULL e OTHER
* Para remover valores de campos vazios (NULL) e OTHER do display, use estas opções:
    - **useother=f**
    - **usenull=f**

### Limitando o número de valores
* Para ajustar o número de séries plotadas, use o argumento limite
* Para valores ilimitados, use limit=0
    - Ex: **index=web sourcetype=access_combined action=purchase status=200 | chart sum(price) over host by product_name limit=5 useother=f**

### timechart Command – Overview
* O comando **timechart** realiza agregações estatísticas em relação ao tempo
* Dados de gráficos e tendências ao longo do tempo
* _time é sempre o eixo x
* Você pode opcionalmente dividir os dados usando a cláusula by para um outro campo
    - Cada valor distinto da divisão por campo é uma série separada no gráfico
* Os gráficos de tempo são mais bem representados como gráficos de linha ou área

### timechart Command – Exemplos
**index=network sourcetype=cisco_wsa_squid usage=Violation | timechart count**

* Dividindo pelo campo de uso, cada linha representa um valor de campo único
    - Ao contrário das estatísticas, apenas UM campo pode ser especificado após por
    - eixo y representa a contagem para cada valor de campo
    - **index=network sourcetype=cisco_wsa_squid | timechart count by usage**

* Multi-series: No
    - Quando o modo multisséries é definido como **NO**, todos os campos compartilham o eixo y

* Multi-series: Yes
    - Definir o modo multisséries como **Yes** faz com que o eixo y se divida para cada valor de campo
    - O eixo y é dividido em seções, cada uma abrangendo a mesma contagem máxima e mínima

### Comando timechart - Ajustando o intervalo de amostragem
* O comando timechart "armazena" os valores do campo _time
    - Isso fornece intervalos de amostragem dinâmica, com base no intervalo de tempo da pesquisa
* Exemplos de padrões:
    - Últimos 60 minutos usa span = 1m
    - As últimas 24 horas usam span = 30m
* Ajuste o intervalo usando o argumento span, por exemplo **span=15m** 

### Trellis Layout
* Exibir vários gráficos com base em um conjunto de resultados
* Permite comparação visual entre diferentes categorias
* Dados buscados apenas uma vez

### Detalhes sobre os Comandos
* stats:
    - Multi-level breakdown [by	clause]: Many

* chart: 
    - Multi-level breakdown [by	clause]: 02
    - Limit # series shown: limit=n, Default=10
    - Filter other series: useother=false
    - Filter null values: usenull=false

* timechart:
    - Multi-level breakdown [by	clause]: 01
    - Limit # series shown: limit=n, Default=10
    - Filter other series: useother=false
    - Filter null values: usenull=false
    - Set time value on x axis: span

* Para contar a frequência de um (s) campo (s), use **top/rare**
    - **index=security sourcetype=linux_secure | top src_ip,user,vendor_action,app**
    - **index=security sourcetype=linux_secure | rare src_ip,user,vendor_action,app**

* Use **stats** para calcular estatísticas para dois ou mais por campos (não baseado em tempo)
    - **index=security sourcetype=linux_secure | stats count by src_ip,user,vendor_action,app**

* Para calcular estatísticas com um campo arbitrário como eixo x (not _time), use o **chart**
    - Quando você usa um by field, a saída é uma tabela
    - Cada coluna representa um valor distinto do campo dividido
    - **index=security sourcetype=linux_secure | chart count over src_ip by vendor_action**

* Use o **timechart** de tempo para calcular estatísticas com _time como o eixo x
* Se for usado um by field, a saída é uma tabela
* Cada coluna representa um valor distinto do campo dividido por: **.. | timechart span=1h count by itemId limit=3 useother=f**