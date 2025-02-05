import utils
import string_processing as sp

def extract_number(toks):
    # toks tokenises (, ) as well
    if (len(toks) == 0) or not (utils.isInt(toks[0]) or utils.isFloat(toks[0]) or utils.isFrac(toks[0])):
        return [], toks
    if (len(toks) > 1):
        if utils.isInt(toks[0]) and utils.isFrac(toks[1]):
            return toks[:2], toks[2:]
        else:
            return toks[:1], toks[1:]
    if utils.isInt(toks[0]) or utils.isFloat(toks[0]) or utils.isFrac(toks[0]):
        return toks, []
    else:
        return [], toks

def extract_units(toks, measurement_units):
    if (len(toks) == 0):
        return [], toks
    if (len(toks) > 1):
        twin = toks[0]+' '+toks[1]
        if (twin in measurement_units):
            return toks[:2], toks[2:]
        if (toks[0] in measurement_units):
            return toks[:1], toks[1:]
        return [], toks
    if (toks[0] in measurement_units):
        return toks[:1], toks[1:]
    return [], toks

def extract_quantity(toks, measurement_units):
    rmdl = []
    if (len(toks)>1) and (toks[0].lower() in ['about', 'approx', 'approx.', 'around']):
        rmdl.append(toks[0])
        toks = toks[1:]
    try:
        tok_idx = toks.index('(')
        if (tok_idx == 0):
            raise ValueError
        mid_quantity, toks_after_mid_quantity = extract_quantity(toks[tok_idx+1:], measurement_units=measurement_units)
        if (len(mid_quantity) == 0) or (toks_after_mid_quantity[0] != ')'):
            raise ValueError
        start_quantity, toks_after_start_quantity = extract_quantity(toks[:tok_idx], measurement_units=measurement_units)
        if (len(toks_after_start_quantity) != 0):
            raise ValueError
        end_unit, end_toks = extract_units(toks_after_mid_quantity[1:], measurement_units=measurement_units)
        start_quantity.extend(['('])
        start_quantity.extend(mid_quantity)
        start_quantity.extend([')'])
        start_quantity.extend(end_unit)
        return rmdl+start_quantity, end_toks
        
    except (ValueError, IndexError):
        pass

    number, toks_nonum = extract_number(toks=toks)
    if (len(number) == 0):
        return number, rmdl+toks_nonum
    units, toks_nounit = extract_units(toks=toks_nonum, measurement_units=measurement_units)
    return rmdl + number + units, toks_nounit

    # # finally, we have number, units, toks_nounit
    # if (len(toks_nounit) > 0) and (toks_nounit[0] == '('):
    #     sec_quantity, sec_toks_noquantity = extract_quantity(toks=toks_nounit[1:], measurement_units=measurement_units)
    #     if (sec_toks_noquantity[0]!=')'):
    #         return number+units, toks_nounit
    #     return number + units + ['('] + sec_quantity + [')'], sec_toks_noquantity[1:]
    # return number+units, toks_nounit

def extract_quantity_old(toks, measurement_units):
    rmdl = []
    if (len(toks)>1) and (toks[0].lower() in ['about', 'approx', 'approx.', 'around']):
        rmdl.append(toks[0])
        toks = toks[1:]
    number, toks_nonum = extract_number(toks=toks)
    if (len(number) == 0):
        return number, rmdl+toks_nonum
    units, toks_nounit = extract_units(toks=toks_nonum, measurement_units=measurement_units)
    # finally, we have number, units, toks_nounit
    if (len(toks_nounit) > 0) and (toks_nounit[0] == '('):
        sec_quantity, sec_toks_noquantity = extract_quantity(toks=toks_nounit[1:], measurement_units=measurement_units)
        if (sec_toks_noquantity[0]!=')'):
            return number+units, toks_nounit
        return number + units + ['('] + sec_quantity + [')'], sec_toks_noquantity[1:]
    return number+units, toks_nounit

def sep_ingredient(ingredient_string, measurement_units):
    toks = utils.tokenize(ingredient_string)
    if ((len(toks) > 0) and toks[-1].lower() == 'advertisement'):
        toks = toks[:-1]
    quantity, items = extract_quantity(toks, measurement_units=measurement_units)
    quantity = " ".join(quantity)
    items = " ".join(items)
    return quantity, items

def jsonitem_sep_ingredient(jsonitem, measurement_units):
    if 'ingredients' not in jsonitem:
        return
    ingredients = jsonitem['ingredients']
    sep_ingredients = [sep_ingredient(ingredient_string=ingredient_string, measurement_units=measurement_units) for ingredient_string in ingredients]
    sep_ingredients = list(filter(lambda x: len(x[0]) != 0 or len(x[1]) != 0, sep_ingredients))
    jsonitem['sep_ingredients'] = sep_ingredients
    return

def sep_ingred_whole_json(data, measurement_units):
    for key in data:
        jsonitem_sep_ingredient(data[key], measurement_units=measurement_units)
    return
