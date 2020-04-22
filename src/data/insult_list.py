def create_insult_list():
    """
        :return:(list) a list of all insults contained in inlusts.txt
    """
    insult_list = []
    with open("src/data/insults.txt", "r") as file:  
        #insults.txt and insult_list.py 
        # must be in the same directory 
        line = file.readline()
        while line: # if line isn't empty, then file isn't over
            insult_list.append(line.strip())
            line = file.readline()
    return(insult_list)

