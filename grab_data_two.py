import sqlite3
def user_username(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Username FROM user_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows

def user_password(password):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Password FROM user_info WHERE Password = '{password}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows

def user_amba(amba_code):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Ambassador_Code FROM user_info WHERE Ambassador_Code = '{amba_code}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows

def balance_balance(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Investment_Balance, Interest_Balance FROM balance_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 0.0
            return rows
        else:  
            a = 0
            for i in rows[0]:
                a += i
            return a

def amba_refered(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Referred_Users FROM amba_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 0
            return rows
        else:  
            return rows[0][0]

def user_tele(tele_id):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Telegram_ID FROM user_info WHERE Telegram_ID = '{tele_id}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows

def with_status():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Current_Status FROM withdraws WHERE Current_Status = 'Pending'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows

def with_serial():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Serial FROM withdraws WHERE Current_Status = 'Pending'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows

def mana_id(id_Number):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT ID_Number FROM managers WHERE ID_Number = '{id_Number}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows


def mana_password(password):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Password FROM managers WHERE Password = '{password}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows

def mana_access(id_number):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Special_Access FROM managers WHERE ID_Number = '{id_number}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows[0][0]

def user_user(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM user_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows[0]
        else:
            return rows[0]
    
def mana_mana(id_number):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM managers WHERE ID_Number = '{id_number}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows[0]
        else:
            return rows[0]

def with_details(serial):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Username, Time, Withdraw_Amount, Serial, Withdrawal_Address FROM withdraws WHERE Serial = '{serial}'")
        rows = cur.fetchall()
        return rows[0]
    
def user_all():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Username FROM user_info")
        rows = cur.fetchall()
        return rows

def mana_all():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT ID_Number FROM managers")
        rows = cur.fetchall()
        return rows

def inve_cate(category):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Investment_Type FROM investment_details WHERE Investment_Category = '{category}'")
        rows = cur.fetchall()
        unique_list = []
        for a in rows:
            if a[0] in unique_list:
                pass
            else:
                unique_list.append(a[0])
        return unique_list

def inve_name(name):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Investment_Name FROM investment_details WHERE Investment_Type = '{name}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            a = []
            for b in rows:
                a.append(b[0])
            return a

def inve_price(name):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Cost FROM investment_details WHERE Investment_Name = '{name}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return int(rows[0][0])

def inve_rate(name):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Payout_Rate FROM investment_details WHERE Investment_Name = '{name}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows[0][0]

def inve_cate_two():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Investment_Category FROM investment_details")
        rows = cur.fetchall()
        unique_list = []
        for a in rows:
            if a[0] in unique_list:
                pass
            else:
                unique_list.append(a[0])
        return unique_list

def inve_type(typ):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Investment_Type FROM investment_details WHERE Investment_Type = '{typ}'")
        rows = cur.fetchall()
        unique_list = []
        for a in rows:
            if a[0] in unique_list:
                pass
            else:
                unique_list.append(a[0])
        return unique_list

def inve_name_two(name):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Investment_Name FROM investment_details WHERE Investment_Name = '{name}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows[0][0]

def inve_bala(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Investment_Balance FROM balance_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        return rows[0][0]

def amba_users(refer):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Referred_Users FROM amba_info WHERE Ambassador_Code = '{refer}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 0
            return rows
        else:  
            return rows[0][0]

def dep_total():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM deposits")
        rows = cur.fetchall()
        COLUMN = 5
        column=[elt[COLUMN] for elt in rows]
        tot = 0
        for a in column:
            tot += a
        d = "%.2f" % tot 
        return d

def with_total():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM withdraws")
        rows = cur.fetchall()
        COLUMN = 6
        column=[elt[COLUMN] for elt in rows]
        tot = 0
        for a in column:
            tot += a
        d = "%.2f" % tot 
        return d

def inve_sold(product):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Time_Sold FROM investment_details WHERE Investment_Name = '{product}'")
        rows = cur.fetchall()
        return rows[0][0]

def holding_user(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Username FROM investment_holding WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'No'
            return rows
        else:
            return rows[0][0]

def holding_holding(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Holdings FROM investment_holding WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        elif rows[0][0] == '':
            rows = 'Nothing'
            return rows
        else:
            return rows[0][0]

def hold_stand(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Standard_Holding FROM investment_holding WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows[0][0]

def hold_promo(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Promotional_Holding FROM investment_holding WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows[0][0]
        
def descri_pro(product):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Description FROM investment_description WHERE Investment_Type = '{product}'")
        rows = cur.fetchall()
        return rows[0][0]

def trans_det(Username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Type, Time, Prodcuct_Name, Transaction_Value FROM investment_transactions WHERE Username = '{Username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows

def holding_holding_two():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT Username, Holdings FROM investment_holding")
        rows = cur.fetchall()
        return rows


def amba_bonus(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Bonus_Given FROM amba_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        return rows[0][0]

def inve_bonus(product):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT One_Time_Bonus FROM investment_details WHERE Investment_Name = '{product}'")
        rows = cur.fetchall()
        return int(rows[0][0])

def amba_used(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Ambassador_Code_Used FROM amba_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        return rows[0][0]

def amba_username(amba):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Username FROM amba_info WHERE Ambassador_Code = '{amba}'")
        rows = cur.fetchall()
        return rows[0][0]

def balance_amba(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Ambassador_Balance FROM balance_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        return rows[0][0]

def ambaused_username(amba):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Username FROM amba_info WHERE Ambassador_Code_Used = '{amba}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:
            return rows


def ambato_username(user):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Ambassador_Code FROM amba_info WHERE Username = '{user}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:
            return rows[0][0]

def amba_amba(amba):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Ambassador_Code_Used FROM amba_info WHERE Ambassador_Code = '{amba}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:
            return rows[0][0]

def amba_all():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Ambassador_Code FROM amba_info")
        rows = cur.fetchall()
        return rows

def holding_enrolled(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Enrolled FROM Investment_holding WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows[0][0]

def amba_tree(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Tree_Investment FROM amba_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 0
            return rows
        else:
            return rows[0][0]

def milestone_tier(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Tier_1,Tier_2,Tier_3,Tier_4,Tier_5,Tier_6 FROM milestone_bonus WHERE Username = '{username}'")
        rows = cur.fetchall()
        return rows[0]

def qualified_mile(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Qualified_Milestone FROM amba_info WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 0
            return rows
        else:
            return rows[0][0]

def ambatra_referral(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Type, Amount, Description FROM ambassador_transactions WHERE Username = '{username}' AND Type = 'Referral'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows

def ambatra_milestone(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Type, Amount, Description FROM ambassador_transactions WHERE Username = '{username}' AND Type = 'Milestone'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows

def ambatra_residual(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Type, Amount, Description FROM ambassador_transactions WHERE Username = '{username}' AND Type = 'Residual'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows

def depo_user(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Time, Transaction_Hash, Deposited_Amount FROM Deposits WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows

def with_user(username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Time, Withdrawal_Address, Transaction_Hash, Withdraw_Amount, Current_Status FROM Withdraws WHERE Username = '{username}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows

def descri_pending():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT Investment_Type FROM investment_description WHERE Payout_Pending = 'True'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows

def inve_products(product):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute(f"SELECT Investment_Name FROM investment_details WHERE Investment_Type = '{product}'")
        rows = cur.fetchall()
        if rows == []:
            rows = 'Nothing'
            return rows
        else:
            return rows

def withdraw_serial():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM withdraws")
        rows = cur.fetchall()
        COLUMN = 8
        column=[elt[COLUMN] for elt in rows]
        return column[-1]

def deposits():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM deposits")
        rows = cur.fetchall()
        COLUMN = 5
        column=[elt[COLUMN] for elt in rows]
        COLUMN = 2
        column2=[elt[COLUMN] for elt in rows]
        COLUMN = 3
        column3=[elt[COLUMN] for elt in rows]
        return column, column2, column3

def withdraws():
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM withdraws")
        rows = cur.fetchall()
        COLUMN = 2
        column=[elt[COLUMN] for elt in rows]
        COLUMN = 3
        column2=[elt[COLUMN] for elt in rows]
        COLUMN = 6
        column3=[elt[COLUMN] for elt in rows]
        return column, column2, column3