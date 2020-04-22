def create_dictionary():
    """
        :return:(list) a list of all insults contained in inlusts.txt
    """
    dictionary = []
    with open("src/data/dictionary.txt", "r") as file:  
        #insults.txt and insult_list.py 
        # must be in the same directory 
        line = file.readline()
        while line: # if line isn't empty, then file isn't over
            dictionary.append(line.strip())
            line = file.readline()
    return(dictionary)