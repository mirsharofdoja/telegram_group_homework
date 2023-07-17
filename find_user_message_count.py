from read_data import read_data
from find_all_users_id import find_all_users_id
import data
def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    data1=dict()
    for user in users_id:
        x=0
        for message in data['messages']:
            if message['type']=='message' and message['from_id']==user:
                x+=1
        data1[user]=x
    return data1
x=read_data('data/result.json')
print(find_user_message_count(x,find_all_users_id(x)))