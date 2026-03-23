temperatures = {
    "delhi": 21,
    "pune": 16,
    "bangalore": 28,
    "chennai": 35
}

for key in temperatures:
    print(f"{key} -> {temperatures[key]}")
    
for value in temperatures.values():
    print(value)
    
for key,value in temperatures.items():
    print(f"{key} -> {value}")
    
