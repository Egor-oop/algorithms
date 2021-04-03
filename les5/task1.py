from collections import defaultdict


def company():
    company_dict = defaultdict(int)
    how_many_company = int(input('Введите кол-во компаний: '))
    how_many_company_backup = how_many_company
    while how_many_company > 0:
        company_name = input('Введите название компании: ')
        company_salary = input(f'Введите доход компании {company_name} в 4 квартала: ')
        company_salary_no_spaces = company_salary.replace(' ', '')
        company_dict[company_name] = int(company_salary_no_spaces)
        how_many_company -= 1
    mid_salary = sum(company_dict.values()) / how_many_company_backup
    for i in company_dict:
        if company_dict.get(i) >= mid_salary:
            print(f'Зарплата компании {i} выше среднего')
        elif company_dict.get(i) < mid_salary:
            print(f'Зарплата компании {i} ниже среднего')
    return 'end'


print(company())
