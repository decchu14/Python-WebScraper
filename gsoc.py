import requests
from bs4 import BeautifulSoup

years = ['2019', '2020']
for y in years:
    res = requests.get(
        "https://summerofcode.withgoogle.com/archive/" + y + "/organizations/")
    soup = BeautifulSoup(res.text, 'html.parser')
    all_org_names = soup.select('.organization-card__name')
    all_org_links = soup.select('.organization-card__link')
    # len(all_org_links) will also give same length
    total_org = len(all_org_names)
    count = 0

    for i in range(total_org):
        org_link = all_org_links[i].get('href', None)
        org_name = all_org_names[i].get_text()
        org_link_req = requests.get(
            "https://summerofcode.withgoogle.com" + org_link)
        tech_soup = BeautifulSoup(org_link_req.text, 'html.parser')
        technologies = [j.get_text().strip()
                        for j in tech_soup.select('.organization__tag--technology')]

        if 'python' in technologies:
            if count == 10:
                break
            else:
                count += 1

                print(f'{count}. YEAR={y}----NAME: {org_name}')
                print('TECHNOLOGIES: ', technologies)
                print('\n')

        # print(f'\n{total_org}\n')

    print('\n')
