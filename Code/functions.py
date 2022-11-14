
def get_messages ():
    fd = fetch_data.FetchData()
    messages  = fd.get_messages()
    return messages

messages= get_messages()


def get_friend(name): 
    """
    Get messages sent from friends
    """
    friends = { 'Julia': '+12545412303', 'Bella': '+19016522520', 
               'Kellyn': '+19015171741', 'Dulce': '+19015749606', 
               'Faith': '+16625010261', 'Claire': '+19012582198', 
               'Mary Caroline': '+19014814783', 'Megan': '+19016741494'}
    messages_= []
    
    for i in messages: 
        if i[0] == friends[name] and i[1] is not None : 
            messages_.append(i[1])
    return messages_

def get_messages_df (): 

    data = {'Name':['Kellyn', 'Faith', 'Mary Caroline', 'Claire', 'Megan', 'Bella', 'Dulce', 'Julia'],
            'Messages':[Kellyn, Faith, Mary_Caroline, Claire, Megan, Bella, Dulce, Julia]}
    df1= pd.DataFrame(data)

    df1.to_csv(r'/Users/casonberkenstock/Project4/Messages.csv', index = False)

    df2= pd.read_csv('/Users/casonberkenstock/Project4/Messages.csv')
    
    return df2

df2= get_messages_df()
df2= pd.read_csv('/Users/casonberkenstock/Project4/Messages.csv')

def connect_engine(): 
    """
    Connect to Project_4 db
    """
    dbName = "Project_4"
    password= 'admin'
    connection_data= f'mysql+pymysql://root:{password}@localhost/{dbName}'
    engine = sqlalc.create_engine(connection_data)
    return engine

engine= connect_engine()

def iMessages_to_sql ():
    """
    Import cleaned (tokenized) messages to SQL 
    """
    IMESSAGES= pd.read_csv('/Users/casonberkenstock/Project4/i_messages.csv', index_col='Name')
    for index, row in IMESSAGES.iterrows():
        mensaje = row['Messages_clean']
        nombre = row['Name']
        engine.execute(f"""insert into iMessages (Name, Messages) VALUES (%s, %s)""", (nombre, mensaje))

def tokenizer(dataFrme): 
    """
    Tokenize df for later use in Natural Language Processing 
    """
    nlp  = spacy.load("en_core_web_sm")
    stop = nlp.Defaults.stop_words
    dataFrme[dataFrme.columns[0]+'_clean'] = ''
    
    for i in dataFrme.index:
        new_list = []
        for element in dataFrme.loc[i][dataFrme.columns[0]].split(','):
            if element not in stop:
                new_list.append(element)
        string_without_stop = " ".join(new_list)
        dataFrme.loc[i][dataFrme.columns[0]] = string_without_stop
        
        ### 2nd part
        filtered=[]
        for token in nlp(string_without_stop):
            lemma = token.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma): # This will remove the question marks
                filtered.append(lemma)
        dataFrme.loc[i][dataFrme.columns[0]+'_clean'] = " ".join(filtered)
        
    return dataFrme

imessages= tokenizer(iMessages)

query = "SELECT * FROM iMessages"
iMessages = pd.read_sql_query(query, engine)

iMessages.to_csv('/Users/casonberkenstock/Project4/i_Messages.csv', index = True) # False: not include index

def get_sentiment(dtfr): 
    """
    Apply Sentiment Analysis Using TextBlob() to each string value in a df. Returns sentiment analysis
    """
    new_dict= {}
    for i in dtfr.index:  
        new_dict[i]= TextBlob(dtfr.loc[i][dtfr.columns[0]]).sentiment
    
    return new_dict

def get_polarity_scores(dtfr): 
    """
    Apply Polarity Analysis Using sia.polarity_scores to each string value in a df. Returns sentiment analysis
    """
    pol_dict= {}
    for i in dtfr.index:  
        pol_dict[i]= sia.polarity_scores(dtfr.loc[i][dtfr.columns[0]])
    
    return pol_dict


sent_dict= get_sentiment(iMessages)

pol_dict=get_polarity_scores(iMessages)

def Word_Cloud(df, name): 
    """
    Get word clouds for each person
    """
    #df.set_index('Name', inplace= True, drop=True)
    wordcloud= WordCloud(width=1600,height=400, max_words= 50, min_word_length=3,colormap='Set2').generate(" ".join(set(df.loc[name][0].split(" "))))
    plt.figure(figsize=(15,10), facecolor="k")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(f'../images/{name}.png', facecolor='k', bbox_inches='tight')
    plt.show();