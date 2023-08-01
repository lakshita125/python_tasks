''' Implement a function that takes a list of dictionaries , each representing a person's income and 
expenses for a month . The keys in each dictionary are "name," " income , "and " expenses . "
Calculate the savings (income-expenses) for each person and return the result as a new dictionary 
with the names as keys and savings as values '''

def calculate_savings(persons_data_list):
    savings_dict = {}
    for person in persons_data_list:
        name = person["name"]
        income = person["income"]
        expenses = person["expenses"]
        savings = income - expenses
        savings_dict[name] = savings
    return savings_dict


persons_data_list = [
    {"name": "harsh", "income": 5000, "expenses": 3000},
    {"name": "laksh", "income": 5500, "expenses": 4000},
    {"name": "nav", "income": 6000, "expenses": 4500},
]

savings_result = calculate_savings(persons_data_list)


print("Savings for each person:", savings_result)
