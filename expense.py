import csv
from PyInquirer import prompt

def get_user(answer):
    options = []
    with open('user.csv', newline='') as csvfile:
        res = csv.reader(csvfile)
        for a in res:
            i = 0
            options.append(a[i])
            i +=1
    return options 


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_user,
    },

]


def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯

    file = 'expenses.csv'
    with open(file, 'a', newline='') as csvfile:
        res = csv.writer(csvfile, delimiter=' ',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        res.writerow(['amount : ' + infos['amount'], 'label : ' + infos['label'],'spender : ' + infos['spender']])
        


    print("Expense Added !")
    return True


