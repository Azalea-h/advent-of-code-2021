import statistics

with open("input.txt", "r") as f:
    f = f.readline()
    
positions = []

for position in f.split(","):
    positions.append(int(position))

destination = int(statistics.median(positions)) # Feel like using median makes sence but I need an evidence that it's right!!

total_fuel = sum([abs(position - destination) for position in positions])

print(total_fuel)


