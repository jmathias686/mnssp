import requests, pprint, json

#information on TMDB API
# https://developers.themoviedb.org/3/getting-started/introduction

def movies(self):
# TMDB Auth key generated by jomathias@deloitte.com.au
# necessary to access the TMDB API data for requests.
    key = '630e56aca56e58a7b972a87876d54340'

    # path found from TMDB API documentation - to receive json data of movies now-playing
    path = 'https://api.themoviedb.org/3/movie/now_playing?api_key=' + key + '&language=en-US&page=1&region=au'
    r = requests.get(path)

    #pretty print data to console (for easy reading and accessing)
    #parsed_json to be used for accessing data
    parsed_json = (json.loads(r.text))

    #data is to be printed out or writtent o a file
    data = json.dumps(parsed_json, indent=4, sort_keys=True)
    # print(data)


    #sort movies by a field (popularity, vote average, votes etc.) and put into titles
    movies = parsed_json['results']
    titles = []
    for m in movies:
        if m['popularity'] > 110:
            titles.append(m['title'])
    print(titles)




#- - - - - - - - - - - - - - - - - - -  FILE WRITE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
#*********uncomment below to create/rewrite a file now_playing.json with the data of now_playing movies**********

# f=open("now_playing.json", "w+")
# f.write(json.dumps(json.loads(r.text), indent=4, sort_keys=True))
# f.close()

return parsed_json