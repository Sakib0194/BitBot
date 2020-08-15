import grab_data_two,update_data
all_data = {}
def down(refer):
    to_track = []
    investments = {}
    refers = grab_data_two.ambaused_username(refer)
    for i in refers:
        to_track.append(i[0])
    a = 0
    while to_track != []:
        c = grab_data_two.hold_stand(to_track[a])
        b = grab_data_two.hold_promo(to_track[a])
        if c == 'Nothing':
            c = 0
            b = 0
        if 'N' in to_track:
            to_track.remove('N')
        if to_track == []:
            break
        #print(to_track)
        investments[to_track[a]] = b + c
        #print(to_track)
        
        amba = grab_data_two.ambato_username(to_track[a])
        #print(amba)
        referrals = grab_data_two.ambaused_username(amba)
        for i in referrals:
            if i == 'Nothing':
                pass
            else:
                #print(i[0])
                if i[0] == 'Nothing':
                    pass
                else:
                    to_track.append(i[0])
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


def up(username):
    manage = ''
    to_track = []
    amba_code = grab_data_two.ambato_username(username)
    to_track.append(amba_code)
    if amba_code == 'MANAGER':
        manage = grab_data_two.amba_username(amba_code)
        to_track.remove(to_track[0])
    else:
        while to_track != []:
            a = grab_data_two.amba_amba(to_track[0])
            if a == 'Nothing' or a == 'MANAGER' or a == '0GAN7KD':
                to_track.remove(to_track[0])
                if a == 'Nothing':
                    pass
                else:
                    manage = grab_data_two.amba_username(a)
            else:
                to_track[0] = a
    return manage

def qualified_mile(username):
    enroll = grab_data_two.holding_enrolled(username)
    qualify = 0
    amba_used = grab_data_two.amba_used(username)
    amba_username = grab_data_two.amba_username(amba_used)
    if enroll == 'True':
        direct_ref = grab_data_two.ambaused_username(amba_used)
        for i in direct_ref:
            en = grab_data_two.holding_enrolled(i[0])
            if en == 'True':
                qualify += 1
            else:
                pass
    amount = down(amba_used)
    update_data.tree_investment(amba_used, amount)
    update_data.qualified_milestone(amba_username, qualify)


def qualified_resi(username):
    enroll = grab_data_two.holding_enrolled(username)
    amba_used = grab_data_two.amba_used(username)
    amba_username = grab_data_two.amba_username(amba_used)
    qualify = 0
    if enroll == 'True':
        direct_ref = grab_data_two.ambaused_username(amba_used)
        for i in direct_ref:
            en = grab_data_two.holding_enrolled(i[0])
            if en == 'True':
                promo = grab_data_two.hold_promo(username)
                stand = grab_data_two.hold_stand(username)
                if promo+stand >= 1000000:
                    qualify += 1
                else:
                    pass
    amount = down(amba_used)
    update_data.tree_investment(amba_used, amount)
    update_data.qualified_residual(amba_username, qualify)



