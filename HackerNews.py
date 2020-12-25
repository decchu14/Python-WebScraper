import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
res1 = requests.get("https://news.ycombinator.com/news?p=2")

soup = BeautifulSoup(res.text, 'html.parser')
soup1 = BeautifulSoup(res1.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')

links1 = soup1.select('.storylink')
subtext1 = soup1.select('.subtext')

mega_links = links + links1
mega_subtexts = subtext + subtext1


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for indx, item in enumerate(links):
        title = links[indx].getText()
        href = links[indx].get('href', None)
        votes = subtext[indx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtexts))
