

def get_messages():
    """
    Fetch all imessages 
    """
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


def get_messages_df(): 
    """
    Put messages into pandas df and save file for use outside of 'message' kernel 
    """

    data = {'Name':['Kellyn', 'Faith', 'Mary Caroline', 'Claire', 'Megan', 'Bella', 'Dulce', 'Julia'],
            'Messages':[Kellyn, Faith, Mary_Caroline, Claire, Megan, Bella, Dulce, Julia]}
    df1= pd.DataFrame(data)

    df1.to_csv(r'/Users/casonberkenstock/Project4/Messages.csv', index = False)

    df2= pd.read_csv('/Users/casonberkenstock/Project4/Messages.csv')
    
    return df2

df2= get_messages_df()