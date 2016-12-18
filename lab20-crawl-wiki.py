# coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import urlparse
import urllib
import unicodedata
import re

request_timeout = 0.5

final_urls = {
    'https://ru.wikipedia.org/wiki/Философия',
    'https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F',
    'https://en.wikipedia.org/wiki/Philosophy'
}

def encode_url(url):
    return urllib.unquote(url.encode('utf-8'))


def extract_normal_link(url, content):
    main_soup = BeautifulSoup(content, 'html.parser')

    for ptag in main_soup.select('div#mw-content-text > p'):

        # remove brackets from content
        subcontent = str(ptag)
        subcontent_length = 0
        # TODO что если скобки в href ???
        # while(len(subcontent) != subcontent_length):
        #     subcontent_length = len(subcontent)
        #    subcontent = re.sub(r'\([^(^)]*\)', '', subcontent)

        # extract links from subcontent
        sub_soup = BeautifulSoup(subcontent, 'html.parser')
        for link in sub_soup.select('a'):
            if link.has_attr('class') and ('new' in link.attrs['class'] or 'extiw' in link.attrs['class']):
                continue
            href = link.get('href')
            if href:
                if href.startswith('#'):
                    continue
                return urlparse.urljoin(url, link.get('href'))

    return None


def test_url(start_url, max_iters=1000000):
    next_url = start_url

    processed_urls = set()
    prev_load = 0

    for i in xrange(max_iters):

        if next_url in processed_urls:
            print 'Cycle is found. Link has already been processed. ({})'.format(encode_url(next_url))
            return False

        processed_urls.add(next_url)

        if next_url in final_urls:
            print 'Link to some Philosophy article is found. ({})'.format(encode_url(next_url))
            return True

        interval_since_last_request = time.time() - prev_load

        if interval_since_last_request < request_timeout:
            time.sleep(request_timeout - interval_since_last_request)

        print '[{}]: {}. {}'.format(time.ctime(), i + 1, encode_url(next_url))

        response = requests.get(next_url)
        prev_load = time.time()

        next_url = extract_normal_link(next_url, response.text)

        if not next_url:
            print 'Link wasn\'t extracted for some reason.'
            return False

    print 'Max iterations limit was exceeded.'

    return False


# print test_url('https://ru.wikipedia.org/wiki/Python')
print test_url('https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0')
# print test_url('https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D1%81%D1%82%D1%8C')
# print test_url('https://en.wikipedia.org/wiki/Python_(programming_language)')
