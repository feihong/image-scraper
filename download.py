import urlparse
import sys
import requests
from selenium import webdriver


def main():
    url = sys.argv[1]

    browser = webdriver.Firefox()
    browser.get(url)
    user_agent = browser.execute_script('return window.navigator.userAgent')
    print user_agent
    image_url = browser.execute_script(JAVASCRIPT)
    print image_url
    headers = {
        'user-agent': user_agent,
        'host': urlparse.urlparse(image_url).netloc,
        'referer': url,
        'accept': 'image/png,image/*;q=0.8,*/*;q=0.5',
        'accept-language': 'Accept-Language: en-US,en;q=0.5',
        'connection': 'keep-alive',
    }
    print headers
    response = requests.get(image_url, headers=headers)
    with open('image.jpg', 'wb') as fp:
        fp.write(response.content)
    browser.quit()


JAVASCRIPT = """
var maxDimensions = 0;
var biggestImage = null;
for (var img of document.querySelectorAll('img')) {
    var dim = img.naturalWidth * img.naturalHeight;
    if (dim > maxDimensions) {
        maxDimensions = dim;
        biggestImage = img;
    }
}
return biggestImage.src
"""


if __name__ == '__main__':
    main()
