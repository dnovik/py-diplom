import requests
import time
import json

USER_ID = '171691064'
USER_NAME = 'eshmargunov'
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
groups_file = 'groups.json'



def get_group_info(unique_main_user_groups):

    BASE_URL = 'https://api.vk.com/method/groups.getById'

    params = {
        'access_token': TOKEN,
        'group_ids': unique_main_user_groups,
        'v': '5.95',
        'fields': ['id', 'name', 'members_count']
    }

   
    r = requests.get(BASE_URL, params).json()
    unique_groups = r['response']

    print(unique_groups)

groups = get_group_info(unique_groups)



def compare_groups(main_user, friend_list):

    main_user_groups = set(get_user_group(main_user))
    friends_group = set()

    try:
        for friend in friend_list:
            group_list = get_user_group(friend)

            if len(group_list) > 1000:
                group_list = group_list[0:1001]

            for group in group_list:
                friends_group.add((group))
    except TypeError:
            pass
    finally:
        time.sleep(2)

    unique_main_user_groups = list(main_user_groups.difference(friends_group))
    return unique_main_user_groups




def get_friend_ids(user_id):

    BASE_URL = 'https://api.vk.com/method/friends.get'

    params = {
        'access_token': TOKEN,
        'user_id': user_id,
        'v': '5.95'
    }
    r = requests.get(BASE_URL, params).json()
    friend_list = r['response']['items']

    return friend_list



def get_user_group(user_id):

    BASE_URL = 'https://api.vk.com/method/groups.get'
    params = {
        'access_token': TOKEN,
        'user_id': user_id,
        'v': '5.95',}

    r = requests.get(BASE_URL, params).json()
    try:
        group_list = r['response']['items']
        return group_list
    except KeyError:
        pass

test_friends = [7858, 317799]
unique_groups = compare_groups(USER_ID, test_friends)
get_group_info(unique_groups)

print(unique_groups)