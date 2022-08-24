cars = ['nissan', 'toyota', 'ford', 'honda']

print(cars.index('honda'))

if 'honda' in cars:
    cars.remove('honda')

cars.insert(0, 'daewoo')
cars.append('gmc')

cars.pop(0)
print(cars)

# Extending

european_cars = ['vw', 'audi', 'bmw']

cars.extend(european_cars)
cars.sort(reverse=True)
print(cars)

new_cars = cars.copy()
print(new_cars)

new_cars.clear()
print(new_cars)
new_cars.append('tata')
print(new_cars[0])
