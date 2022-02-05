d = {}

for num in range(1, 11):
    d[num] = num**2

print(d)

d = {num: num ** 2 for num in range(1, 11)}

print(d)

r1 = {'IOS': '15.4',
    'IP': '10.255.0.1',
    'hostname': 'london_r1',
    'location': '21 New Globe Walk',
    'model': '4451',
    'vendor': 'Cisco'}

lower_r1 = {key.lower(): value for key, value in r1.items()}
print(lower_r1)