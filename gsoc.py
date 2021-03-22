import requests
from bs4 import BeautifulSoup
import pprint

years = ['2020']
org_names_list = []


for y in years:
    org_names_list = []
    technologies_list = []
    res = requests.get(
        "https://summerofcode.withgoogle.com/archive/" + y + "/organizations/")
    soup = BeautifulSoup(res.text, 'html.parser')
    all_org_names = soup.select('.organization-card__name')
    all_org_links = soup.select('.organization-card__link')
    # len(all_org_links) will also give same length
    total_org = len(all_org_names)
    # count = 0

    for i in range(total_org):
        org_link = all_org_links[i].get('href', None)
        org_name = all_org_names[i].get_text()
        org_link_req = requests.get(
            "https://summerofcode.withgoogle.com" + org_link)
        tech_soup = BeautifulSoup(org_link_req.text, 'html.parser')
        technologies = [j.get_text().strip()
                        for j in tech_soup.select('.organization__tag--technology')]

        # for z in technologies:
        #     print(z)
        #     consistant_orgs[org_name].append(z)

        if 'python' in technologies:
            org_names_list.append(org_name)
            technologies_list.append(technologies)

    for j in range(len(org_names_list)):
        print(f'{org_names_list[j]}: {technologies_list[j]}')
        print('\n')
    # pprint.pprint(org_names_list)
    # print('\n')
    # print(len(org_names_list), '\n')
    # if count == 2:
    #     break
    # elif y == '2020':
    #     count += 1
    #     dict_1 = {org_name: technologies}
    #     consistant_orgs.append(dict_1.copy())
    #     # print(f'{count}. YEAR={y}----NAME: {org_name}')
    #     # print('TECHNOLOGIES: ', technologies)
    #     # print('\n')
    # # else:
    # #
    # #     dict_1 = {org_name: technologies}
    # else:
    #     count += 1
    #     dict_1 = {org_name: technologies}
    #     print(dict_1)
    #     # if dict_1 in consistant_orgs:

    # #     print(dict_1[0].keys())
    # #     if key,value in dict_1.items():
    # #        if key in list(consistant_orgs)
    # #         consistant_orgs.append(dict_1.copy())

    #     # print(f'\n{total_org}\n')
