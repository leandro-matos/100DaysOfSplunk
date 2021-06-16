
# Splunk-Power-User

Esses são algumas perguntas preparatórios para a prova de Certificação PowerUser, uma das provas iniciais da Splunk para quem precisa executar tarefas de criação de consultas, alertas, dashboards, etc.

* BluePrint = https://www.splunk.com/pdfs/training/Splunk-Test-Blueprint-Power-User-v.1.1.pdf
* 65 Questões, mínimo de 75% de acerto.
* Perguntas de Múltipla escolha.

### Questões de Exemplo para a prova:
Which command removes results with duplicate field values?
Resposta: **dedup**

These are booleans in the Splunk Search Language.
Resposta: **And, NOT, OR**

Which is not a comparison operator in Splunk?
Resposta: **?=**

Field values are case sensitive.
Resposta: **False**

How is the asterisk used in Splunk search?
Resposta: **As a wildcard**

Which of the following is NOT a stats function:
Resposta: **addtotals**

The search job inspector shows you how long a given search took to run.
Resposta: **TRUE**

Which of the following search modes automatically returns all extracted fields in the fields sidebar?
Resposta: **Verbose Mode**

Bucket names in Splunk indexes are used to:
Resposta: **Determine if the bucket should be searched based on the time range of the search**

When searching, field values are case:
Resposta: **Insensitive**

In this search, __________ will appear on the y-axis. SEARCH: **sourcetype=access_combined status!=200 | chart count over host**
Resposta: **count**

The ______ clause allows you to define which field is represented on the X axis of a chart.
Resposta: **over**

If a search returns _______ it can be viewed as a chart.
Resposta: **statistics**

The _____ axis should always be numeric.
Resposta: **Y**

Which type of visualization allows you to show a third dimension of data?
Resposta: **bubble chart**

Which of the following are valid options with the chart command?
Resposta: **useother** **usenull**

The iplocation and geostats commands can be used together.
Resposta: **True**

The geom command allows you to create:
Resposta: **choropleth maps**

This command will compute the sum of numeric fields within events and place the result in a new field:
Resposta: **addtotals**

Which command is used to create choropleth maps?
Resposta: **geom**

By default, the fillnull Command replaces null values with:
Resposta: **0**

What is wrong with the following search syntax: sourcetype=vendor_sales | eval SalesTerritory = if((VendorID >= 7000 AND VendorID < 8000), Asia, "Rest of the World") | stats sum(price) as TotalRevenue by SalesTerritory
Resposta: **Asia is not in double quotes**

If the destination field for the eval command already exists, it is:
Resposta: **overwritten by the new field defined in the eval command**

You can only use one eval command per search.
Resposta: **False**

The eval command overwrites field values in the Splunk index.
Resposta: **False**

If you want to format values without changing their characteristics, which would you use?
Resposta: **The fieldformat command**

Mark the terms that fill in the blanks in the correct order: Use _____ to see results of a calculation, or group events on a field value. Use _____ to see events correlated together, or grouped by start and end values.
Resposta: **stats, transaction**

What will you learn from the results of the following search? sourcetype=cisco_esa | transaction mid, dcid, icid | timechart avg(duration)
Resposta: **The average time elapsed during each transaction for all transactions**

You can create a transaction based on multiple fields.
Resposta: **True**

The maxpause definition:
Resposta: **Finds groups of events where the span of time between included events does not exceed a specific value**

Which of these is NOT a field that is automatically created with the transaction command?
Resposta: **maxcount**

The transaction command allows you to _________ events across multiple sources.
Resposta: **correlate**

### Materiais de Apoio:
* Commonly Used Search Commands: https://docs.splunk.com/Documentation/Splunk/latest/Search/GetstartedwithSearch
* Search Job Inspector: https://docs.splunk.com/Documentation/Splunk/latest/Search/ViewsearchjobpropertieswiththeJobInspector
* Creating Custom Visualizations: https://docs.splunk.com/Documentation/Splunk/latest/AdvancedDev/CustomVizDevOverview
* Transaction Command Definitions: https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Transaction
