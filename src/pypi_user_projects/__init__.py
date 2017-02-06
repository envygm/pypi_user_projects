#! /user/bin/env python3

import requests
import dhtmlparser

def get_html(nick):
    url = "https://pypi.python.org/pypi?%3Aaction=search&term=" + nick + "&submit=search"

    response = requests.get(url)

    return response.text

#print(get_html("bystroushaak"))

def parse_projects(html):
    dom = dhtmlparser.parseString(html)
    table = dom.find("table", {"class": "list"} )

    return table

print(parse_projects(get_html("bystroushaak")))


