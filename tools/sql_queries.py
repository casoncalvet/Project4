import sys
sys.path.append('../')

from config.sql_connection import engine
import pandas as pd
import spacy
from spacy import displacy
NER = spacy.load("en_core_web_sm")


def entities_recognition (raw_text):
    dict_ = {}
    text1= NER(raw_text)
    for word in text1.ents:
        dict_[word.label_] = word.text
    return dict_



def get_all ():
    query = """SELECT * FROM iMessages;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient='records')


def get_entities ():
    query = """SELECT * FROM iMessages;"""
    df = pd.read_sql_query(query, engine)
    df['entities'] = df['Messages'].apply(entities_recognition)
    df_2 = df[['Name', 'entities']]
    return df_2.to_dict(orient='records')


def get_everything_from_person (name):
    query = f"""SELECT * 
    FROM iMessages
    WHERE Name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_freq(): 
    query= f"""
    SELECT * 
    FROM iMessages;
    """
    df= pd.read_sql_query(query, engine)
    
    df.set_index('Name', inplace= True, drop= True)
    SERIES= df['Messages'].apply(len)

    Freqdf= pd.DataFrame(SERIES)

    total= 0
    new=[]
    for i in SERIES: 
        total += i
    for i in SERIES:
        new.append(i/total)
    Freqdf['Frequency'] = new 
    Freqdf.reset_index(inplace= True, drop= False)

    return Freqdf.to_dict(orient="records")
    

def tokenizer(dataFrme): 
    import re
    nlp  = spacy.load("en_core_web_sm")
    stop = nlp.Defaults.stop_words
    dataFrme[dataFrme.columns[1]+'_clean'] = ''
    
    for i in dataFrme.index:
        new_list = []
        for element in dataFrme.loc[i][dataFrme.columns[1]].split(','):
            if element not in stop:
                new_list.append(element)
        string_without_stop = " ".join(new_list)
        dataFrme.loc[i][dataFrme.columns[1]] = string_without_stop
        
        ### 2nd part
        filtered=[]
        for token in nlp(string_without_stop):
            lemma = token.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma): # This will remove the question marks
                filtered.append(lemma)
        dataFrme.loc[i][dataFrme.columns[1]+'_clean'] = " ".join(filtered)
        
    return dataFrme

def get_Sentiment(): 
    query= f"""
    SELECT * 
    FROM iMessages;
    """ 
    from textblob import TextBlob
    df= pd.read_sql_query(query, engine)
    df= tokenizer(df)
    df.set_index('Name', drop= True, inplace= True)
    new_dict= {}
    for i in df.index:  
        new_dict[i]= TextBlob(df.loc[i][df.columns[0]]).sentiment
    listy= list(new_dict.values())
    df['Polarity, Subjectivity']= listy
    df.reset_index(drop= False, inplace= True)
    return df[['Name','Polarity, Subjectivity']].to_dict(orient="records")


def insert_one_row (Name, Message):
    query = f"""INSERT INTO iMessages
     (Name, Messages) 
        VALUES ('{Name}', '{Message}');
    """
    engine.execute(query)
    return f"Correctly introduced!"



# sia by person
# length by person
# frequency of words by person
# entities recognition
