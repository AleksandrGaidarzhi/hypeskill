import requests
import string
import os

from bs4 import BeautifulSoup
q_pages = int(input())
topic_name = input()

for pg in range(1, q_pages + 1):
    os.mkdir('Page_' + str(pg))
    os.chdir(os.path.join(os.getcwd(), ('Page_' + str(pg))))
    page = requests.get(f'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={pg}', headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all(class_="c-card__link u-link-inherit")
    type_ = soup.find_all(class_="c-meta__type")
    links_list = []
    type_list = []
    for word in type_:
        type_list.append(word.text.strip())
    for link in links:
        links_list.append('https://www.nature.com' + link.get('href'))

    links_dict = dict(zip(links_list, type_list))

    for elem in links_dict:
        if links_dict[elem] == topic_name:
            true_news_page = requests.get(elem, headers={'Accept-Language': 'en-US,en;q=0.5'})
            soup_true = BeautifulSoup(true_news_page.content, 'html.parser')
            headline = soup_true.find('h1').text.strip()
            text_content = soup_true.find_all(class_="c-article-body u-clearfix")
            list_text = []
            corr_text = []
            for t_word in text_content:
                t_word = t_word.text.strip()
                t_word = t_word.replace('\n', '')
                list_text.append(t_word)
            for i in list_text:
                if i not in corr_text:
                    corr_text.append(i)

            symbols = string.punctuation

            for n in symbols:
                name = headline.replace(str(n), '')
            name = name.replace('?', '').replace(':', '').replace(' ', '_')

            file = open(f'{name}.txt', 'w', encoding='utf-8')
            file.write(''.join(corr_text))
            file.close()
    os.chdir(os.path.dirname(os.getcwd()))
print('Saved all articles.')
