import requests


from bs4 import BeautifulSoup

page = requests.get(input())
soup = BeautifulSoup(page.content, 'lxml')
paragraphs = soup.find("div", id="PageContent_C002_Col00").find_all("a")
key_letter = 'S'
answer_list = []
for i in paragraphs:
    if len(i.text) > 2 and i.text.startswith(key_letter):
        answer_list.append(i.text.strip())
    else:
        continue
print(answer_list)
