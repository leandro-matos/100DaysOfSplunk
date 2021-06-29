
## Criação de Data Models

* Descrever a relação entre data models e Pivot
* Identificar data model datasets
* Identificar os campos do dataset
* Criar um datamodel
* Use um data model no Pivot

### Revisando Pivot
* Usado para criar relatórios e painéis
* Como gerente de conhecimento, você é responsável por construir o data model que fornece os conjuntos de dados para Pivot 

### Overview Data Models
* Conjuntos de datasets estruturados hierarquicamente que geram pesquisas e impulsionam o Pivot
* Pivot Reports são criados com base em datasets
* Cada evento, pesquisa ou transação é salvo como um dataset separado

### Data Model Dataset Types
Um data model pode consistir em 3 tipos de conjuntos de dados
* Eventos
* Pesquisas
* Transactions

### Data Model Events
* Os **Event datasets** contêm restrições e campos
* As **constraints** são essencialmente a pesquisa dividida em uma hierarquia
* Os **Fields** são propriedades associadas aos eventos

### Dataset Fields
* Selecione os campos que deseja incluir no dataset
* Assim como as constraints, os campos são herdados de objetos pais

### Criando um Data Model
* Settings -> Data Models - New Data Model

### Adicionando Root Event
* Neste exemplo, o root event deste data model representa todas as solicitações da web
* Os atributos herdados são campos padrão
* Use **Add field > Auto-Extracted** para adicionar mais campos

### Adicionando Fields
* Auto-Extracted -Podem ser campos padrão ou campos extraídos manualmente
* Eval Expression - um novo campo baseado em uma expressão que você define
* Lookup - aproveite uma tabela de lookup existente
* Regular Expression - extraia um novo campo com base em regex
* Geo IP - adicione campos geográficos, como latitude/longitude, país, etc.

### Adicionando Fields - Auto-Extracted
* Os campos que já existem para a constraint podem ser adicionados como atributos ao data model

### Field Types
* String: os valores dos campos são reconhecidos como alfanuméricos
* Number: os valores dos campos são reconhecidos como numéricos
* Boolean: os valores dos campos são reconhecidos como verdadeiro/falso ou 1/0
* IPV4: os valores dos campos são reconhecidos como endereços IP
    - Este é um tipo de campo importante, pois pelo menos um tipo de atributo IPV4 deve estar presente no modelo de dados para adicionar um atributo GeoIP

### Field Flags
* Optional: Este campo não precisa aparecer em todos os eventos
* Required: apenas os eventos que contêm este campo são retornados no Pivot
* Hidden: Este campo não é exibido para usuários do Pivot quando eles selecionam o conjunto de dados no Pivot
    - Use para campos que estão sendo usados ​​apenas para definir outro campo, como uma expressão eval
* Hidden, Required: apenas os eventos que contêm este campo são retornados, e os campos não podem ser usados ​​no Pivot

### Adicionando Fields - Eval Expressions
* Você pode definir um novo campo usando uma expressão eval
    - Neste exemplo, você cria um campo denominado **Error Reason** que avalia o valor do campo de status

### Adding Fields – Lookups
* Aproveite um lookup definition para adicionar campos ao seu objeto de evento
* Configure o lookup attribute da mesma forma que um automatic lookup
* Use a Preview para testar suas configurações de pesquisa
* Use a guia Eventos e Valores para verificar seus resultados

### Adicionando Fields - Regular Expression
* Você pode definir um novo campo usando uma expressão regular

### Adicionando Fields - GeoIP
* As visualizações de mapa requerem campos de latitude/longitude
* Para usar Geo IP Lookup, pelo menos um campo IP deve ser configurado como um tipo IPv4
* Embora a função de mapa não esteja disponível no Pivot, o data model pode ser chamado usando o **| comand pivot and <map>** elemento em uma pesquisa de população de painel
    - Selecione o campo que contém o mapeamento para lat/lon
    - Identificar os campos lat/lon e geo nos dados

### Adicionando Child Datasets
* Ao criar um novo child dataset, você atribui a ele uma ou mais constraint adicionais
* Child datasets herdam todos os campos dos eventos pai
* Você pode adicionar mais campos ao child datasets

### Testando Data Model
* Clique em Pivot para acessar a janela Selecionar um Conjunto de Dados
* Escolha um objeto do modelo de dados selecionado para começar a construir o relatório

### Utilizando o DataModel in Pivot
* Uma nova janela do Pivot é preenchida automaticamente com uma contagem de eventos para o dataset selecionado

### Pivot - Utilizando Fields
* Os campos associados a cada dataset estão disponíveis como divisões para linhas ou colunas
* Neste exemplo, o relatório Pivot mostrará uma contagem de ações de solicitação com falha por status
* Os campos também podem ser usados ​​para filtrar eventos na interface Pivot
* Neste exemplo, o relatório Pivot é filtrado para retornar apenas resultados onde status=503

### Data Model Search Datasets
* Pesquisas arbitrárias que incluem comandos de transformação para definir o dataset que eles representam
* Os datasets de pesquisa também podem ter campos, que são adicionados por meio do botão **Add Field**

### Data Model Transaction Datasets
* Permitir a criação de datasets que representam transações
* Use campos que já foram adicionados ao modelo usando eventos ou datasets de pesquisa

### Adicionando uma Transação
* Você pode adicionar uma transação ao data model
* O conjunto de dados da transação abaixo equivaleria à pesquisa:
    - sourcetype = access_ * | transaction clientip maxpause=10s
* Você pode então adicionar uma expressão eval ou qualquer outro campo à sua transação para definir melhor os resultados

### Considerações sobre o dataset de pesquisa e transação
* Deve haver pelo menos um evento ou dataset de pesquisa antes de adicionar um conjunto de dados de transação
* Conjuntos de dados de pesquisa e transação não podem se beneficiar da aceleração persistente do datamodel
* À medida que você aprende a criar data models, considere os tipos de relatórios que seus usuários executarão
    - O mesmo relatório pode ser obtido com datasets de eventos?
    - Os usuários precisarão de raw events ou dados transacionais?

### Definir permissões
* Quando um data model é criado, o proprietário pode determinar o acesso com base nas seguintes permissões:
    - Quem pode ver os modelos de dados (Owner, App, All Apps)  
    - Quais usuários podem executar quais ações (leitura/gravação)
         Everyone
         Power
         User
         Funções definidas pelo administrador, se aplicável
    
### Download e Upload de Data Models
* Use a interface Splunk Web para fazer download ou upload de data models:
    - Faça backup de data models importantes
    - Colabore com outros usuários do Splunk para criar/modificar/testar datamodels
    - Mova data models de um ambiente de teste para uma instância de produção

### Data Model Acceleration
* Usa resumos criados automaticamente para acelerar os tempos de conclusão para pivots
* Assume a forma de arquivos de índice de série temporal invertidos(tsidx) que foram otimizados para velocidade

### Accelerating a Data Model
* Com a aceleração persistente do data model, todos os campos no modelo se tornam campos "indexados"
* Você deve ter permissões administrativas ou o capacidade de **accelerate_datamodel** para acelerar um data model
* Modelos de dados privados não podem ser acelerados
* Modelos de dados acelerados não podem ser editados
* Apenas roto events podem ser acelerados. Se houver vários root events, apenas o primeiro evento raiz será acelerado.