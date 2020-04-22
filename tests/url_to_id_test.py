from src.url_to_id import url_to_id

def detect_test():
    url = "https://twitter.com/EmmanuelMacron/status/1194995239322210304"
    tweet_id = 1194995239322210304
    assert url_to_id(url) == tweet_id

detect_test()