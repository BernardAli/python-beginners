car = {'make': 'Nissan', "model": "Sentra", "year": 2022}
print(car.items())
print(car.keys())
print(car.values())

car['country'] = "Japan"


print(f"Name: {car['make']}")
print("model" in car.keys())
print(car)

del car['country']
print(car)

for key in car.keys():
    print(key, car[key])