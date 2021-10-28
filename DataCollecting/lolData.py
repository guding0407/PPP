import random

import requests
from bs4 import BeautifulSoup


def main():
    listMeta = ['극AP', '극AD', '극탱', '딜탱', '서포팅', '극 이속', '극 흡혈', '극 공속', '극 쿨감']

    raw = requests.get("https://www.op.gg/champion/statistics",
                       headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    champ = html.select("div.champion-index__champion-item__name")
    position = html.select("div.champion-index__champion-item__positions")
    rank = html.select("div.champion-index-table__name")
    rankPosition = html.select("div.champion-index-table__position")

    top = []
    jg = []
    mid = []
    bot = []
    sup = []

    for i in range(len(champ)):
        if 'Top' in position[i].text:
            top.append(champ[i].text)
        elif 'Jungle' in position[i].text:
            jg.append(champ[i].text)
        elif 'Middle' in position[i].text:
            mid.append(champ[i].text)
        elif 'Bottom' in position[i].text:
            bot.append(champ[i].text)
        elif 'Support' in position[i].text:
            sup.append(champ[i].text)

    # for i in range(len(rank)):
    #     print('\033[95m' + rank[i].text, '\033[00m' + rankPosition[i].text.replace("\t", "").replace("\n", ""))

    # for t in top:
    #     print(t)

    random.shuffle(listMeta)
    random.shuffle(top)
    print(listMeta[0], top[0])
    random.shuffle(listMeta)
    random.shuffle(top)
    print(listMeta[0], jg[0])
    random.shuffle(listMeta)
    random.shuffle(top)
    print(listMeta[0], mid[0])
    random.shuffle(listMeta)
    random.shuffle(top)
    print(listMeta[0], bot[0])
    random.shuffle(listMeta)
    random.shuffle(top)
    print(listMeta[0], sup[0])

    # answer = input("어느 라인 메타를 추천해줄까요?(1. 탑, 2. 정글, 3. 미드, 4. 원딜, 5. 서폿 : ")
    #
    # random.shuffle(listMeta)
    # if answer == '1':
    #     random.shuffle(top)
    #     print(listMeta[0], top[0])
    # elif answer == '2':
    #     random.shuffle(jg)
    #     print(listMeta[0], jg[0])
    # elif answer == '3':
    #     random.shuffle(mid)
    #     print(listMeta[0], mid[0])
    # elif answer == '4':
    #     random.shuffle(bot)
    #     print(listMeta[0], bot[0])
    # elif answer == '5':
    #     random.shuffle(sup)
    #     print(listMeta[0], sup[0])

    # for i in range(len(champ)):
    #     print(champ[i].text, position[i].text)
    # print("오늘 할 메타는??")
