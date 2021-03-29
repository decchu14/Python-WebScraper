import requests
from bs4 import BeautifulSoup
import pprint

# years whose organizations details we want to fetch
years = ['2020']

# this list is used to store the org names who and years in which they participated
# along with technologies they used.
main_list = []

# opening a text file to write a data
with open('gsoc.txt', mode='a') as gsoc_file:

    # looping through each year given in the years list above
    for y in years:

        # making a requests to the gsoc archive page to fetch the organizations details and storing
        # the result in the variable called "res".
        res = requests.get(
            "https://summerofcode.withgoogle.com/archive/" + y + "/organizations/")

        # parsing through the result 'res' using html parser
        soup = BeautifulSoup(res.text, 'html.parser')

        # here orgainizations names are fetched by using the class name '.organization-card__name'.
        # the fetched result that is org names will be in the form of list
        all_org_names = soup.select('.organization-card__name')

        # here orgainizations links are fetched by using the class name '.organization-card__link'.
        # the fetched result that is org links will be a list
        all_org_links = soup.select('.organization-card__link')

        # length of the list means total number of orgs is calculated
        total_org = len(all_org_names)
        print(total_org)
        count = 0
        # looping through each org page to check whether they use python or no
        for i in range(total_org):

            # fetching the each org link from a list of links
            org_link = all_org_links[i].get('href', None)

            # making a requests to each org page.
            org_link_req = requests.get(
                "https://summerofcode.withgoogle.com" + org_link)

            # parsing through the result 'tech_soup' using html parser
            tech_soup = BeautifulSoup(org_link_req.text, 'html.parser')

            # fetching technologies of each org in list form
            technologies = [j.get_text().strip()
                            for j in tech_soup.select('.organization__tag--technology')]

            gsoc_dict = {}

            # looping through the org technologies to check for python
            # if there then writing the org name to the gsoc text file
            if 'python' in technologies:
                gsoc1_dict = {y: technologies}
                gsoc_dict = {all_org_names[i].get_text(): gsoc1_dict}
                gsoc_file.write(str(gsoc_dict))
                gsoc_file.write('\n')
                count += 1

        print(count)
