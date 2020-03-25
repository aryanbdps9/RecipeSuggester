import json
import os
from os import path
import extract

datadir = path.join('..', 'data')
dumpdir = path.join('..', 'dumps')

### READ MEASUREMENT UNITS ######################

measurement_units_path = path.join(datadir, 'measurement_units.txt')
measurement_units = set()
with open(measurement_units_path) as mupf:
    for line in mupf:
        line = line.strip()
        measurement_units.add(line)


##################################################

f1name = 'recipes_raw_nosource_ar.json'
f2name = 'recipes_raw_nosource_epi.json'
f3name = 'recipes_raw_nosource_fn.json'


##################################################
######## READ DATA ###############################
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

###################################################

f1_dumppath = path.join(dumpdir, f1name)
f2_dumppath = path.join(dumpdir, f2name)
f3_dumppath = path.join(dumpdir, f3name)

f1w = open(f1_dumppath, 'w')
f2w = open(f2_dumppath, 'w')
f3w = open(f3_dumppath, 'w')

print("started 1")
extract.sep_ingred_whole_json(data1, measurement_units=measurement_units)
json.dump(data1, f1w, indent=4)
f1w.close()

print("started 2")
extract.sep_ingred_whole_json(data2, measurement_units=measurement_units)
json.dump(data2, f2w, indent=4)
f2w.close()

print("started 3")
extract.sep_ingred_whole_json(data3, measurement_units=measurement_units)
json.dump(data3, f3w, indent=4)
f3w.close()

#################################################
