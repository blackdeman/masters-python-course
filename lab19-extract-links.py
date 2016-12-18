from bs4 import BeautifulSoup


def extract_links(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')

    tags = [('a', 'href'), ('link', 'href'), ('area', 'href')]

    result = list()

    for tagtuple in tags:
        result.extend([link.get(tagtuple[1]) for link in soup.find_all(tagtuple[0]) if link.get(tagtuple[1])])

    return result

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
<area href="http://example.com/link4" id="link4">Link4</a>;
<link href="http://example.com/link5" id="link5">Link5</a>;
<a id="linkEmpty">Empty link</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

for link in extract_links(html_doc):
    print link
