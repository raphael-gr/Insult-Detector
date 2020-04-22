def distance(word1,word2):
    m=len(word1)
    n=len(word2)

    differences=[[0 for i in range(m+1)] for j in range(n+1)]

    #Initialisation du tableau : distance entre les mots formés des premières lettres et ''
    for i in range(m+1):
        differences[0][i]=i
    for j in range(n+1):
        differences[j][0]=j
    
    #Distance de Levenshtein par programmation dynamique
    for i in range(1,n+1):
        for j in range(1,m+1):
            if word1[j-1]==word2[i-1]:
                differences[i][j]=min(differences[i-1][j]+1,differences[i][j-1]+1,differences[i-1][j-1])
            else:
                differences[i][j]=min(differences[i-1][j]+1,differences[i][j-1]+1,differences[i-1][j-1]+1)
    
    return(differences[n][m])
