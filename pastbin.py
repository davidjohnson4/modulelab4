def post_new_paste(titl, body_text, expiration='N', listed=True):
    '''
    
    
    
    '''

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