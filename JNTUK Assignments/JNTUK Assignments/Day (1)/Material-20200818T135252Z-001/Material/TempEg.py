temps = []
temps = [32.1, 35.2, 31.5,29.6,41.9,25.8, ]

for val in temps:
    print(val)

temps.sort(reverse=True)

temps1 = temps[:2]

temps2 = temps[-2:]

tempsa = [31.6,40.1,26.8]

print("After sorting: Maximum two temperatures")

for val in temps[-2:]:
    print(val)

tempsa.extend(temps)

for val in tempsa[:]:
    print(val)