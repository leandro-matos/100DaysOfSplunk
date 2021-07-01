
# Splunk-Power-User

Esses são algumas perguntas preparatórios para a prova de Certificação PowerUser, uma das provas iniciais da Splunk para quem precisa executar tarefas de criação de consultas, alertas, dashboards, etc.

* BluePrint = https://www.splunk.com/pdfs/training/Splunk-Test-Blueprint-Power-User-v.1.1.pdf
* 65 Questões, mínimo de 75% de acerto.
* Perguntas de Múltipla escolha.

### Questões de Exemplo para a prova:
- The _____ function of the eval command can take multiple boolean arguments.
    - Resposta: **case**

- Which of these search strings is NOT valid:
    - Resposta: **index=web status=50* | chart count over host, status**

- datasets can be added to a root dataset to narrow down the search
    - Resposta: **event**

- can share a knowledge object across all apps.
    - Resposta: **Administrators**

- Splunk suggests naming your Knowledge Objects using _______ segmented keys.
    - Resposta: **6**

- The eval command 'if' function requires the following three arguments (in order):
    - Resposta: **boolean expression, result if true, result if false**

- Which function should you use with the transaction command to set the maximum total time between the earliest and latest events returned?
    - Resposta: **maxspan**

- The trendline command requires the following three arguments:
    - Resposta: **trend type, time period, and field**

- The gauge command:
    - Resposta: **allows you to set colored ranges for a single-value visualization.**

- Warm buckets in Splunk indexes are named by:
    - Resposta: **the timestamps of first and last event in the bucket**

- Time is the most efficient filter you can apply to a search.
    - Resposta: **True**

- How many results are shown by default when using a Top or Rare Command?
    - Resposta: **10**

- Which command removes results with duplicate field values?
    - Resposta: **dedup**

- These are booleans in the Splunk Search Language.
    - Resposta: **And, NOT, OR**

- Which is not a comparison operator in Splunk?
    - Resposta: **?=**

- Field values are case sensitive.
    - Resposta: **False**

- How is the asterisk used in Splunk search?
    - Resposta: **As a wildcard**

- Which of the following is NOT a stats function:
    - Resposta: **addtotals**

- The search job inspector shows you how long a given search took to run.
    - Resposta: **TRUE**

- Which of the following search modes automatically returns all extracted fields in the fields sidebar?
    - Resposta: **Verbose Mode**

- Bucket names in Splunk indexes are used to:
    - Resposta: **Determine if the bucket should be searched based on the time range of the search**

- When searching, field values are case:
    - Resposta: **Insensitive**

- In this search, __________ will appear on the y-axis. SEARCH: **sourcetype=access_combined status!=200 | chart count over host**
    - Resposta: **count**

- The ______ clause allows you to define which field is represented on the X axis of a chart.
    - Resposta: **over**

- If a search returns _______ it can be viewed as a chart.
    - Resposta: **statistics**

- The _____ axis should always be numeric.
    - Resposta: **Y**

- Which type of visualization allows you to show a third dimension of data?
    - Resposta: **bubble chart**

- Which of the following are valid options with the chart command?
    - Resposta: **useother** **usenull**

- The iplocation and geostats commands can be used together.
    - Resposta: **True**

- The geom command allows you to create:
    - Resposta: **choropleth maps**

- This command will compute the sum of numeric fields within events and place the result in a new field:
    - Resposta: **addtotals**

- Which command is used to create choropleth maps?
    - Resposta: **geom**

- By default, the fillnull Command replaces null values with:
    - Resposta: **0**

- What is wrong with the following search syntax: 
    - sourcetype=vendor_sales | eval SalesTerritory = if((VendorID >= 7000 AND VendorID < 8000), Asia, "Rest of the World") | stats sum(price) as TotalRevenue by SalesTerritory
    - Resposta: **Asia is not in double quotes**

- If the destination field for the eval command already exists, it is:
    - Resposta: **overwritten by the new field defined in the eval command**

- You can only use one eval command per search.
    - Resposta: **False**

- The eval command overwrites field values in the Splunk index.
    - Resposta: **False**

- If you want to format values without changing their characteristics, which would you use?
    - Resposta: **The fieldformat command**

- Mark the terms that fill in the blanks in the correct order: Use _____ to see results of a calculation, or group events on a field value. Use _____ to see events correlated together, or grouped by start and end values.
    - Resposta: **stats, transaction**

- What will you learn from the results of the following search? sourcetype=cisco_esa | transaction mid, dcid, icid | timechart avg(duration)
    - Resposta: **The average time elapsed during each transaction for all transactions**

- You can create a transaction based on multiple fields.
    - Resposta: **True**

- The maxpause definition:
    - Resposta: **Finds groups of events where the span of time between included events does not exceed a specific value**

- Which of these is NOT a field that is automatically created with the transaction command?
    - Resposta: **maxcount**

- The transaction command allows you to _________ events across multiple sources.
    - Resposta: **correlate**

- Knowledge Objects can be used to normalize data.
    - Resposta: **True**

