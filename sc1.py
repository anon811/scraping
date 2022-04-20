from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def get_names(url):
    """
    Return title or None if element not found.
    :param url: url to parse.
    :return: <h1> element.
    """

    try:
        html = urlopen(url)
    except HTTPError as err:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        names = bs.find_all('span', {'class': 'green'})
    except AttributeError as err:
        return None
    return names


if __name__ == '__main__':
    names = get_names('https://www.pythonscraping.com/pages/warandpeace.html')
    if names:
        for name in names:
            print(name.get_text())
    else:
        print('Names not found')