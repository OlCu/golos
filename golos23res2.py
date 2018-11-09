# ищем сколько раз голосовал вотер за посты

from golos import Steem
import datetime

NODE = 'wss://ws.golos.io'
AUTHOR = 'whaler-fund'

VOTER = 'feb'

posts = ['bod-na-golose-1-nedelya',
         'bod-na-colose-nedelya-2',
         'bod-na-golose-nedelya-3',
         'bod-na-golose-nedelya-4',
         'bod-na-golose-nedelya-5-skrytaya-ugroza',
         'bod-na-golose-nedelya-6-miloserdie-grizli-i-predlozhenie-k-avtoram',
         'bod-na-golose-nedelya-7-nedostizhimyij-idealxnyij-stroij',
         'bod-na-golose-nedelya-8-vremya-i-regiony']

s = Steem([NODE], no_broadcast=True)

print('Исследуем вотера', VOTER)
print()

hit = 0
hit2 = 0

for pl in posts:
    try:
        p = s.get_content(AUTHOR, pl, 1000)
    except Exception as e:
        print("Ошибка сети", e)
        print('Выполнение прервано. Перезапустите скрипт.')
        exit(1)
    for el in p['active_votes']:
        if el['voter'] == VOTER:
            votetime = datetime.datetime.strptime(el['time'], '%Y-%m-%dT%H:%M:%S')
            posttime = datetime.datetime.strptime(p['created'], '%Y-%m-%dT%H:%M:%S')
            dt = votetime - posttime
            print('За пост', pl, 'проголосовал на', dt.seconds, 'секунде')
            if dt.seconds <= 60 * 60 * 24 * 7:
                hit2 += 1
            hit += 1
            break

if hit == 0:
    print('Не прголосовал ниразу')
else:
    print()
    print('Проголосовал вовремя', hit2)
    print('Всего', hit)
