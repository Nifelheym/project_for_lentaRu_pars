from bs4 import BeautifulSoup
import requests
#import pyodbc
import json
urlJson = 'front_for_parse/static/news.json'
def write_new(new, old_data=None):
        #print(new,old_data)
    if old_data is not None:
        old_data.append(new)
        print(old_data)
    else:
        old_data = list()
        old_data.append(new)
    with open(urlJson, 'w') as f:
        f.write(json.dumps(old_data, indent=2, separators=(',', ': ')))

def wtj(name, date, alt):
    print(name, date, alt)
    # проверка, вдруг фал не существует
    try:
        json_file = open(urlJson, 'r')
        # проверка, вдруг фал существует, но пуст
        try:
            data = json.load(json_file)
            print(data)
            json_file.close()
            write_new({'news': name, 'date': date, 'alt': alt}, data)
        except TypeError:
            print('TypeERROR')
            write_new({'news': name, 'date': date, 'alt': alt})
    except FileNotFoundError:
        print('notFound')
        write_new({'news': name, 'date': date, 'alt': alt})

def updateNewsTable():
    proxy = {'http' :'http://62.173.145.48:3128',
    'https': 'http://91.208.39.70:8080'}

    url = 'http://www.lenta.ru'
    rs = requests.get(url, proxies=proxy)

    postPars= BeautifulSoup(rs.content, 'html.parser')
    div = postPars.find('div', class_='first-item')
    divs = postPars.find_all('div', class_='item')
    firstItem = div.find('h2').text
    timeOfFirstPost = firstItem[0:5]
    textOfPost = firstItem[5:]
    newNewsUrl = div.find('a').get('href')
    # кидаем новый запрос чтобы получить категорию статьи

    newurl = url + newNewsUrl
    rse = requests.get(newurl, proxies=proxy)
    roote = BeautifulSoup(rse.content, 'html.parser')
    categ = roote.find('a', class_='b-header__block').text
#     print(timeOfFirstPost, textOfPost, categ)
    wtj(textOfPost, timeOfFirstPost, categ)

    for x in divs[0:9]:
        try:
            textOfNEws = x.find('a').text
            timeOfNews = textOfNEws[0:5]
            textOfNEws = textOfNEws[5:]
            newNewsUrl = x.find('a').get('href')
            newurl = url + newNewsUrl
            rse = requests.get(newurl, proxies=proxy)
            roote = BeautifulSoup(rse.content, 'html.parser')
            try:
                newCateg = roote.find('a', class_='b-header__block').text
                wtj(textOfNEws, timeOfNews, newCateg)
            except:
                wtj(textOfNEws, timeOfNews, 'Мослента')
        except FileNotFoundError:
            print('WrongConnection')
        # print(textOfNEws, timeOfNews, newCateg)


def write_to_json(name, date, city):
    with open(urlJson,'r') as jfr:
        jf_file = json.load(jfr)
    with open(urlJson,'w') as jf:
        jf_target = jf_file[0]['news']
        user_info = {'news': name, 'date': date, 'alt': city}
        jf_target.append(user_info)
        json.dump(jf_file, jf, indent=4)

updateNewsTable()
