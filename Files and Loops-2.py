## 2. Opening Files ##

f = open("crime_rates.csv", "r")
print(f)

## 3. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()
print(data)

## 4. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows)

## 6. Practice - Loops ##

ten_rows = rows[0:10]
for rows in ten_rows:
    print(rows)

## 7. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

## 8. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = []

for row in rows:
    a = row.split(",")
    final_data.append(a)
    
print(final_data)

## 9. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
# data_set = five_elements.split(",")
cities_list = []
crime_rates = []

for elements in five_elements:
    cities_list.append(elements[0])
    crime_rates.append(int(elements[1]))
    
print(cities_list)

## 10. Looping Through a List of Lists ##

crime_rates = []
cities_list = []

for data in final_data:
    # row is a list variable, not a string.
    city = data[0]
    # crime_rate is a string, the crime rate of the city.
    cities_list.append(city)
    
print(cities_list)

## 11. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
int_crime_rates = []

for row in rows:
    a = row.split(',')
    int_crime_rates.append(int(a[1]))

print(int_crime_rates)