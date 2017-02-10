#! /user/bin/env python3

import requests
import dhtmlparser


class Project:
    def __init__(self, name, url):
        self.name = name
        self.url = url


def get_html(nick):
    url = "https://pypi.python.org/pypi?%3Aaction=search&term=" + nick + "&submit=search"

    response = requests.get(url)

    return response.text

def get_project_html(url):
    response = requests.get(url)
    return response.text


#print(get_html("bystroushaak"))

def parse_projects(html):
    dom = dhtmlparser.parseString(html)
    tables = dom.find("table", {"class": "list"})

    def select_project_link(link):
        if not link.params.get("href", "").startswith("/pypi"):
            return False
        url = "https://pypi.python.org/" + link.params.get("href", "")
        project_html = get_project_html(url)
        project_dom = dhtmlparser.parseString(project_html)

        #todo find author in project_dom; return true / false


    def create_project(link):
        url = link.params.get("href", "")
        name = link.getContent()

        return Project(name, url)

    links = tables[0].find("a", fn=select_project_link)
    return list(map(create_project, links))

#print()
projects = parse_projects(get_html("bystroushaak"))

for p in projects:
    print(p.name)
    print(p.url)







