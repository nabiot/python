

data = []
with open('congress-terms.csv', 'r') as file:
    data = file.read()
data = data.split('\n')
del data[0]

CONGRESS_INDEX = 0
FIRST_NAME_INDEX = 3
MIDDLE_NAME_INDEX = 4
LAST_NAME_INDEX = 5
AGE_INDEX = 12
counter = 0
while counter < len(data):
    data[counter] = data[counter].split(',')
    data[counter][AGE_INDEX] = float(data[counter][AGE_INDEX])
    # print("data[counter]=", data[counter])
    counter += 1
print(data)

# print counter using for loop
# grid = []
# for row in data:
#     grid.append(row.split(','))
# print(grid)

# 1. Who was the youngest person to serve, and what congress did
# they serve in?
# 2. Who was the oldest person to serve, and what congress did
# they serve in?

min_age = 1000
min_congress_number = -1
min_name = ''
max_age = 1
max_congress_number = -1
max_name = ''
for row in data:
    if row[AGE_INDEX] < min_age:
        min_age = row[AGE_INDEX]
        min_congress_number = row[CONGRESS_INDEX]
        min_name = f"{row[FIRST_NAME_INDEX]} {row[MIDDLE_NAME_INDEX]} {row[LAST_NAME_INDEX]}"
    if row[AGE_INDEX] > max_age:
        max_age = row[AGE_INDEX]
        max_congress_number = row[CONGRESS_INDEX]
        max_name = f"{row[FIRST_NAME_INDEX]} {row[MIDDLE_NAME_INDEX]} {row[LAST_NAME_INDEX]}"
# print(min_age)
# print(min_congress_number)
# print(min_name)
# print(max_age)
# print(max_congress_number)
# print(max_name)

answers = [
    [min_congress_number, str(min_age), min_name],
    [max_congress_number, str(max_age), max_name]
]
with open('answers.csv', 'w+') as file:
    for answer in answers:
        file.write(','.join(answer))
        file.write('\n')

# file.write(f"{min_congress_number},{min_age},{min_name}\n")
# file.write(f"{max_congress_number},{max_age},{max_name}")
