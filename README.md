# Задание на дипломный проект «Шпионские игры» курса  «Python: программирование на каждый день и сверхбыстрое прототипирование» 

Есть вещи, которые объединяют людей, а есть те, которые делают нас индивидуальными. Давайте посмотрим, чем пользователи в ВК не делятся со своими друзьями?

## Задание:
Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.
В качестве жертвы, на ком тестировать, можно использовать: [https://vk.com/eshmargunov](https://vk.com/eshmargunov)

### Входные данные: 
Имя пользователя или его id в ВК, для которого мы проводим исследование.

**Внимание:** и имя пользователя `(eshmargunov)` и `id (171691064)`  - являются валидными входными данными.

Ввод можно организовать любым способом: 
* из консоли
* из параметров командной строки при запуске
* из переменной

### Выходные данные: 
Файл `groups.json` в формате:
```javascript
[
    {
    “name”: “Название группы”, 
    “gid”: “идентификатор группы”, 
    “members_count”: количество_участников_сообщества
    },
    {
    …
    }
]
```
Форматирование не важно, важно чтобы файл был в формате json

### Требования к программе:
* Программа не падает, если один из друзей пользователя помечен как “удалён” или “заблокирован”.
* Показывает что не зависла: рисует точку или чёрточку на каждое обращение к api.
* Не падает, если было слишком много обращений к API 
(Too many requests per second).
Ограничение от ВК: не более 3х обращений к API в секунду.
Могут помочь модуль time (time.sleep) и конструкция (try/except).
* Код программы удовлетворяет `PEP8`.
* Не использовать внешние библиотеки (vk, vkapi).


### Дополнительные требования (не обязательны для получения диплома):
* Использовать execute для ускорения работы.
* Показывает прогресс:  сколько осталось до конца работы (в произвольной форме: сколько обращений к API, сколько минут, сколько друзей или групп осталось обработать).
* Восстанавливается если случился `ReadTimeout`.
* Показывать в том числе группы, в которых есть общие друзья, но не более, чем **N** человек, где **N** задается в коде.

**Hint:**
Если у пользователя больше 1000 групп, можно ограничиться первой тысячей

**Hint:**
Удобно использовать множества

### Материалы:
Для того чтобы выполнить задание вам необязательно иметь аккаунт в ВК. 

Документация по методам: https://vk.com/dev/methods

**Токен** для VK api:

ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae

### Как правильно задавать вопросы дипломному руководителю?

Что следует делать, чтобы все получилось:

1. Попробовать найти ответ сначала самому в интернете. Ведь, именно это скилл поиска ответов пригодится тебе на первой работе. И только после этого спрашивать дипломного руководителя
2. В одном вопросе должна быть заложена одна проблема
3. По возможности, прикреплять к вопросу скриншоты и стрелочкой показывать где не получается. Программу для этого можно скачать здесь https://app.prntscr.com/ru/
4. По возможности, задавать вопросы в комментариях к коду. Начинать работу над дипломом как можно раньше! Чтобы было больше времени на правки.
5. Делать диплом по-частям, а не все сразу. Иначе, есть шанс, что нужно будет все переделывать :)

Что следует делать, чтобы ничего не получилось:
1. Писать вопросы вида “Ничего не работает. Не запускается. Всё сломалось.”
2. Откладывать диплом на потом.
3. Ждать ответ на свой вопрос моментально. Дипломные руководители - работающие разработчики, которые занимаются, кроме преподавания, своими проектами. Их время ограничено, поэтому постарайтесь задавать правильные вопросы, чтобы получать быстрые ответы!

