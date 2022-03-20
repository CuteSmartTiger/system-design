import hashlib
import time

SHORT_URL_LENGTH = 6


def get_long_url_hash(long_url):
    if not isinstance(long_url, str):
        raise Exception('need string')

    long_url = long_url + str(time.time())
    encode_long_url = long_url.encode('utf8')

    return int(hashlib.md5(encode_long_url).hexdigest(), 16)


def get_short_url(num):
    if not num:
        raise Exception('there need num')

    base62_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    url = ""

    # for each digit find the base 62
    while num > 0:
        url += base62_map[num % 62]
        num //= 62

    # reversing the url
    return url[::-1][:SHORT_URL_LENGTH]


if __name__ == '__main__':
    URL = 'https://www.google.com.hk/search?q'
    n = get_long_url_hash(URL)
    short_url = get_short_url(n)

    print(short_url)
