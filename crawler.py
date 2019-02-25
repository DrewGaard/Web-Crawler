#!/usr/bin/env python

import requests
import re
import urlparse


# def request(url):
#     try:
#         return requests.get("http://" + url)
#     except requests.exceptions.ConnectionError:
#         pass


target_url = "http://gibson.com"
target_links = []

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):
    href_links = extract_links_from(target_url)
    for link in href_links:
        link = urlparse.urljoin(target_url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links: #remove exernal links from the search
            target_links.append(link)
            print(link) #get the html code from the page


crawl(target_url)





#-----------------------------------Refactored Code------------------------

# response = request(target_url)
#
# href_links = re.findall('(?:href=")(.*?)"', response.content)



#-------------------------Used for the Crawler---------------------------
# with open("/root/Downloads/subdomains.list", "r") as wordlist_file:
#     for line in wordlist_file:
#         word = line.strip()
#         test_url = word + "." + target_url
#         response = request(test_url)
#         if response:
#             print("[+] Discovered subdomain --> " + test_url)