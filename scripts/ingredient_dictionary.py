import json
import os
from os import path
import extract

datadir=os.path.join('..','dumps')
f1name = 'recipes_raw_nosource_ar.json'
f2name = 'recipes_raw_nosource_epi.json'
f3name = 'recipes_raw_nosource_fn.json'

ingr_dict_name='ingredient_dictionary.json'

f1path = path.join(datadir, f1name)
f2path = path.join(datadir, f2name)
f3path = path.join(datadir, f3name)

f1r = open(f1path, 'r')
f2r = open(f2path, 'r')
f3r = open(f3path, 'r')

data1 = json.load(f1r)
data2 = json.load(f2r)
data3 = json.load(f3r)
f1r.close()
f2r.close()
f3r.close()

ing_file = path.join(datadir, ingr_dict_name)
ing_filew= open(ing_file,'w')

ingredient_list={}

print('started 1')
extract.getIngridient(data1,ingredient_list)
print('ended 1')

print('started 2')
extract.getIngridient(data2,ingredient_list)
print('ended 1')


print('started 3')
extract.getIngridient(data3,ingredient_list)
print('ended 3')

json.dump(ingredient_list, ing_filew, indent=4)
ing_filew.close()

