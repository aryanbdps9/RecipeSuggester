import pickle

def load(filename):
    with open(filename, 'rb') as f:
        loaded = pickle.load(f)
    return loaded

def save(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f, protocol=4)
    return

def isFloat(str_):
    try:
        float(str_)
        return True
    except ValueError:
        return False

def isInt(str_):
    try:
        int(str_)
        return True
    except ValueError:
        return False

def isFrac(s): # taken from https://stackoverflow.com/a/29895622
    values = s.split('/')
    return len(values) == 2 and all(i.isdigit() for i in values)

def tokenize(s):
    s = s.replace('(', ' ( ')
    s = s.replace(')', ' ) ')
    res = s.split()
    return res
