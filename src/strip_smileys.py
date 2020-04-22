def strip_smileys(foo):
    foo = ''.join(filter(lambda char : ord(char)<65535, foo))
    return foo