# coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import urlparse
import urllib

request_timeout = 1

final_urls = {
    'https://ru.wikipedia.org/wiki/Философия',
    'https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F',
    'https://en.wikipedia.org/wiki/Philosophy'
}


def encode_url(url):
    return urllib.unquote(str(url))


def extract_normal_link(url, content):
    main_soup = BeautifulSoup(content, 'html.parser')

    for link in main_soup.select('div#mw-content-text > p > a'):
        # check if link points to new article
        if link.has_attr('class') and ('new' in link.attrs['class'] or 'extiw' in link.attrs['class']):
            continue
        href = link.get('href')
        if href:
            # check if link is an anchor
            if href.startswith('#'):
                continue

            # check if link is in brackets
            open_brackets_count = 0
            close_brackets_count = 0
            sibling = link.findPreviousSibling(text=True)
            while sibling is not None:
                open_brackets_count += str(sibling.encode('utf-8')).count('(')
                close_brackets_count += str(sibling.encode('utf-8')).count(')')
                sibling = sibling.findPreviousSibling(text=True)

            if close_brackets_count >= open_brackets_count:
                return urlparse.urljoin(url, link.get('href'))

    return None


def test_url(start_url, max_iters=1000000):
    next_url = start_url
    # next_url = start_url

    processed_urls = set()
    prev_load = 0
    prev_prev_load = 0

    for i in xrange(max_iters):

        if next_url in processed_urls:
            print 'Cycle is found. Link has already been processed. ({})'.format(encode_url(next_url))
            return False

        processed_urls.add(next_url)

        if next_url in final_urls:
            print 'Link to some Philosophy article is found. ({})'.format(encode_url(next_url))
            return True

        # sleeping
        interval_since_request = time.time() - prev_prev_load
        if interval_since_request < request_timeout:
            time.sleep(request_timeout - interval_since_request)

        print '[{}]: {}. {}'.format(time.ctime(), i + 1, encode_url(next_url))

        response = requests.get(next_url)
        prev_prev_load = prev_load
        prev_load = time.time()

        # extract normal link
        next_url = extract_normal_link(next_url, response.text)

        if not next_url:
            print 'Link wasn\'t extracted for some reason.'
            return False

    print 'Max iterations limit was exceeded.'

    return False


urls_to_test = ['https://ru.wikipedia.org/wiki/Python',
                # https://ru.wikipedia.org/wiki/Мэрилин_Монро
                'https://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%80%D0%B8%D0%BB%D0%B8%D0%BD_%D0%9C%D0%BE%D0%BD%D1%80%D0%BE',
                # https://ru.wikipedia.org/wiki/Белорусский_государственный_университет
                'https://ru.wikipedia.org/wiki/%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82',
                'https://ru.wikipedia.org/wiki/Steam',
                # https://ru.wikipedia.org/wiki/Кошка
                'https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0',
                # https://ru.wikipedia.org/wiki/Теория_большого_взрыва_(телесериал)
                'https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F_%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B3%D0%BE_%D0%B2%D0%B7%D1%80%D1%8B%D0%B2%D0%B0_(%D1%82%D0%B5%D0%BB%D0%B5%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB)']

for i in xrange(len(urls_to_test)):
    print " ---- Start test #{} ---- ".format(i + 1)
    print test_url(urls_to_test[i])
    print " --- Finish test ---- "
