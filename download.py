import sys
import base64
from selenium import webdriver


def main():
    url = sys.argv[1]

    browser = webdriver.Firefox()
    browser.get(url)
    browser.set_script_timeout(20)
    data_uri = browser.execute_async_script(JAVASCRIPT)
    with open('image.png', 'wb') as fp:
        fp.write(base64.decodestring(data_uri))


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
// Convert image to base64.
var resolve = arguments[arguments.length - 1];
//resolve('foobar')
var img = new Image();
img.crossOrigin = 'Anonymous';
img.onload = function() {
    var canvas = document.createElement('CANVAS');
    canvas.height = this.height;
    canvas.width = this.width;
    canvas.getContext('2d').drawImage(this, 0, 0);
    data = canvas.toDataURL('image/png').replace(/^data:image\/(png|jpg);base64,/, '');
    canvas = null;
    resolve(data);
};
img.src = biggestImage.src;
"""


if __name__ == '__main__':
    main()
