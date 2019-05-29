import requests
import time
import json

USER_ID = '171691064'
USER_NAME = 'eshmargunov'
TOKEN ='73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
groups_file = 'groups.json'



def get_diff_groups(user_id):
    # основная функция - вход в программу!


    # получим id пользователя
    user_id = get_id_by_username(user_id)
    # получим список друзей
    friend_list = get_friend_ids(user_id)
    # получим список групп друзей
    group_list = get_user_group(friend_list)
    # получим непересекающиеся группы
    diff_groups = compare_groups(user_id, group_list)
    # выводим по ним информацию в файл
    get_group_info(diff_groups)
    print('Программа завершена!')


def get_group_info(groups):
    # функция возвращает информацию в указанном формате при вводе id группы
    BASE_URL = 'https://api.vk.com/method/groups.getById'

    for group in groups:

        params = {
            'access_token': TOKEN,
            'group_id': group,
            'v': '5.95',
            'fields': ['id', 'name', 'members_count']
        }
        print('.', '.', '.') 
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

    group_list = get_user_group(friend)          
    
    for group_list in user_groups:
        if len(group_list) > 1000:
                group_list = group_list[0:1001]
        for group in group_list:
            friends_group.add(group)

    unique_main_user_groups = list(main_user_groups.difference(friends_group))

    return unique_main_user_groups


def get_friend_ids(user_id):
    # функция возвращает список id друзей пользователя при вводе user_id
    BASE_URL = 'https://api.vk.com/method/friends.get'

    params = {
        'access_token': TOKEN,
        'user_id': user_id,
        'v': '5.95'
    }

    print('...')
    r = requests.get(BASE_URL, params).json()
    friend_list = r['response']['items']

    return friend_list



def get_user_group(user_ids):
    # функция возвращает список групп одного пользователя при вводе user_id
    BASE_URL = 'https://api.vk.com/method/groups.get'

    groups = []

    
    params = {
        'access_token': TOKEN,
        'user_id': user_id,
        'v': '5.95'}
    try:
        print('...')
        r = requests.get(BASE_URL, params).json()
        group_list = r['response']['items']
    except KeyError:
        pass

        groups.append(group_list)

    return groups


def get_id_by_username(user_name):
    # функция возвращает id пользователя при вводе username
    BASE_URL = 'https://api.vk.com/method/users.get'

    params = {
        'access_token': TOKEN,
        'domain': user_name,
        'v': '5.95'
    }
    print('...')
    r = requests.get(BASE_URL, params).json()
    user_id = r['response'][0]['id']

    return user_id


get_diff_groups(USER_NAME)


friends = get_friend_ids(USER_ID)
compare_groups(USER_ID, friends)

get_user_group(USER_ID)