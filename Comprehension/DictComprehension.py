import random

dict_cn = {num: num ** 2 for num in range(1, 11)}
print(f'1. {dict_cn}')

# Example 2.
data = {'IOS': '15.4',
        'IP': '10.255.0.1',
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'model': '4451',
        'vendor': 'Cisco'}

lower_r1 = {key.lower(): value for key, value in data.items()}
print(f'2. {lower_r1}')

# Example 3.
customers = ["Alex", "Bob", "Carol", "Dave", "Flow", "Katie", "Nate"]
discount_dict = {customer: random.randint(1, 100) for customer in customers}
customer_10 = {customer: discount for (customer, discount) in discount_dict.items() if discount < 30}
print(f'3. {discount_dict}')
print(f'3.1. {customer_10}')

# Example 4. Creating a dictionary of weekly tempertaures from the list of temperatures and days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_C = {30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9}
weekly_temp = {day: temp for (day, temp) in zip(days, temp_C)}
print(f'4. {weekly_temp}')  # weekly_temp["Monday"] -> 33.4
