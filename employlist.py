import random
import pandas as pd
from faker import Faker
from datetime import timedelta, date

fake = Faker()


departments = ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
genders = ['Male', 'Female']
hire_dates = [fake.date_this_decade() for _ in range(1000)]

def generate_termination_date(hire_date):
    # Случайно определяем, ушел ли сотрудник
    if random.random() > 0.7:  # 30% вероятность, что сотрудник уволился
        return hire_date + timedelta(days=random.randint(30, 1000))  # Случайная дата увольнения
    return None


data = []
for i in range(1, 1001):
    hire_date = random.choice(hire_dates)
    employee = {
        'id': i,
        'name': fake.name(),
        'department': random.choice(departments),
        'gender': random.choice(genders),
        'age': random.randint(22, 60),
        'hire_date': hire_date,
        'termination_date': generate_termination_date(hire_date)
    }
    data.append(employee)


df = pd.DataFrame(data)

df.to_csv('employees.csv', index=False)

print("CSV файл создан")
