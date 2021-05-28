# CORRELATION
**These commands can be used to build correlation searches.**

1. append	    
   - Appends subsearch results to current results.

2. appendcols	
    - Appends the fields of the subsearch results to current results, first results to first result, second to second, etc.

3. appendpipe	
    - Appends the result of the subpipeline applied to the current result set to results.

4. arules	    
    - Finds association rules between field values.

5. associate	
    - Identifies correlations between fields.

6. contingency, 
    - counttable, ctable	Builds a contingency table for two fields.

7. correlate	
    - Calculates the correlation between different fields.

8. diff	        
    - Returns the difference between two search results.

9. join	        
    - Combines the results from the main results pipeline with the results from a subsearch.

10. lookup	    
    - Explicitly invokes field value lookups.

11. selfjoin	
    - Joins results with itself.

12. set	        
    - Performs set operations (union, diff, intersect) on subsearches.

13. stats	    
    - Provides statistics, grouped optionally by fields. See Statistical and charting functions.

14. transaction	    
    - Groups search results into transactions.



# DATA E INDEXES
**These commands can be used to learn more about your data, add and delete data sources, or manage the data in your summary indexes.**

## View data
**These commands return information about the data you have in your indexes. They do not modify your data or indexes in any way.**

15. audit	
    - Returns audit trail information that is stored in the local audit index.

16. datamodel	
    - Return information about a data model or data model object.

17. dbinspect	
    - Returns information about the specified index.

18. eventcount	
    - Returns the number of events in an index.

19. metadata	
    - Returns a list of source, sourcetypes, or hosts from a specified index or distributed search peer.

20. typeahead	
    - Returns typeahead information on a specified prefix.

## Manage data
**These are some commands you can use to add data sources to or delete specific data from your indexes.**

21. delete	
    - Delete specific events or search results.

## Manage summary indexes
**These commands are used to create and manage your summary indexes.**

22. collect, stash	
    - Puts search results into a summary index.

23. overlap	
    - Finds events in a summary index that overlap in time or have missed events.

24. sichart	
    - Summary indexing version of chart. Computes the necessary information for you to later run a chart search on the summary index.

25. sirare	
    - Summary indexing version of rare. Computes the necessary information for you to later run a rare search on the summary index.

26. sistats	
    - Summary indexing version of stats. Computes the necessary information for you to later run a stats search on the summary index.

27. sitimechart	
    - Summary indexing version of timechart. Computes the necessary information for you to later run a timechart search on the summary index.

28. sitop	
    - Summary indexing version of top. Computes the necessary information for you to later run a top search on the summary index.


# FIELDS
**These are commands you can use to add, extract, and modify fields or field values. The most useful command for manipulating fields is eval and its statistical and charting functions.**

## Add fields
**Use these commands to add new fields.**

29. accum	
    - Keeps a running total of the specified numeric field.

30. addinfo	
    - Add fields that contain common information about the current search.

31. addtotals	
    - Computes the sum of all numeric fields for each result.

32. delta	
    - Computes the difference in field value between nearby results.

33. eval	
    - Calculates an expression and puts the value into a field. See also, evaluation functions.

34. iplocation	
    - Adds location information, such as city, country, latitude, longitude, and so on, based on IP addresses.

35. lookup	
    - For configured lookup tables, explicitly invokes the field value lookup and adds fields from the lookup table to the events.

36. multikv	
    - Extracts field-values from table-formatted events.

37. rangemap	
    - Sets RANGE field to the name of the ranges that match.

38. relevancy	
    - Adds a relevancy field, which indicates how well the event matches the query.

39. strcat	
    - Concatenates string values and saves the result to a specified field.

## Extract fields
**These commands provide different ways to extract new fields from search results.**

40. erex	
    - Allows you to specify example or counter example values to automatically extract fields that have similar values.

41. extract, kv	
    - Extracts field-value pairs from search results.

42. kvform	
    - Extracts values from search results, using a form template.

43. rex	
    - Specify a Perl regular expression named groups to extract fields while you search.

44. spath	
    - Provides a straightforward means for extracting fields from structured data formats, XML and JSON.

45. xmlkv
    - Extracts XML key-value pairs.

## Modify fields and field values
**Use these commands to modify fields or their values.**

46. convert	
    - Converts field values into numerical values.

47. filldown	
    - Replaces NULL values with the last non-NULL value.

48. fillnull	
    - Replaces null values with a specified value.

49. makemv	
    - Change a specified field into a multivalue field during a search.

50. nomv	
    - Changes a specified multivalue field into a single-value field at search time.

51. reltime	
    - Converts the difference between 'now' and '_time' to a human-readable value and adds adds this value to the field, 'reltime', in your search results.

52. rename	
    - Renames a specified field. Use wildcards to specify multiple fields.

