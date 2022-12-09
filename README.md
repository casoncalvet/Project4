

<h1  align="center">Building and Querying Flask API for Natural Language Processing of my friends' iMessages</h1>


<div align="center">

<br>
<br>
<br>


<h4 

<div align="left"> 
Objective: Build an API which will be used to query an SQL database containing all the messages sent to my iphone via iMessages 
</h4>


The database will be used to perform analyses on messages from each of my friends


Hypothesis: Kellyn is the most frequent (and negative) texter. 
<br>

- Motive: cause chaos in the group message 
  

<div> 

<br>
<br>

<div align="left"> 


Poject Overview
<br>

1. get_messages( ): compile desired messages into a dataframe

<br>

2. Build tokenizer( ) function to filter out natural language processing "stop words" and add to dataframe
<br>

3. Upload dataframe to SQL Workbench
<br>

4. Construct API using Flask in order to query and analyze messages. 

<br>
<br>
<br>
Use the api: http://127.0.0.1:9000
<br>
- /sql: Retrieve all from SQL database table containing iMessage data
<br>
- /sentiment: Polarity and Subjectivity of each friend using NLP 
<br>
- /name: Query by friend name
<br>
- /polarity: Get overall polarity of messages from each friend 
<br>
- /entities: Retrieve entities mentioned per friend
<br>
- /frequency: Retrieve relative frequency of texts per person 
<br>
- Insert rows using POST, with parameters 'Name' and 'Message' 

<br>
<h3  align="center">
Conlculsion: Kellyn is the most frequent and the most negative texter. Alternatively, Megan is the most 'positive' and the most subjective texter, while Dulce is the most objective. Mary Caroline is the least frequent texter. 