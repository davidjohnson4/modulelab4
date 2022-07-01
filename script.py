from module4 import search_dad_jokes


jokes_dict = search_dad_jokes('cow')

for j in jokes_dict['results']:
    print(j['joke'])

pass