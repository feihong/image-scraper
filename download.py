import urlparse
import sys
import requests
from selenium import webdriver


browser = webdriver.Firefox()


def main():
    url = sys.argv[1]

    browser.get(url)
    user_agent = browser.execute_script('return window.navigator.userAgent')
    print user_agent
    image_url = get_largest_image_url()
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


def get_largest_image_url():
    return browser.execute_script(JAVASCRIPT)


JAVASCRIPT = """
var images = document.querySelectorAll('img');
var maxArea = 0;
var biggestImage = null;

for (var i=0; i < images.length; i++) {
    var img = images[i];
    if (img.style.display === 'none') {
        continue;
    }
    var area = img.naturalWidth * img.naturalHeight;
    if (biggestImage === null || area > maxArea) {
        maxArea = area;
        biggestImage = img;
    }
}
console.log(biggestImage)
return biggestImage.src
"""


if __name__ == '__main__':
    main()
