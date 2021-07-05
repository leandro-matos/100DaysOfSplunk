
### Comandos de Instalação do Splunk em ambiente Linux:
```
wget -O splunk-8.2.0-e053ef3c985f-Linux-x86_64.tgz
'https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=8.2.0&product=s
plunk&filename=splunk-8.2.0-e053ef3c985f-Linux-x86_64.tgz&wget=true'

sudo tar –zxvf file.tgz –C /opt

Validação da instalação/serviço (Validar serviços e path)

Validações de Portas - nc (Verificar portas no FW da máquina)

Validação de acesso (Validar portas 443, 8000, 8089, 9997)

cd $SPLUNK_HOME/bin

./splunk start
```


### Comandos de Instalação do SplunkForwarder em ambiente Linux:
```
wget -O splunkforwarder-8.1.3-63079c59e632-Linux-x86_64.tgz
'https://www.splunk.com/bin/splunk/DownloadActivityServlet?architecture=x86_64&platform=linux&version=8.1.3&produ
ct=universalforwarder&filename=splunkforwarder-8.1.3-63079c59e632-Linux-x86_64.tgz&wget=true'

wget –O splunkforwarder-8.1.3-63079c59e632-Linux-x86_64.tgz.md5
'https://download.splunk.com/products/universalforwarder/releases/8.1.3/linux/splunkforwarder-8.1.3-63079c59e632-Linux-x86_64.tgz.md5'

md5sum splunkforwarder-8.1.3-63079c59e632-Linux-x86_64.tgz splunkforwarder-8.1.3-63079c59e632-Linuxx86_64.tgz.md5 > splunkuf.md5
md5sum -c splunkuf.md5

sudo tar –zxvf splunkforwarder-8.1.3-63079c59e632-Linux-x86_64.tgz –C /opt

cd /opt/splunkfowarder/bin
./splunk start --accept-license
export SPLUNK_HOME='/opt/splunkforwarder/bin’

nc -z -v hostname/IP 22
sudo ./splunk set deploy-poll splunk-server:8089
sudo ./splunk add forward-server splunk-server:9997
sudo ./splunk add monitor /var/log
```

### Searchs de Exemplos

Pesquisa Densa
```
index=access_combined status_code=200 | stats count by host, URL, status_code
```

Cálculo
```
index="main" sourcetype="access_combined_curso“ | eval KB=bytes/1024
```

String de pesquisa combinada:
```
index="main" 
| eval KB=bytes/1024 
| eval http_response=if(status!=200,"Error","OK") 
| eval port=(random() % 10000) + 1
| eval connection = clientip.":".port
```

Cálculo e renomeação de campos
```
index="curso" sourcetype="access_combined_curso“ | stats avg(bytes) AS "Avg Bytes“
```

Cálculos estátisticos múltiplos:
```
index="curso" | stats avg(bytes) AS "Avg Bytes", sparkline(avg(bytes)) AS BYtes_Trend min(bytes), max(bytes)
```

Uso de outro campo:
```
index="curso" | stats avg(bytes) AS "Avg Bytes", sparkline(avg(bytes)) AS BYtes_Trend min(bytes), max(bytes) by clientip
```

Estátisticas na linha do tempo:
```
index="curso" sourcetype="access_combined_curso“ | timechart avg(bytes)
```

Adição de linha de tendência:
```
index="curso" sourcetype="access_combined_curso“ | timechart avg(bytes) as bytes | trendline sma5(bytes)
```

Adição de linha de predição:
```
index="curso" sourcetype="access_combined_curso“ | timechart avg(bytes) as bytes | predict future_timespan=5 bytes
```

Enriquecendo com lookups:
```
index="curso" | head 10 | lookup http_response_status_code.csv status 
| lookup http_response_status_code.csv status OUTPUT status_type | stats count by status_type
```

Inception!:
```
index="curso" sourcetype="access_combined_curso“
| search index="curso" sourcetype="access_combined_curso“
| stats sum(bytes) AS total_bytes by clientip
| sort - total_bytes
| head 1
| return clientip ]
| stats count by clientip status uri
| sort – count
```

Adicionando múltiplas consultas:
```
index="curso" sourcetype="access_combined_curso”
| timechart span=15s avg(bytes) as avg_bytes
| appendcols [ search index="curso” sourcetype="access_combined_curso“
| stats stdev(bytes) as stdev_bytes ]
| eval 2stdv_upper = avg_bytes + stdev_bytes*2 | filldown 2stdv_upper
| eval 2stdv_lower = avg_bytes - stdev_bytes*2 | filldown 2stdv_lower
| eval 2stdv_lower = if('2stdv_lower' < 0, 0, '2stdv_lower’)
| fields - stdev_bytes
```

Definindo Lat/Lon:
```
index="curso" sourcetype="access_combined_curso"
| iplocation clientip
```

Visualizando estatísticas geográficas
```
index="curso" sourcetype="access_combined_curso"
| iplocation clientip
| geostats sum(bytes) by Country
```

Usando choropleths customizados:
```
index="curso" sourcetype="access_combined_curso"
| iplocation clientip
| stats count by Country
| geom geo_countries featureIdField="Country“
```

Rastreando movimento de objetos:
```
index="curso" sourcetype="access_combined_curso"
| iplocation clientip
| rename lat AS latitude, lon AS longitude
| table _time, latitude, longitude useragent
```

Rastreando movimento de objetos - 2:
```
| inputlookup locations.csv
| table _time latitude longitude user
| sort -_time
```

Agrupamento de transações:
```
index="curso" sourcetype="access_combined_curso“
| transaction clientip
```

Calculando a duração das sessões:
```
index="curso" sourcetype="access_combined_curso“
| transaction clientip
| stats min(duration), max(duration), avg(duration)
```

Uso de estatísticas – Sempre melhor:
```
index="curso" sourcetype="access_combined_curso“
| stats min(_time) AS earliest, max(_time) AS latest by clientip
| eval duration=latest-earliest
| stats min(duration), max(duration), avg(duration)
```

Pesquisando dados mais/menos comuns – 3 eventos mais recentes:
```
index=curso sourcetype="st_json_curso"
| cluster showcount=true t=0.7 labelonly=true
| table _time, cluster_count, cluster_label, _raw
| dedup 3 cluster_label
| sort -cluster_count, cluster_label, - _time
```

Apresentando um sumário dos campos:
```
index=curso sourcetype="access_combined_curso"
| fields - date* source* time*
| fieldsummary maxvals=5
```

Apresentando padrões de co-correlação de campos:
```
index=curso sourcetype="access_combined_curso”
| fields - date* source* time*
| correlate
```

Análise de relacionamento entre campos:
```
index=curso sourcetype="access_combined_curso“
| contingency uri status
```

Identifique predições de campos:
```
index=curso sourcetype="st_json_curso“
| analyzefields classfield=crime_number
```

Streamstats - Valor estatístico
```
index=curso sourcetype="st_json_curso“
| streamstats count | stats min(count) as begin max(count) as end by action
``` 