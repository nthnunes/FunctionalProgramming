from functools import reduce


def search_obese(peoples_list):
    '''
    Function to search people with obesity in a list with dictionaries
    :param peoples_list: list with peoples data
    :return: list with obeses
    '''
    obese = []
    if peoples_list['bmi'] >= 30:
        obese.append(peoples_list)
    return obese


def get_all_bmi(peoples_list):
    '''
    Function to get all BMIs in a list with dictionaries
    :param peoples_list: list with peoples data
    :return: list with all BMIs
    '''
    new_imc_list = []
    for people in peoples_list:
        if people['bmi'] >= 30:
            new_imc_list.append(int(people['bmi']))
    return new_imc_list


peoples = [{'name': 'Joao', 'bmi': 27},
         {'name': 'Cleiton', 'bmi': 21},
         {'name': 'Julia', 'bmi': 16},
         {'name': 'Carlos', 'bmi': 43},
         {'name': 'Daniela', 'bmi': 31}
]

#Geting names using map()
names_list = list(map(lambda p: p['name'], peoples))
other_names_list = list(map(lambda p: p['name'], peoples))

print(f'Names: {names_list}')
print(f'Other names: {other_names_list}')


#Geting people with obesity using list()
people_with_obesity = list(filter(search_obese, peoples))
other_people_with_obesity = list(filter(search_obese, peoples))
print(f'Peoples with obesity: {people_with_obesity}')
print(f'Other peoples with obesity: {other_people_with_obesity}')

#Geting higher BMI using reduce()
bmi_list = list(map(lambda p: p['bmi'], peoples))
higher_bmi = reduce(lambda a, b: a if a > b else b, bmi_list)
print(f'Higher BMI: {higher_bmi}')