53. replace	
    - Replaces values of specified fields with a specified new value.

# FIND ANOMALIES
**These commands are used to find anomalies in your data. Either search for uncommon or outlying events and fields or cluster similar events together.**

54. analyzefields, af	
    - Analyze numerical fields for their ability to predict another discrete field.

55. anomalies	
    - Computes an "unexpectedness" score for an event.

56. anomalousvalue	
    - Finds and summarizes irregular, or uncommon, search results.

57. anomalydetection	
    - Identifies anomalous events by computing a probability for each event and then detecting unusually small probabilities.

58. cluster	
    - Clusters similar events together.

59. kmeans	
    - Performs k-means clustering on selected fields.

60. outlier	
    - Removes outlying numerical values.

61. rare	
    - Displays the least common values of a field.

# GEOGRAPHIC AND LOCATION
**These commands add geographical information to your search results.**

62. iplocation	
    - Returns location information, such as city, country, latitude, longitude, and so on, based on IP addresses.

63. geom	
    - Adds a field, named "geom", to each event. This field contains geographic data structures for polygon geometry in JSON and is used for choropleth map visualization. This command requires an external lookup with external_type=geo to be installed.

64. geomfilter	
    - Accepts two points that specify a bounding box for clipping choropleth maps. Points that fall outside of the bounding box are filtered out.

65. geostats	
    - Generate statistics which are clustered into geographical bins to be rendered on a world map.

# METRICS
**These commands work with metrics data.**

66. mcollect	
    - Converts events into metric data points and inserts the data points into a metric index on the search head.

67. meventcollect	
    - Converts events into metric data points and inserts the data points into a metric index on indexer tier.

68. mpreview, msearch	
    - Provides samples of the raw metric data points in the metric time series in your metrics indexes. Helps you troubleshoot your metrics data.

69. mstats	
    - Calculates visualization-ready statistics for the measurement, metric_name, and dimension fields in metric indexes.

# PREDICTION AND TRENDING
**These commands predict future values and calculate trendlines that can be used to create visualizations.**

70. predict	
    - Enables you to use time series algorithms to predict future values of fields.

71. trendline	
    - Computes moving averages of fields.

72. x11	
    - Enables you to determine the trend in your data by removing the seasonal pattern.

# REPORTS
**These commands are used to build transforming searches. These commands return statistical data tables that are required for charts and other kinds of data visualizations.**

73. addtotals	
    - Computes the sum of all numeric fields for each result.

74. autoregress	
    - Prepares your events for calculating the autoregression, or moving average, based on a field that you specify.

75. bin, discretize	
    - Puts continuous numerical values into discrete sets.

76. chart	
    - Returns results in a tabular output for charting. See also, Statistical and charting functions.

77. contingency, counttable, ctable	
    - Builds a contingency table for two fields.

78. correlate	
    - Calculates the correlation between different fields.

79. eventcount	
    - Returns the number of events in an index.

80. eventstats	
    - Adds summary statistics to all search results.

81. gauge	
    - Transforms results into a format suitable for display by the Gauge chart types.

82. makecontinuous	
    - Makes a field that is supposed to be the x-axis continuous (invoked by chart/timechart)

83. mstats	
    - Calculates statistics for the measurement, metric_name, and dimension fields in metric indexes.

84. outlier	
    - Removes outlying numerical values.

85. rare	
    - Displays the least common values of a field.

86. stats	
    - Provides statistics, grouped optionally by fields. See also, Statistical and charting functions.

87. streamstats	
    - Adds summary statistics to all search results in a streaming manner.

88. timechart	
    - Create a time series chart and corresponding table of statistics. See also, Statistical and charting functions.

89. top	
    - Displays the most common values of a field.

90. trendline	
    - Computes moving averages of fields.

91. tstats	
    - Performs statistical queries on indexed fields in tsidx files.

92. untable	
    - Converts results from a tabular format to a format similar to stats output. Inverse of xyseries and maketable.

93. xyseries	
    - Converts results into a format suitable for graphing.

# RESULTS
**These commands can be used to manage search results. For example, you can append one set of results with another, filter more events from the results, reformat the results, and so on.**

## Alerting
**Use this command to email the results of a search.**

94. sendemail	
    - Emails search results, either inline or as an attachment, to one or more specified email addresses.

## Appending
**Use these commands to append one set of results with another set or to itself.**

95. append	
    - Appends subsearch results to current results.

96. appendcols	
    - Appends the fields of the subsearch results to current results, first results to first result, second to second, and so on.

97. join	
    - SQL-like joining of results from the main results pipeline with the results from the subpipeline.

98. selfjoin	
    - Joins results with itself.

## Filtering
**Use these commands to remove more events or fields from your current results.**

99.  dedup	
    - Removes subsequent results that match a specified criteria.

