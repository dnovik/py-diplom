import requests
import time
import json

# для запуска программы необходимо в функцию main() передать username или user_id

USER_ID = '171691064'
USER_NAME = 'eshmargunov'
TOKEN ='73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
groups_file = 'groups.json'



def main(user_id):
    user_id = get_id_by_username(USER_NAME)
    friend_list = get_friend_ids(user_id)
    group_list = get_user_group(friend_list[0:5])
    unique_groups = compare_groups(USER_ID, friend_list[0:5])
    get_group_info(unique_groups)


def get_group_info(groups):
    # функция возвращает информацию в указанном формате при вводе id группы
    BASE_URL = 'https://api.vk.com/method/groups.getById'

    print('Получаем информацию по группам')
    for group in groups:

        params = {
            'access_token': TOKEN,
            'group_id': group,
            'v': '5.95',
            'fields': ['id', 'name', 'members_count']
        }
        print('_') 
        r = requests.get(BASE_URL, params).json()
        unique_groups = r['response']
        time.sleep(1)

        with open(groups_file, 'a') as file:
            json.dump(unique_groups, file, indent=1)
        
    print('Запись в файл завершена')


def compare_groups(main_user, friend_list):
    # функция возвращает список непересекающихся групп пользователя при вводе user_id и id друзей
    main_user_groups = set(get_user_group(main_user))
    friends_group = set()

    for friend_id in friend_list:
        group_list = get_user_group(friend_id)
        time.sleep(1)
        
        try:
            for group in group_list:
                friends_group.add(group)
        except TypeError:
            pass
    
    unique_groups = main_user_groups.difference(friends_group)

    return unique_groups
    

def get_friend_ids(user_id):
    # функция возвращает список id друзей пользователя при вводе user_id
    BASE_URL = 'https://api.vk.com/method/friends.get'

    params = {
        'access_token': TOKEN,
        'user_id': user_id,
        'v': '5.95'
    }
    print('_')
    r = requests.get(BASE_URL, params).json()
    friend_list = r['response']['items']

    return friend_list



def get_user_group(user_id):
    # функция возвращает список групп одного пользователя при вводе user_id
    BASE_URL = 'https://api.vk.com/method/groups.get'

    params = {
        'access_token': TOKEN,
        'user_id': user_id,
        'v': '5.95'}
    r = requests.get(BASE_URL, params).json()
    print('_')
    try:
        group_list = r['response']['items']
        if len(group_list) > 1000:
            group_list = group_list[0:1000]
    except KeyError:
        pass
    else:
        return group_list



def get_id_by_username(user_name):
    # функция возвращает id пользователя при вводе username
    BASE_URL = 'https://api.vk.com/method/users.get'

    params = {
        'access_token': TOKEN,
        'domain': user_name,
        'v': '5.95'
    }
    print('_')
    r = requests.get(BASE_URL, params).json()
    user_id = r['response'][0]['id']

    return user_id