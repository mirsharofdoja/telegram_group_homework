from read_data import read_data
import data
def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    user_name=[]
    for i in data['messages']:
        if i['type']=="service":
            if i["actor"] not in user_name:
                if i['actor_id'].startswith('user'):
                    user_name+=[i["actor"]]
        elif i['type']=="message":
            if i["from"] not in user_name:
                if i['from_id'].startswith('user'):
                    user_name+=[i["from"]]
    return user_name
data=read_data('data/result.json')
print(find_all_users_name(data))