## 1. Overview ##

f = open('movie_metadata.csv','r')
movies_data = f.read()
movies_data_list = movies_data.split('\n')

movie_data = []
for movie in movies_data_list:
    x = movie.split(",")
    movie_data.append(x)
    
for i in range(0,6):
    print(movie_data[i])

## 3. Writing Our Own Functions ##

#print(movie_data)
def first_elmnts(input_lst):
    first = []
    for each in input_lst:
        first.append(each[0])
    return first


movie_names = first_elmnts(movie_data)
print(movie_names[0:5])
    


 
    


## 4. Functions with Multiple Return Paths ##


def is_usa(test):
    #for each in test:
    #for i in range(0,3):
        if (test[6] == "USA"):
            return True
        else:
            return False
        

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
wonder_woman_usa = is_usa(wonder_woman)
print(wonder_woman_usa)

## 5. Functions with Multiple Arguments ##


def index_equals_str(input_lst,index,input_str):
    if(input_lst[index] == input_str):
        return True
    else:
        return False


wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

wonder_woman_in_color = index_equals_str(input_lst=wonder_woman, index = 2, input_str = "Color")

print(wonder_woman_in_color)

## 6. Optional Arguments ##

   
def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt


def feature_counter(input_lst):
    us_movies = []
    for each in input_lst:
        test  = index_equals_str(each, index=6, input_str="USA")
        if( test == True):
            us_movies.append(test)
    num_of_us_movies = counter(input_lst=us_movies)
    return num_of_us_movies

num_of_us_movies = feature_counter(movie_data)

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if (each[index] == input_str):
            num_elt = num_elt + 1
    return num_elt
                  
def summary_statistics(input_lst):
    num_japan_films = feature_counter(input_lst, index=6, input_str="Japan", header_row=True)
    num_color_films = feature_counter(input_lst, index=2, input_str="Color", header_row=True)
    num_films_in_english = feature_counter(input_lst, index=5, input_str="English", header_row=True)
    
    summary = {"japan_films" : num_japan_films, 
               "color_films" : num_color_films,
               "films_in_english" : num_films_in_english}
    return summary

summary = summary_statistics(movie_data)
print(summary)


