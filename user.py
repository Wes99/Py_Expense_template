import csv
from PyInquirer import prompt

user_questions = [
     {
        'type': 'input',
        'name': 'name',
        'message': 'What\'s your name',
    }
]

def add_user():
    user_infos = prompt(user_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯

    file = 'user.csv'
    with open(file, 'a', newline='') as csvfile:
        res = csv.writer(csvfile)
        res.writerow([user_infos['name']])
        
    print("User Added !")
    return True