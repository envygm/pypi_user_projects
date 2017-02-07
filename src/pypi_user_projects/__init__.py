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

#print(get_html("bystroushaak"))

def parse_projects(html):
    dom = dhtmlparser.parseString(html)
    tables = dom.find("table", {"class": "list"})

    def select_project_link(link):
        return link.params.get("href", "").startswith("/pypi")

    links = tables[0].find("a", fn=select_project_link)

    return links

print(parse_projects(get_html("bystroushaak")))

