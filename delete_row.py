def user_info(username, cur):
        a = f"DELETE FROM user_info WHERE Username = '{username}'"
        b = f"DELETE FROM amba_info WHERE Username = '{username}'"
        c = f"DELETE FROM balance_info WHERE Username = '{username}'"
        d = f"DELETE FROM investment_holding WHERE Username = '{username}'"
        e = f"DELETE FROM milestone_bonus WHERE Username = '{username}'"
        cur.execute(a)
        cur.execute(b)
        cur.execute(c)
        cur.execute(d)
        cur.execute(e)



#user_info('FakeAcc')

def delete_user(username, cur):
    c = f"DELETE FROM user_info WHERE username = '{username}'"
    cur.execute(c)