## 2. Parsing the File ##

la_weather_open = open("la_weather.csv","r")
la_weather = la_weather_open.read();

la_weather_data = la_weather.split("\n")
weather_data = []

for data in la_weather_data:
    split_row = data.split(",")
    weather_data.append(split_row)

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.

# wd  = weather_data.split("\n")
weather = []

for data in weather_data:
    temp = data[1]
    weather.append(temp)
    
print(weather)

## 4. Counting the Items in a List ##

count = 0
for data in weather:
    count += 1
    
if (count == len(weather)):
    print("true")

## 5. Removing the Header ##

new_weather = weather[1:len(weather)]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals

space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for weather_type in weather_types:
    x = weather_type in new_weather
    weather_type_found.append(x)