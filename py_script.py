import requests
import pandas

def pad_dict_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if  ll < lmax:
            dict_list[lname] += [padel] * (lmax - ll)
    return dict_list

def buscar_dados():
    request = requests.get("http://localhost:8000/artigos")
    
    category = []
    categoryCounter = []
    
    authors = []
    authorsCounter = []
    
    json_request = request.json()
    
    num=0
    den=len(json_request)
    
    for i in json_request:
        cat=i['category'].upper()
        
        if cat not in category:
            category.append(cat)
            categoryCounter.append(1)
        else:
            for i, ind in enumerate(category):
                if cat == category[i]:
                    categoryCounter[i]+=1
        
    for i in json_request:
        aut=i['author'].upper()
        
        if aut not in authors:
            authors.append(aut)
            authorsCounter.append(1)
        else:
            for i, ind in enumerate(authors):
                if aut == authors[i]:
                    authorsCounter[i]+=1
                    
    for i in json_request:
        cont=i['content'].split()
        
        num+=len(cont)
        
    media = num / den
    media = str(round(media, 2))
    
    artigos = {
        'Autor': authors,
        'Qtd de artigos aut': authorsCounter,
        'Categoria': category,
        'Qtd de artigos cat': categoryCounter,
        'Media de palavras no conteudo': media
        }
    df = pad_dict_list(artigos, 0)
    df = pandas.DataFrame(df)
    df.to_csv("C:/Users/betin/Documents/artigos.csv", index=False)
    
buscar_dados()