import string_processing as sp
import csv
import re

NoAlphaNumWhiteSpacePattern = re.compile('([^ \w])+')


def join_ingredient(jsonitem):
    # I renamed it from sep_ingredient to join_ingredient bcoz sep_ingredient was already defined
    if 'sep_ingredients' not in jsonitem:
        return ""
    sep_ingredients=jsonitem['sep_ingredients']
    s=""
    for ingredients in sep_ingredients:
        if(len(ingredients)>1 and len(ingredients[1])>0):
            s += ingredients[1] + " "
    
    return s

def getIngridient(data,ingredient_list):
    # i=0
    for key in data:
        l=join_ingredient(data[key])
        if(len(l)==0):
            continue
        # print(i)
        # i += 1        
        unique_words=sp.process_text(l)
        for word in unique_words:
            if word not in ingredient_list:
                ingredient_list[word]=[key]
            else:
                ingredient_list[word].append(key)

def wrd2ingrdtdict2tsv(wrd2ingrdtdict, data, filename, descending=True):
    f = open(filename, 'w', encoding='utf-8', newline='\n')
    writer = csv.writer(f, delimiter='\t')
    rows = []
    for key in wrd2ingrdtdict:
        recipe_names = ";;".join([NoAlphaNumWhiteSpacePattern.sub('', data[id_]['title'].replace('\n', ' ')) for id_ in wrd2ingrdtdict[key]])
        row = [key, len(wrd2ingrdtdict[key]), recipe_names]
        # writer.writerow(row)
        rows.append(row)
    rows = sorted(rows, key=lambda ro: ro[1], reverse=descending)
    writer.writerows(rows)
    f.close()

def printdatadict(data, filename):
    f = open(filename, 'w', encoding='utf-8', newline='\n')
    writer = csv.writer(f, delimiter='\t')
    rows = []
    for key in data:
        try:
            row = [key, data[key]['title']]
            writer.writerow(row)
            rows.append(row)
        except KeyError:
            continue
    f.close()

def print_dict_stats(wrd2ingrdtdict, data, filename, descending=True):
    f = open(filename, 'w', encoding='utf-8', newline='\n')
    writer = csv.writer(f, delimiter='\t')
    rows = []
    for key in wrd2ingrdtdict:
        row = [key, len(wrd2ingrdtdict[key])]
        # writer.writerow(row)
        rows.append(row)
    rows = sorted(rows, key=lambda ro: ro[1], reverse=descending)
    writer.writerows(rows)
    f.close()
