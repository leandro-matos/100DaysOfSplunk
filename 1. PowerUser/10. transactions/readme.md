
### Use o comando eval para:
    - Identificar transactions
    - Eventos de grupo usando campos
    - Eventos de grupo usando campos e tempo
    - Pesquisa com transactions
    - Relatório de transactions
    - Determine quando usar transactions vs. stats

### O que é uma transação?
    * Uma transação é qualquer grupo de eventos relacionados que abrangem o tempo
    * Os eventos podem vir de vários aplicativos ou hosts
        - Eventos relacionados a uma única compra de uma loja online podem se estender por um servidor de aplicativos, banco de dados e mecanismo de comércio eletrônico
    * Uma mensagem de e-mail pode criar vários eventos à medida que passa por várias filas
    * Cada evento nos logs de tráfego de rede representa um único usuário gerando uma única solicitação http
    * Visitar um único site normalmente gera várias solicitações http
        - HTML, JavaScript, arquivos CSS
        - Flash, imagens, etc.

### transaction
* transaction field-list
    - a lista de campos pode ser um nome de campo ou uma lista de nomes de campo
    - Os eventos são agrupados em transações com base nos valores desses campos
* Se vários campos forem especificados e houver uma relação entre esses campos, os eventos com valores de campo relacionados serão agrupados em uma única transação
• Restrições comuns:
    - maxspan maxpause startswith endswith


### Eventos que possuem o mesmo JSESSIONID
* O log mostra uma série de eventos que compartilham o mesmo valor JSESSIONID (SD0SL10FF3ADFF4950)
* No entanto, é difícil:
    - Veja os eventos como um grupo
    - Obtenha informações sobre o que está acontecendo com esses eventos
    - Saiba se existem outros eventos espalhados no conjunto de resultados
    - Ex: **index=web sourcetype=access_combined**


### transaction Command – Exemplo01
* O comando de transaction cria um único evento de um grupo de eventos
* Os eventos devem compartilhar o mesmo valor em um campo especificado
* As transações podem cruzar vários níveis, como servidores da web ou servidores de aplicação
* Por exemplo, você pode facilmente visualizar os eventos para JSESSIONID SD0SL10FF3ADFF4950
    - Ex: **index=web sourcetype=access_combined | transaction JSESSIONID**


### transaction Command – Exemplo02
* Use o comando **search** em qualquer ponto do pipeline de pesquisa para filtrar os resultados
* Se comporta exatamente como as strings de pesquisa antes do primeiro tubo
    - a pesquisa usa o caractere curinga "*" e trata os valores dos campos sem fazer distinção entre maiúsculas e minúsculas
    - status=404 encontra os erros
    - realçar destaca os termos que você especificar
    - Ex: **index=web sourcetype=access_combined | transacion JSESSIONID | search status=404 | highlight JSESSIONID, 404**


#### transaction - Campos específicos
O comando transaction produz campos adicionais, como:
    - duration: a diferença entre os carimbos de data/hora para o primeiro e o último evento na transação
    - eventcount: o número de eventos na transação


### transaction – maxspan/maxpause
* Você também pode definir um intervalo de tempo geral máximo e um intervalo máximo entre eventos
    - maxspan = 10m
        - Tempo total máximo entre o primeiros e últimos eventos
        - Se não for especificado, o padrão é -1 (ou sem limite)
    - maxpause = 1m
        - Tempo total máximo entre eventos
        - Se não for especificado, o padrão é -1 (ou sem limite)
    - Ex: **index=web | transaction clientip maxspan=10m maxpause=1m | eval duration=tostring(duration,"duration") | sort -duration | table clientip duration action**


### transaction – startswith/endswith
* Para formar transações com base em termos, valores de campo ou avaliações, use as opções startswith e endswith
* Neste exemplo:
    - O primeiro evento na transação inclui addtocart
    - O último evento inclui purchase
    - Ex: **index=web | transaction cliente JSESSIONID startswith=eval(action="addtocart") endswith=eval(action="purchase") | table clientip, JSESSIONID, duration, eventcount**

#### Investigando com transactions
* As transações podem ser úteis quando um único evento não fornece informações suficientes
* Este exemplo pesquisa logs de e-mail para o termo “REJEITAR”
* Eventos que incluem o termo não fornecem muitas informações sobre a rejeição
    - Ex: **index=network sourcetype=cisco REJECT**

* Ao criar uma transação, você pode pesquisar e ver eventos adicionais relacionados à rejeição, como:
    - endereço IP do remetente
    - Resultados de busca reversa de DNS
    - Ação realizada pelo sistema de correio após a rejeição
    - mid: ID da mensagem
    - dcid: ID de conexão de entrega
    - icid: ID de conexão de entrada
    - Ex: **index=network sourcetype=cisco | transaction mid dcid icid | search REJECT**


### Relatório de transactions
* Você pode usar estatísticas e comandos de relatórios com transações
* Neste exemplo, uma transação é definida por eventos que compartilham clientip e cabem em um intervalo de 10 minutos
* a função count() conta o número de transações e separa a contagem pela duração de cada
    - Ex: **index=poweruser sourcetype="access_combined_wcookie" status=200 action=purchase | transaction clientip maxspan=10m | chart count by duration span=log2**


### transaction vs stats
* Quando você tiver escolha, use **stats** - é mais rápido e mais eficiente, especialmente em grandes ambientes Splunk
* Use **transaction** apenas quando você:
    - Precisa ver eventos correlacionados juntos
    - Deve definir o agrupamento de eventos com base nos valores de início/fim ou segmento no tempo
* Use estatísticas quando você:
    - Quer ver os resultados de um cálculo
    - Pode agrupar eventos com base em um valor de campo (por exemplo, por src_ip)
* Por padrão, há um limite de 1.000 eventos por transação
    - Esse limite não se aplica ao **stats**
    - Os administradores podem alterar o limite configurando **max_events_per_bucket** em **limites.conf**


### transaction vs stats - Exemplo 01
* As pesquisas produzem o mesmo resultado
    - Ex: **index=web | transaction JSESSIONID | table JSESSIONID, action, product_name | sort JSESSIONID**
    - Ex: **index=web | stats values(action) as "action", values(product_name) as "product_name" by JSESSIONID | sort JSESSIONID**
    - stats: levou 23.381 segundos
    - transaction: levou 2.077 segundos
    - stats mais rápidas do que transaction


### transaction vs stats - Exemplo 01
* As pesquisas produzem o mesmo resultado
    - Ex: **index=security failed | transaction src_ip | table src_ip, eventcount | sort - eventcount**
    - Ex: **index=security failed | stats count as eventcount by src_ip | sort - eventcount**
    - stats: levou 06 segundos
    - transaction: levou 04 segundos
