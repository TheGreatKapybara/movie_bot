import requests

headers = {
        'X-API-KEY': 'FSX7GN5-5Q84131-MGHPGV7-7YVTHS2',
        'Content-Type': 'application/json',
    }

def random_movie():
    gener = []
    country = []
    request = requests.get('https://api.kinopoisk.dev/v1.3/movie/random', headers=headers).json()
    result = [request['name'], request['description'], request['poster']['url'],
              None, request['year'], None, None]
    if result[1] == None:
        result = random_movie()
        return result

    if 'videos' in request and len(request['videos']['trailers']) > 0:
        result[3] = request['videos']['trailers'][0]['url']

    for i in range(len(request['genres'])):
       gener.append(request['genres'][i]['name'])

    if len(gener) > 0:
        result[5] = ', '.join(gener)
    else: result[5] = 'Неизвестен'

    for i in range(len(request['countries'])):
       country.append(request['countries'][i]['name'])

    if len(country) > 0:
        result[6] = ', '.join(country)
    else: result[6] = 'Неизвестно'

    return result

biba = random_movie()