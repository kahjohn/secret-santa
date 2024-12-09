import numpy as np
import pandas as pd
import random

#If the list is taken from a Google spreadsheet
def get_list(file):
    """Get the list of participants from a single column csv file"""
    # participants = pandas.read_csv(file, header=None, 
    #                                names=np.array(['Names']), encoding='utf-8')
    # participants = list(participants['Names'])
    participants = file
    return (participants)

def get_special_code(final_list):

    random.seed(1234)
    special_code = []

    # Generate a random 5-digit number

    for i in range(0,len(final_list)):
        random_number = random.randint(10000, 99999)
        special_code.append(random_number)

    return special_code

def get_secret_santa(participants):
    """Generate a draw from a list of participants using numpy arrays and random methods
    to define who offers/receives a gift to/from whom """
    to_pickup = np.array([participants.index(name) for name in participants])  #Int paired with each participant
    print(str(len(to_pickup))+' participants')

    #Initialisation tirage au sort
    pickedup = np.array([])
    results = ""
    results_raw = []

    np.random.seed(6666)
    r = np.random.choice(to_pickup)
    print("picked-up first: " + participants[r] + '(' + str(r) + ')' + '\n')
    to_pickup = np.delete(to_pickup, np.where(to_pickup == r))
    pickedup = np.append(pickedup, r)

    #Who offers to who
    for person in to_pickup:  #N-1 tirages au sort pour N participants
        r = np.random.choice(to_pickup)
        pickedup = np.append(pickedup, r)
        to_pickup = np.delete(to_pickup, np.where(to_pickup == r))
        results = results + participants[int(pickedup.item(-2))] + ' offers to ' + participants[r] + '\n'
        # print([participants[int(pickedup.item(-2))], participants[r]])
        results_raw.append(list([participants[int(pickedup.item(-2))], participants[r]]))

    #Final - results + last picked up offers to first picked-up
    results = results + 'And ' + participants[int(pickedup.item(-1))] + ' offers to ' + participants[int(pickedup.item(0))] + '\n'
    results_raw.append(list([participants[int(pickedup.item(-1))], participants[int(pickedup.item(0))]]))
    # print([participants[int(pickedup.item(-2))], participants[r]])

    # print(results)
    # print(results_raw)
    
    # #Copy in the clipboard
    # pyperclip.copy(results)
    # clipboard = pyperclip.paste()
    # print('Results of the draw copied in the clipboard')

    return results_raw

participant_list = ['L Y CHING','L W NIE','N S HWA','C W ZHE','L K WHY','L S LING','C H YAN','C C CHONG','L Y LENG','L Y LEE','L J SHENG','L K JOHN','L Y MOOI','L J NIE','L Y YEN']

lst = get_list(participant_list)
# print(lst)

final = get_secret_santa(lst)
# print(final)

code = get_special_code(lst)
# print(code)

tbl1 = pd.DataFrame(final, columns=['Santa','Recipient'])
tbl2 = pd.DataFrame(code, columns=['Code'])

tbl = pd.merge(tbl1, tbl2, how='left', left_index=True, right_index=True)
print(tbl[['Santa','Code']])

tbl.to_csv('/workspaces/secret-santa/santa.csv', index=False)