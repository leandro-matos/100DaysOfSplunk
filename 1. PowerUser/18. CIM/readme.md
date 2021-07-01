

### Utilizando o Common Information Model (CIM) Add-On

* Descrever o Splunk Common Information Model
* Liste os knowledge objects incluídos no Splunk CIM Add-On
* Use o CIM Add-On para normalizar os dados

### O que é o Common Information Model (CIM)?
* O Splunk Common Information Model fornece uma metodologia para normalizar os dados
* Aproveite o CIM ao criar field extractions, field aliases, event types e tags para garantir:
    - Vários aplicativos podem coexistir em uma única implantação do Splunk
    - As permissões de objeto podem ser definidas como globais para o uso de vários aplicativos
    - Correlação mais fácil e eficiente de dados de diferentes sources e source types

### Normalizando Field Names - Email Data
Field Name: action
Data Type:  string
Description: Action taken by the reporting device
Possible Values: delivered, blocked, quarantined, deleted, unknown

Field Name: duration
Data Type:  number
Description: The amount of time for the completion of the messaging event, in seconds.
Possible Values: Email

Field Name: src
Data Type:  string
Description: The system that sent the message. May be aliased from more specific fields such as src_host, src_ip, or src_name.	

### Normalizando Field Names - Network Traffic
Field Name: action
Data Type: string
Description: The action taken by the network device.	
Possible Values: allowed, blocked, dropped, unknown

Field Name: bytes
Data Type: number
Description: Total count of bytes handled by this device/interface (bytes_in + bytes_out).	
	
Field Name: bytes_in
Data Type: number
Description: How many bytes this device/interface received.
	
Field Name: bytes_in
Data Type: number
Description: How many bytes this device/interface received.

Field Name: bytes_out
Data Type: number
Description: How many bytes this device/interface transmitted.

Field Name: src
Data Type: strings
Description: The source of the network traffic (the client requesting the connection). May be aliased from more specific fields such as src_host, src_ip, or src_name.	

### Normalizando Field Names - Web Data
Field Name: action
Data Type: string
Description: The action taken by the server or proxy.	

Field Name: duration
Data Type: number
Description: The time taken by the proxy event, in milliseconds.	

Field Name: http_method
Data Type: string
Description: The HTTP method used in the request.
Possible Values: GET, PUT, POST, DELETE, etc.

Field Name: src
Data Type: string
Description: The source of the network traffic (the client requesting the connection). 

Field Name: status
Data Type: string
Description: The HTTP response code indicating the status of the proxy request.
Possible Values: 404, 302, 500, and so on.

#### Splunk CIM Add-on
* Conjunto de 22 modelos de dados pré-configurados
    - Fields e categorias de event tags
    - Menor denominador comum de um domínio de interesse
* Aproveite o CIM para que os knowledge objects em vários aplicativos possam coexistir em uma única implantação do Splunk
* Disponível em splunkbase:
    - https://splunkbase.splunk.com/app/1621/
* Use as tabelas de referência CIM
    - https://docs.splunk.com/Documentation/CIM/4.9.0/User/Howtousethesereferencetables

#### Utilizando o CIM Add-On
1. Examine seus dados
    - Vá para Settings > Data Models
    - Identifique um modelo de dados relevante para o seu dataset

2. Crie event types e tags
    - Identifique os datasets CIM relevantes para seus eventos
    - Observe quais tags são necessárias para esse dataset ou qualquer dataset pai
    - Aplique essas tags a seus eventos usando event types

3. Criar field aliases
- Determine se algum campo existente em seus dados tem nomes diferentes dos esperados pelos data models
- Defina field aliases para capturar o campo com um nome diferente em seus dados originais e mapeá-lo para o nome do campo que o CIM espera

4. Adicionar missing fields
    - Criar field extractions
    - Escreva lookups para adicionar campos e normalizar os field values

5. Validar em relação ao modelo de dados
    - Use o comando **datamodel**
    - Use o Pivot no Splunk Web

#### Comando datamodel
* Pesquisa em um objeto de modelo de dados especificado
* Retorne uma descrição de todos ou de um data model especificado e seus objetos
* É um comando gerador e deve ser o primeiro comando no pipeline
* O nome do objeto e a palavra-chave de pesquisa não são válidos, a menos que precedidos pelo nome do data model. O comando search não pode ser substituído por uma string de pesquisa ou nome.
    - Ex: | datamodel WebDataModel Web search | fields Web*
    - Ao usar o comando datamodel, o nome do modelo de dados e o nome do conjunto de dados diferenciam maiúsculas de minúsculas.

#### from Command
* Recupera dados de um data model ou dataset nomeado
* Deve ser o primeiro comando em uma pesquisa
* Diferente de apenas usar datamodel
    - datamodel retorna todos os campos prefixados com o nome do modelo de dados
    - from datamodel retorna apenas campos especificados
    - **| from datamodel:"internal_server.splunkdaccess"**
* from também pode recuperar dados de saved searches, reports ou arquivos lookup
    - **| from savedsearch:mysecurityquery**

### CIM - Recursos Adicionais
* Entendendo e utilizando o CIM Add-on
http://docs.splunk.com/Documentation/Splunk/latest/Knowledge/UnderstandandusetheCommonInformationModel

* Overview do Splunk CIM
http://docs.splunk.com/Documentation/CIM/latest/User/Overview

* Use o CIM para normalizar os dados no momento da pesquisa
http://docs.splunk.com/Documentation/CIM/latest/User/UsetheCIMtonormalizedataatsearchtime
