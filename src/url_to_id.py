def url_to_id(url):
    """ Takes a tweet url and returns its id """
    character_list = url.split('/')
    return int(character_list[5]) # The tweet's id is after the 5th slash

