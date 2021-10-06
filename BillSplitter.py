import random

print('Enter the number of friends joining (including you): ')
try:
    quantity_friends = int(input())
except (ValueError, NameError):
    print('No one is joining for the party')
if quantity_friends < 1:
    print('No one is joining for the party')
else:
    dict_temp = []
    print('Enter the name of every friend (including you), each on a new line: ')
    for i in range(quantity_friends):
        temp_name = input()
        dict_temp.append(temp_name)
    dict_names = dict.fromkeys(dict_temp, 0)
    print('Enter the total bill value:')
    common_bill = int(input())
    split_bill = round(common_bill / quantity_friends, 2)
    dict_names = dict.fromkeys(dict_names, split_bill)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    a_answer = input()
    if a_answer == "Yes":
        free_guy = random.choice(dict_temp)
        print(str(free_guy), 'is the lucky one!')
        changed_bill = round(common_bill / (quantity_friends - 1), 2)
        for names in dict_names:
            if names != free_guy:
                dict_names.update({names: changed_bill})
            else:
                dict_names.update({names: 0})
        print(dict_names)
    else:
        print('No one is going to be lucky')
        print(dict_names)
