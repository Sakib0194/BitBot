import grab_data_two,update_data
import mysql.connector
all_data = {}
def down(refer, cur):
    to_track = []
    investments = {}
    refers = grab_data_two.ambaused_username(refer, cur)
    for i in refers:
        to_track.append(i[0])
    a = 0
    while to_track != []:
        c = grab_data_two.hold_stand(to_track[a], cur)
        b = grab_data_two.hold_promo(to_track[a], cur)
        if c == 'Nothing':
            c = 0
        if b == 'Nothing':
            b = 0
        if 'N' in to_track:
            to_track.remove('N')
        if to_track == []:
            break
        #print(to_track)
        investments[to_track[a]] = b + c
        #print(to_track)
        
        amba = grab_data_two.ambato_username(to_track[a], cur)
        #print(amba)
        referrals = grab_data_two.ambaused_username(amba, cur)
        for i in referrals:
            if i == 'Nothing':
                pass
            else:
                #print(i[0])
                if i[0] == 'Nothing':
                    pass
                else:
                    to_track.append(i[0])
        #print(to_track)
        to_track.remove(to_track[a])
    tot = 0
    for i in investments:
        tot += investments[i]
    all_data[refer] = tot
    return tot

'''a = grab_data_two.amba_all()
for i in a:
    down(i[0])
for h in all_data:
    print(h, all_data[h])
    update_data.tree_investment(h, all_data[h])'''


def up(username, cur):
    manage = ''
    to_track = []
    amba_code = grab_data_two.ambato_username(username, cur)
    to_track.append(amba_code)
    if amba_code == 'MANAGER':
        manage = grab_data_two.amba_username(amba_code, cur)
        to_track.remove(to_track[0])
    else:
        while to_track != []:
            a = grab_data_two.amba_amba(to_track[0], cur)
            if a == 'Nothing' or a == 'MANAGER' or a == '0GAN7KD' or a == 'LVXD4A8' or a == 'ADMIN':
                to_track.remove(to_track[0])
                if a == 'Nothing' or a == 'ADMIN':
                    pass
                else:
                    manage = grab_data_two.amba_username(a, cur)
            else:
                to_track[0] = a
    return manage

def qualified_mile(username, cur):
    qualify = 0
    amba_used = grab_data_two.amba_used(username, cur)
    if amba_used == 'ADMIN':
        amba_username = 'vito'
    else:
        amba_username = grab_data_two.amba_username(amba_used, cur)
        direct_ref = grab_data_two.ambaused_username(amba_used, cur)
        for i in direct_ref:
            en = grab_data_two.holding_enrolled(i[0], cur)
            if en == 'True':
                qualify += 1
            else:
                pass
    amount = down(amba_used, cur)
    update_data.tree_investment(amba_used, amount, cur)
    update_data.qualified_milestone(amba_username, qualify, cur)


def qualified_resi(username, cur):
    amba_used = grab_data_two.amba_used(username, cur)
    if amba_used == 'ADMIN':
        amba_username = 'vito'
    else:
        amba_username = grab_data_two.amba_username(amba_used, cur)
    qualify = 0
    direct_ref = grab_data_two.ambaused_username(amba_used, cur)
    for i in direct_ref:
        en = grab_data_two.holding_enrolled(i[0], cur)
        if en == 'True':
            promo = grab_data_two.hold_promo(i[0], cur)
            stand = grab_data_two.hold_stand(i[0], cur)
            if promo+stand >= 1000000:
                qualify += 1
            else:
                pass
    amount = down(amba_used, cur)
    update_data.tree_investment(amba_used, amount, cur)
    update_data.qualified_residual(amba_username, qualify, cur)


def resi_per(username, cur):
    amba_code = grab_data_two.ambato_username(username, cur)
    tree = float(down(amba_code, cur))
    promo = float(grab_data_two.hold_promo(username, cur))
    stand = float(grab_data_two.hold_stand(username, cur))
    resi_num = grab_data_two.quali_resi(username, cur)[0][1] 
    percentage = 0
    if tree+promo+stand >= 5000000 and resi_num >= 2:
        percentage = 2
    if tree+promo+stand >= 10000000 and resi_num >= 2:
        percentage = 2
    if tree+promo+stand >= 50000000 and resi_num >= 2:
        percentage = 3
    if tree+promo+stand >= 100000000 and resi_num >= 2:
        percentage = 4
    update_data.tree_percentage(username, percentage, cur)
    update_data.tree_investment(amba_code, tree, cur)

'''all_users = grab_data_two.user_all()
for i in all_users:
    print(i[0])
    qualified_mile(i[0])
    qualified_resi(i[0])
    resi_per(i[0])'''

def all_refer(refer, cur):
    to_track = []
    all_username = []
    investments = {}
    refers = grab_data_two.ambaused_username(refer, cur)
    for i in refers:
        if i[0] == 'N':
            pass
        else:
            all_username.append(i[0])
        to_track.append(i[0])
    a = 0
    while to_track != []:
        c = grab_data_two.hold_stand(to_track[a], cur)
        b = grab_data_two.hold_promo(to_track[a], cur)
        if c == 'Nothing':
            c = 0
        if b == 'Nothing':
            b = 0
        if 'N' in to_track:
            to_track.remove('N')
        if to_track == []:
            break
        #print(to_track)
        investments[to_track[a]] = b + c
        #print(to_track)
        
        amba = grab_data_two.ambato_username(to_track[a], cur)
        #print(amba)
        referrals = grab_data_two.ambaused_username(amba, cur)
        for i in referrals:
            if i == 'Nothing':
                pass
            else:
                #print(i[0])
                if i[0] == 'Nothing':
                    pass
                else:
                    if i[0] in all_username or i[0] == 'N':
                        pass
                    else:
                        all_username.append(i[0])
                    to_track.append(i[0])
        #print(to_track)
        to_track.remove(to_track[a])
    tot = 0
    for i in investments:
        tot += investments[i]
    all_data[refer] = tot
    return all_username

