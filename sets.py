items = {1, 2, 'ben', 2, 32, 4, 4, 5, 5, 6}
print(items)

items.update([3, 6, 7])
print(items)

items.discard('ben')
print(items)
# items.remove(11)

items.pop()
print(items)

print(32 in items)

if 32 in items:
    items.remove(32)
    items.update([9])

print(items)

new_items = set(range(20))
print(new_items)

u = new_items.union(items)
print(u)

i = new_items.intersection(items)
print(i)

d = new_items.difference(items)
print(d)

sd = new_items.symmetric_difference(items)
print(sd)