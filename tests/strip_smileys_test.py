from src.strip_smileys import strip_smileys

def strip_smileys_test():
    foo = "LOCK TRUMP UP💗"
    print(strip_smileys(foo))
    assert strip_smileys(foo) == "LOCK TRUMP UP"
    
strip_smileys_test()