mtns = {
    'Everest' : '8848 meters',
    'Denali' : '6168 meters',
    'Raineer' : '4392 meters',
    'Robson' : '3954 meters',
    'Fuji' : '3776 meters'
}

print("\nElevations:")
for key in mtns:
    print(mtns[key])

print("\nInfo:")
for key in mtns:
    print(f"Mount {key} is {mtns[key]} tall.")

print()