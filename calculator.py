def calculator(last_month, curr_month, tax_rate):
    return {'electricity' : round((curr_month['electricity'] - last_month['electricity']) * tax_rate['electricity'], 2),
            'cold_water'  : round((curr_month['cold_water'] - last_month['cold_water']) * tax_rate['cold_water'], 2),
            'hot_water'   : round((curr_month['hot_water'] - last_month['hot_water']) * (tax_rate['water_heating'] + tax_rate['cold_water']), 2)}

tax = {'electricity' : 5.47, 'cold_water' : 40.48, 'water_heating' : 157.71}

augu = {'electricity' : 16552.0, 'hot_water' : 40.755, 'cold_water' : 77.835}
sept = {'electricity' : 16662.0, 'hot_water' : 46.159, 'cold_water' : 84.726}
octo = {'electricity' : 16746.1, 'hot_water' : 51.606, 'cold_water' : 90.826}
nove = {'electricity' : 16835.7, 'hot_water' : 56.988, 'cold_water' : 97.224}
dece = {'electricity' : 16928.0, 'hot_water' : 62.131, 'cold_water' : 103.586}

def summarizer(last_month, curr_month, tax_rate):
    res = calculator(last_month, curr_month, tax_rate)
    text = f'Нынешние показания счетчиков:\n'
    text += f'    Электричество: { curr_month["electricity"] },\n'
    text += f'    Холодная вода: { curr_month["cold_water"] },\n'
    text += f'    Горячая вода: { curr_month["hot_water"] },\n'
    text += f'Показания прошлого месяца:\n'
    text += f'    Электричество: { last_month["electricity"] },\n'
    text += f'    Холодная вода: { last_month["cold_water"] },\n'
    text += f'    Горячая вода: { last_month["hot_water"] },\n'
    text += f'Тариф:\n'
    text += f'    Электричество: { tax_rate["electricity"] },\n'
    text += f'    Холодная вода: { tax_rate["cold_water"] },\n'
    text += f'    Горячая вода:\n'
    text += f'        холодная вода для ГВС { tax_rate["cold_water"] } + подогрев воды { tax_rate["water_heating"] } = { tax_rate["cold_water"] + tax_rate["water_heating"] },\n'
    text += f'Итого:\n'
    text += f'    Электричество:\n'
    text += f'        ({ curr_month["electricity"] } - { last_month["electricity"] }) * { tax_rate["electricity"] } = { res["electricity"] }\n'
    text += f'    Холодная вода:\n'
    text += f'        ({ curr_month["cold_water"] } - { last_month["cold_water"] }) * { tax_rate["cold_water"] } = { res["cold_water"] }\n'
    text += f'    Горячая вода:\n'
    text += f'        ({ curr_month["hot_water"] } - { last_month["hot_water"] }) * ({ tax_rate["cold_water"] } + { tax_rate["water_heating"]}) =  {res["hot_water"] },\n'
    text += f'    Сумма:\n'
    text += f'        { res["electricity"] } + { res["cold_water"] } + { res["hot_water"] } = { res["electricity"] + res["cold_water"] + res["hot_water"] }'
    print(text)
    return res


summarizer(nove, dece, tax)
# summarizer(octo, nove, tax)
# summarizer(sept, octo, tax)