- What are the predefined ways Knowledge Objects can be shared?
    - Resposta: **Specific App, Private e All Apps**

- Which users can create private Knowledge Objects?
    - Resposta: **User, Admin e Power**

- Knowledge Objects should be named as generically as possible.
    - Resposta: **False**

- When a user creates a Knowledge Object it is automatically set to _________.
    - Resposta: **Private**

- When extracting fields, we may choose to use our own regular expressions.
    - Resposta: **True**

- In the Field Extractor Utility, this button will display events that do not contain extracted fields.
    - Resposta: **Non-Matches**

- After editing your regular expression from the Field Extractor Utility, you will be returned to the utility.
    - Resposta: **False**

- Once a field is created using the regex method, you cannot modify the underlying regular expression.
    - Resposta: **False**

- The field extractor utility allows you to extract fields using the following two methods:
    - Resposta: **regex and delimiter**

- Fields extracted with the Field Extractor:
    - Resposta: **Are specific to a host, source or sourcetype; Are persistent**

- During the validation step of the Field Extractor workflow:
    - Resposta: **You can remove values that aren't a match for the field you want to define**

- How many ways are there to access the Field Extractor Utility?
    - Resposta: **3**

- A field can only have one field alias.
    - Resposta: **False**

- Field aliases can only be applied to a single source type, source, or host.
    - Resposta: **False**

- Calculated fields are based on underlying:
    - Resposta: **eval expressions**

- Once a field alias is created:
    - Resposta: **You can still use the original field name to search**

- Field aliases are used to _____ data.
    - Resposta: **normalize**

- Event Types do not show up in the Fields List.
    - Resposta: **False**

- Tags can be added to Event Types.
    - Resposta: **True**

- These allow you to categorize events based on search terms.
    - Resposta: **Event Types**

- Which search would limit an "alert" tag to the "host" field?
    - Resposta: **tag::host=alert**

- You can only add one tag per field value pair.
    - Resposta: **False**

- Tags are descriptive names for ____________.
    - Resposta: **Key Value Pairs**

- You can pipe the results of a macro to other commands
    - Resposta: **True**

- Search macros:
    - Resposta: **Can pass arguments to the search**
    - Resposta: **Are time-range independent**
    - Resposta: **Allow you to store entire search strings, including pipes and eval statements**

- What is the correct way to name a macro with two arguments?
    - Resposta: **us_sales(2)**

- The search expansion tool:
    - Resposta: **Allows you to see what a macro will expand to before you run a search.**

- What is the proper syntax for using a macro named "us_sales"
    - Resposta: **`us_sales`**

- The number of arguments in a macro must be included in the macro name.
    - Resposta: **True**

- Workflow Actions can only be applied to a single field.
    - Resposta: **False**

- To use field value data from an event in a Workflow Action, we need to:
    - Resposta: **Wrap the field in dollar signs.**

- This Workflow Action type directs users to a specified URI.
    - Resposta: **GET**

- A Workflow action can:
    - Resposta: **Send field values to external sources.**
    - Resposta: **Execute a secondary search**
    - Resposta: **Direct users to a specified URI**

- When using a field value variable with a Workflow Action, which punctuation mark will escape the data?
    - Resposta: **!**

- This Workflow Action type sends field values to external resources.
    - Resposta: **POST**

- Required fields in a data model:
    - Resposta: **constrains the dataset to only return events that include that field**

- Which of these are NOT Data Model dataset types:
    - Resposta: **Lookups**

- The only way to access and use a dataset is from the Pivot interface.
    - Resposta: **False**

- Hidden fields in a data model:
    - Resposta: **will not be displayed to a Pivot user, but can be used to define other datasets**

- Fields used in Data Models must already be extracted before creating the datasets.
    - Resposta: **False**

- This role is required to install the CIM Add-on.
    - Resposta: **ADMIN**

- The CIM Add-on indexes extra data and will affect license usage.
    - Resposta: **False**

- By default, data models in the CIM Add-on will search across all indexes.
    - Resposta: **True**

- You can normalize data for CIM use:
    - Resposta: **Using Knowledge Objects**
    - Resposta: **At Index Time**

- The Splunk CIM Add-on includes data models in a __________ format.
    - Resposta: **JSON**

- The data models in the CIM Add-on are accelerated by default.
    - Resposta: **False**

- The CIM schema should be used when creating Field Extractions, Aliases, Event Types, and Tags.
    - Resposta: **True**

### Materiais de Apoio:
* Commonly Used Search Commands: shorturl.at/tNSUZ
* Search Job Inspector: shorturl.at/kJOY4
* Creating Custom Visualizations: shorturl.at/aorR7
* Transaction Command Definitions: shorturl.at/clBEQ
* Recommended Naming Convention: shorturl.at/wFG08
* Splunk Regular Expressions: shorturl.at/tzBM2
* Accelerating Data Models: shorturl.at/tvDQ9
* Splunk CIM add-on: https://splunkbase.splunk.com/app/1621/
* CIM Reference Tables: shorturl.at/zCL06
* CIM Documentation: shorturl.at/hnvxG