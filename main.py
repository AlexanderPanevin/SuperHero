import requests

TOKEN = '5582487781872590'
url_list = [f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk/',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain America/',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos/']
def requests_get(url_list):
    response = (requests.get(url) for url in url_list)
    return response
def compare_parameter():
    super_man = []
    name = ''
    intelligence_super_hero = 0
    for url in requests_get(url_list):
        super_men_character = url.json()
        try:
            for power_stats in super_men_character['results']:
                super_man.append({'name': power_stats['name'],'intelligence': power_stats['powerstats']['intelligence']})
        except KeyError:
            print(f'Такой ссылки в url_list нет: {url_list}')
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']
    print(f"Самый умный - {name}. Его интеллект: {intelligence_super_hero} баллов.")
compare_parameter()

