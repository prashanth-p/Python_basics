## 3. Read the File Into a String ##

dq_ptr = open('dq_unisex_names.csv','r')
names = dq_ptr.read()


## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []

for name in names_list:
    comma_list = name.split(",")
    nested_list.append(comma_list)
    
print(nested_list)
    
for x in range(0,5):
    print(nested_list[x])
    

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list = []
#unisex_list = []


for row in nested_list:
    y = row[0]
    x = float(row[1])
    z = [y,x]
    # numerical_list.append(y)
    numerical_list.append(z)
    
for x in range(0,5):
    print(numerical_list[x])

## 7. Filter the List ##

# The last value is ~100 people
thousand_or_greater = []

for names in numerical_list:
    if (names[1]>=1000):
        thousand_or_greater.append(names[0])
        
#for i in range(0,10):
print(thousand_or_greater[0:10])
    

# numerical_list[len(numerical_list)-1]