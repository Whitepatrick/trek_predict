import imdb
import json

#Star Trek: The Motion Picture (1979) 0079945
#Star Trek II: The Wrath of Khan (1982) 0084726
#Star Trek III: The Search for Spock (1984) 0088170
#Star Trek IV: The Voyage Home (1986) 0092007
#Star Trek V: The Final Frontier (1989) 0098382
#Star Trek VI: The Undiscovered Country (1991) 0102975
#Star Trek: Generations (1994) 0111280
#Star Trek: First Contact (1996) 0117731
#Star Trek: Insurrection (1998) 0120844
#Star Trek: Nemesis (2002) 0253754
#Star Trek (2009) 0796366
#Star Trek Into Darkness (2013) 1408101
#Star Trek Beyond (2016) 2660888
movie_ids = ('0079945', '0084726', '0088170', '0092007',
             '0098382', '0102975', '0111280', '0117731',
             '0120844', '0253754', '0796366', '1408101',
             '1408101', )

ia = imdb.IMDb()

for movie in movie_ids:
movie = ia.get_movie()
ia.update(movie, 'ratings')
movie_rating = movie['ratings']
print movie_rating

def get_ratings(season_i):
    ratings = {}
    for key, value in season_i.iteritems():
        ia.update(value)
        ratings[key] = value.get('rating')

    return ratings

#show_ratings = {}
#for i in range(1, len(show_seasons) + 1):
#    season_key = "season_" + str(i)
#    show_ratings[season_key] = get_ratings(show_seasons[i])

#print show_ratings
#with open('st_ent.json', 'w') as fp:
#    json.dump(show_ratings, fp)
