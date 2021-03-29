def get_names(peoples_list):
    '''
    Function to get all names in a list with dictionaries
    :param peoples_list: list with peoples data
    :return: list with all names
    '''
    for people in peoples_list:
        names_list.append(people['name'])
    return names_list


def search_obese(peoples_list):
    '''
    Function to get people with BMI higher than 30 in as list with dictionaries
    :param peoples_list: list with peoples data
    :return: list with obese people
    '''
    for people in peoples_list:
        if people['bmi'] >= 30:
            people_with_obesity.append(people)
    return people_with_obesity


peoples = [{'name': 'Joao', 'bmi': 27},
         {'name': 'Cleiton', 'bmi': 21},
         {'name': 'Julia', 'bmi': 16},
         {'name': 'Carlos', 'bmi': 43},
         {'name': 'Daniela', 'bmi': 31}
]

#Geting names
names_list = []
names_list = get_names(peoples_list=peoples)
other_names_list = get_names(peoples_list=peoples)
print(f'Names: {names_list}')
print(f'Other names: {other_names_list}')

#Geting people with obesity
people_with_obesity = []
people_with_obesity = search_obese(peoples_list=peoples)
other_people_with_obesity = search_obese(peoples_list=peoples)
print(f'Peoples with obesity: {people_with_obesity}')
print(f'Other peoples with obesity: {other_people_with_obesity}')

#Geting higher BMI
bmi_list = []
for people in peoples:
    if people['bmi'] >= 30:
        bmi_list.append(int(people['bmi']))
higher_bmi = 0
for bmi in bmi_list:
    if higher_bmi < bmi:
        higher_bmi = bmi
print(f'Higher BMI: {higher_bmi}')
