movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#exercise 1
def above5(dict_mov, movie_name):
    for movie in movies:
        if movie["name"] == movie_name:
            if movie["imdb"] > 5.5:
                print(True)
            else:
                print(False)
inp = input("Enter the name: ")
above5(movies, inp)


#exercise 2
def list_above5(dict_mov):
    for movie in dict_mov:
        if movie["imdb"] > 5.5:
            print(movie["name"])
list_above5(movies)


#exercise 3
def movie_category(dict_mov, category):
    for movie in dict_mov:
        if movie["category"] == category:
            print(movie["name"])
user_input = input("Enter the category: ")
movie_category(movies, user_input)


#exercise 4
def avg_imdb(dict_mov):
    sum = 0
    cnt = 0
    for movie in dict_mov:
        cnt += 1
        sum += movie["imdb"]
    print(sum / cnt)
avg_imdb(movies)


#exercise 5
def avg_imdb_ctg(dict_mov, category):
    sum = 0
    cnt = 0
    for movie in dict_mov:
        if movie["category"] == category:
            cnt += 1
            sum += movie["imdb"]
    print(sum / cnt)
user_Input = input("Enter the category: ")
avg_imdb_ctg(movies, user_Input)
