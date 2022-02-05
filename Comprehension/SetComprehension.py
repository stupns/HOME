vlans = [10, '30', 30, 10, '56']

unique_vlans = {int(vlan) for vlan in vlans}

print(unique_vlans)