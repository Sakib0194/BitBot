#!/usr/bin/env python3
import grab_data_two

def details(product, cur):
    pro = grab_data_two.inve_name(product, cur)
    cost = {}
    for i in pro:
        cost[i] = grab_data_two.inve_price(i, cur)
    all_holdings = grab_data_two.holding_holding_two(cur)
    holding_sorted = {}
    values = {}
    for i in all_holdings:
        for h in i:
            if h == None or len(h) == 0:
                all_holdings.remove(i)
    for i in all_holdings:
        holding_sorted[i[0]] = i[1]
    eli_pro = {}
    for i in holding_sorted:
        data = []
        a = holding_sorted[i].split(' ')
        for h in range(len(a)):
            if a[h] in pro:
                data.append(a[h])
                data.append(a[h+1])
            else:
                pass
        if data == []:
            pass
        else:
            eli_pro[i] = data
    if eli_pro == {}:
        a = 'Nothing'
        return a
    else:
        for i in eli_pro:
            dat = eli_pro[i]
            for h in range(len(dat)):
                if dat[h].isnumeric():
                    pass
                else:
                    price = cost[dat[h]]
                    total = price * int(dat[h+1])
                    values[i] = total
        return values
