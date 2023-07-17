from read_data import read_data
import data
def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    x=0
    for i in data['messages']:
        if i['type']=='message':
            x+=1
    return x
data=read_data('data/result.json')
print(find_number_of_messages(data))