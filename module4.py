import requests


URL = 'https://icanhazdadjoke.com'

def search_dad_jokes(search_term='', page_num=1, page_limit=20):
    
    search_term = str(search_term).strip().lower()

    h = {'Accept': 'application/json'}

    p = {
        "page": page_num,
        'limit': page_limit,
        'term': search_term
    }
    search_url = URL + 'search'

    resp_msg = requests.get(search_url, headers=h, params=p)

    if resp_msg.status_code == requests.codes.ok:
         return resp_msg.json()
        
    else:
        print(f'Status code: {resp_msg.status_code}, error reason: {resp_msg.reason}')

joke_dict = search_dad_jokes('hipster')

pass