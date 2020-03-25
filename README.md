# Directory structure
.
├── data # json files need to be unzipped from `recipes_raw.zip`
│   ├── measurement_units.txt
│   ├── recipes_raw_nosource_ar.json
│   ├── recipes_raw_nosource_epi.json
│   ├── recipes_raw_nosource_fn.json
│   └── recipes_raw.zip
├── dumps # will be generated by code.
│   ├── recipes_raw_nosource_ar.json
│   ├── recipes_raw_nosource_epi.json
│   └── recipes_raw_nosource_fn.json
├── README.md # this readme file
├── resources # resources for human reference. Not to be used by machines
│   ├── measurement_units_raw.txt
│   ├── measurement_units.txt
│   ├── notes.txt
│   └── tough_eg.txt
└── scripts # code goes here
    ├── extract.py
    ├── parseIngredients.py
    └── utils.py

# How to run
1. Make sure that you have the json files in `data` folder. It can be obtained by extracting `recipes_raw.zip`.
2. Make sure that `dumps` directory exists. (No need to remove its contents).
2. `cd` into scripts directory and run: `<python 3 name> parseIngredients.py`
    where `<python 3 name>` is the command used to run python 3. Usually it is `python3`, but if you are using **Anaconda**, then, it's simply `python`.
3. The script `parseIngredients.py` will generate `.json` files in `dumps` directory.

