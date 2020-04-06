import json
import os
from os import path
import extract
import utils
import ingredient_dictionary_helper as idh

datadir=os.path.join('..','dumps')
f1name = 'recipes_raw_nosource_ar.json'
f2name = 'recipes_raw_nosource_epi.json'
f3name = 'recipes_raw_nosource_fn.json'

ingr_dict_name='ingredient_dictionary.pkl'

f1path = path.join(datadir, f1name)
f2path = path.join(datadir, f2name)
f3path = path.join(datadir, f3name)

print("loading data...")
f1r = open(f1path, 'r')
f2r = open(f2path, 'r')
f3r = open(f3path, 'r')

data1 = json.load(f1r)
data2 = json.load(f2r)
data3 = json.load(f3r)
f1r.close()
f2r.close()
f3r.close()
print("Done loading data!")

ing_file = path.join(datadir, ingr_dict_name)
# ing_filew= open(ing_file,'w')

ingredient_list={}

try:
    ingredient_list = utils.load(ing_file)
    print("loaded ingredient list from disk...")
except Exception as e:
    print('started 1')
    idh.getIngridient(data1,ingredient_list)
    print('ended 1')

    print('started 2')
    idh.getIngridient(data2,ingredient_list)
    print('ended 1')

    print('started 3')
    idh.getIngridient(data3,ingredient_list)
    print('ended 3')

    utils.save(ingredient_list, ing_file)
    print('saved ingredient list to disk...')

data = {}
data.update(data1)
data.update(data2)
data.update(data3)

idh.wrd2ingrdtdict2tsv(ingredient_list, data, path.join(datadir, 'bigdict.tsv')) # Unless you wanna freeze your computer, DON'T OPEN IT! XD
idh.print_dict_stats(ingredient_list, data, path.join(datadir, 'bigdict_stats.tsv'))

