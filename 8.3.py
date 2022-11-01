site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(struct, key):
    if key in struct:
        return struct[key]
    for sub in struct.values():
        if isinstance(sub, dict):
            a = find_key(sub, key)
            if a:
                break
    else:
        a = None
    return a


user_key = input('Искомый ключ: ')
value = find_key(site, user_key)
if value:
    print(value)
else:
    print('такого ключа нет')