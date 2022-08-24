import json


filename = 'json.json'

out_data = dict(name='Ben', age=30, pet='Dog')
s = json.dumps(out_data)
print(f'String = {s}')

# To file
with open(filename, 'w') as f:
    json.dump(out_data, f)

# From string
in_data = json.loads(s)
print(in_data)

# From File
with open(filename, 'r') as f:
    file_data = json.load(f)

print(f'Type {type(file_data)} = {file_data}')