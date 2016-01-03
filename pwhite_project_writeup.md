### TREK PREDICT!
## Predicting the success (or failure) of the upcoming 2017 Star Trek television series.

# Summary
There is a new Star Trek series starting up in 2017 and I think it will have a better shot at success than the last series that aired.

The Star Trek television series has been a fan of mine since Star Trek: The Next Generation. Since that series it's had more series come and share the same popularity that Next Generation (TNG) had. But after Star Trek: Voyager (VOY), the success started to taper off resulting in Star Trek: Enterprise being canceled and ending in it's 4th season, a full 3 seasons short of the average 7 season run of the previous three Trek shows (TNG, DS9, & VOY).

I would like to use a handful of TV/Movie database APIs to get as much data on previous statistics and factors that would account for a successful series (TNG, DS9, VOY), compare against seemingly abysmal series (original series TOS, Animated Series ANI, Enterprise ENT).

Some of the factors that I hope to use to estimate the success of the new series will be performance of old series' and some temporal events as well:
  - Show rating from IMDb, and OMDb
  - Show ratings from Rotten Tomatoes users (provided my API key request is approved)
  - Movies released during the shows aired dates
    - Will also try to factor in performance of the movie itself as some of the TNG movies have been credited to ENT's poor performance (this may or may not happen as it may be hard to implement meaningfully)

# Data Sources
IMDb - Using http://imdbpy.sourceforge.net/ which is simply scraping IMDb HTML pages and returning results in a string, list or dictionary. Already gathered [some data](https://github.com/Whitepatrick/trek_predict/tree/master/trek_json) and have stored it so I don't keep hitting this "API" as it is pretty slow.

Rotten Tomatoes - http://developer.rottentomatoes.com/. Their API is no longer public, I've applied for an API key, hopefully I'm approved, if not I'll just have to scrape the info I need from HTML pages.

OMDb - http://www.omdbapi.com/ for anything I can't get from the other two.
  - I may try adding in some other data sources, but the public and free APIs for useful TV data aren't supported by paid devs so this is a labor of love.

Show ratings (in aggregate) - http://www.trektoday.com/articles/ratings_history.shtml

If the data I've collected already proves to be too little, I can scrape ratings and reviews from amazon using python/[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)


# Unrelated to this course
I was COMPLETELY surprised by the internet's lack of structured Star Trek data and databases devoted strictly to star trek. Since I've got some of the JSON already generated, I may extend this project into offering the world Star Trek Episode information in JSON format.