100. fields	
    - Removes fields from search results.

101. from	
    - Retrieves data from a dataset, such as a data model dataset, a CSV lookup, a KV Store lookup, a saved search, or a table dataset.

102. mvcombine	
    - Combines events in search results that have a single differing field value into one result with a multivalue field of the differing field.

103. regex	
    - Removes results that do not match the specified regular expression.

104. searchtxn	
    - Finds transaction events within specified search constraints.

105. table	
    - Creates a table using the specified fields.

106. uniq	
    - Removes any search that is an exact duplicate with a previous result.

107. where	
    - Performs arbitrary filtering on your data. See also, Evaluation functions.

## Formatting
**Use these commands to reformat your current results.**

108. fieldformat	
    - Uses eval expressions to change the format of field values when they are rendered without changing their underlying values. Does not apply to exported data.

109. transpose	
    - Reformats rows of search results as columns. Useful for fixing X- and Y-axis display issues with charts, or for turning sets of data into a series to produce a chart.

110. untable	
    - Converts results from a tabular format to a format similar to stats output. Inverse of xyseries and maketable.

111. xyseries	
    - Converts results into a format suitable for graphing.

## Generating
**Use these commands to generate or return events.**

112. gentimes	
    - Returns results that match a time-range.

113. loadjob	
    - Loads events or results of a previously completed search job.

114. makeresults	
    - Creates a specified number of empty search results.

115. mvexpand	
    - Expands the values of a multivalue field into separate events for each value of the multivalue field.

116. savedsearch	
    - Returns the search results of a saved search.

117. search	
    - Searches indexes for matching events. This command is implicit at the start of every search pipeline that does not begin with another generating command.

## Grouping
**Use these commands to group or classify the current results.**

118. cluster	
    - Clusters similar events together.

119. kmeans	
    - Performs k-means clustering on selected fields.

120. mvexpand	
    - Expands the values of a multivalue field into separate events for each value of the multivalue field.

121. transaction	
    - Groups search results into transactions.

122. typelearner	
    - Generates suggested eventtypes.

123. typer	
    - Calculates the eventtypes for the search results.

## Reordering
**Use these commands to change the order of the current search results.**

124. head	
    - Returns the first number n of specified results.

125. reverse	
    - Reverses the order of the results.

126. sort	
    - Sorts search results by the specified fields.

127. tail	
    - Returns the last number N of specified results

## Reading
**Use these commands to read in results from external files or previous searches.**

128. inputcsv	
    - Loads search results from the specified CSV file.

129. inputlookup	
    - Loads search results from a specified static lookup table.

130. loadjob	
    - Loads events or results of a previously completed search job.

## Writing
**Use these commands to define how to output current search results.**

131. collect, stash	
    - Puts search results into a summary index.

132. meventcollect	
    - Converts events into metric data points and inserts the data points into a metric index on indexer tier.

133. mcollect	
    - Converts events into metric data points and inserts the data points into a metric index on the search head.

134. outputcsv	
    - Outputs search results to a specified CSV file.

135. outputlookup	
    - Writes search results to the specified static lookup table.

136. outputtext	
    - Ouputs the raw text field (_raw) of results into the _xml field.

137. sendemail	
    - Emails search results, either inline or as an attachment, to one or more specified email addresses.

# SEARCH

138. localop	
    - Run subsequent commands, that is all commands following this, locally and not on a remote peer.

139. map	
    - A looping operator, performs a search over each search result.

140. redistribute	
    - Invokes parallel reduce search processing to shorten the search runtime of a set of supported SPL commands.

141. search	
    - Searches indexes for matching events. This command is implicit at the start of every search pipeline that does not begin with another generating command.

142. sendemail	
    - Emails search results, either inline or as an attachment, to one or more specified email addresses.

# SUBSEARCH
**These are commands that you can use with subsearches.**

143. append	
    - Appends subsearch results to current results.

144. appendcols	
    - Appends the fields of the subsearch results to current results, first results to first result, second to second, and so on.

145. appendpipe	
    - Appends the result of the subpipeline applied to the current result set to results.

146. foreach	
    - Runs a templated streaming subsearch for each field in a wildcarded field list.

147. format	
    - Takes the results of a subsearch and formats them into a single result.

148. join	
    - Combine the results of a subsearch with the results of a main search.

149. return	
    - Specify the values to return from a subsearch.

150. set	
    - Performs set operations (union, diff, intersect) on subsearches.

# TIME 
**Use these commands to search based on time ranges or add time information to your events.**

151. gentimes	
    - Returns results that match a time-range.

152. localize	
    - Returns a list of the time ranges in which the search results were found.
    
153. reltime	
    - Converts the difference between 'now' and '_time' to a human-readable value and adds adds this value to the field, 'reltime', in your search results.