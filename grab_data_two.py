#!/usr/bin/env python3
def user_username(username, cur):
    cur.execute(f"SELECT Username FROM user_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows
    else:  
        return rows

def user_password(username, cur):
    cur.execute(f"SELECT Password FROM user_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:  
        return rows[0][0]

def user_amba(amba_code, cur):
    cur.execute(f"SELECT Ambassador_Code FROM user_info WHERE Ambassador_Code = '{amba_code}'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows
    else:  
        return rows

def balance_balance(username, cur):
    cur.execute(f"SELECT Investment_Balance FROM balance_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 0.0
        return rows
    else:  
        a = 0
        for i in rows[0]:
            a += i
        return a

def amba_refered(username, cur):
    cur.execute(f"SELECT Referred_Users FROM amba_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:  
        return rows[0][0]

def user_tele(tele_id, cur):
        cur.execute(f"SELECT Telegram_ID FROM user_info WHERE Telegram_ID = '{tele_id}'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows

def with_status(cur):
        cur.execute(f"SELECT Current_Status FROM withdraws WHERE Current_Status = 'Pending'")
        rows = cur.fetchall()
        if rows == []:
            rows = ['Nothing']
            return rows
        else:  
            return rows

def with_serial(cur):
    cur.execute(f"SELECT Serial FROM withdraws WHERE Current_Status = 'Pending'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows
    else:  
        return rows

def mana_id(id_Number, cur):
    cur.execute(f"SELECT ID_Number FROM managers WHERE ID_Number = '{id_Number}'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows
    else:  
        return rows


def mana_password(id_number, cur):
    cur.execute(f"SELECT Password FROM managers WHERE ID_Number = '{id_number}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:  
        return rows[0][0]

def mana_access(id_number, cur):
    cur.execute(f"SELECT Special_Access FROM managers WHERE ID_Number = '{id_number}'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows
    else:  
        return rows[0][0]

def user_user(username, cur):
    cur.execute(f"SELECT * FROM user_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows[0]
    else:
        return rows[0]
    
def mana_mana(id_number, cur):
    cur.execute(f"SELECT * FROM managers WHERE ID_Number = '{id_number}'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows[0]
    else:
        return rows[0]

def with_details(serial, cur):
    cur.execute(f"SELECT Username, Time, Withdraw_Amount, Serial, Withdrawal_Address FROM withdraws WHERE Serial = '{serial}'")
    rows = cur.fetchall()
    return rows[0]
    
def user_all(cur):
    cur.execute(f"SELECT Username FROM user_info")
    rows = cur.fetchall()
    return rows

def mana_all(cur):
    cur.execute(f"SELECT ID_Number FROM managers")
    rows = cur.fetchall()
    return rows

def inve_cate(category, cur):
    cur.execute(f"SELECT Investment_Type FROM investment_details WHERE Investment_Category = '{category}'")
    rows = cur.fetchall()
    unique_list = []
    for a in rows:
        if a[0] in unique_list:
            pass
        else:
            unique_list.append(a[0])
    return unique_list



def inve_name(name, cur):
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

def inve_price(name, cur):
    cur.execute(f"SELECT Cost FROM investment_details WHERE Investment_Name = '{name}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return int(rows[0][0])

def inve_rate(name, cur):
    cur.execute(f"SELECT Payout_Rate FROM investment_details WHERE Investment_Name = '{name}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows[0][0]

def inve_cate_two(cur):
    cur.execute(f"SELECT Investment_Category FROM investment_details")
    rows = cur.fetchall()
    unique_list = []
    for a in rows:
        if a[0] in unique_list:
            pass
        else:
            unique_list.append(a[0])
    return unique_list

def inve_type(typ, cur):
    cur.execute(f"SELECT Investment_Type FROM investment_details WHERE Investment_Type = '{typ}'")
    rows = cur.fetchall()
    unique_list = []
    for a in rows:
        if a[0] in unique_list:
            pass
        else:
            unique_list.append(a[0])
    return unique_list

def inve_name_two(name, cur):
    cur.execute(f"SELECT Investment_Name FROM investment_details WHERE Investment_Name = '{name}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows[0][0]

def inve_bala(username, cur):
    cur.execute(f"SELECT Investment_Balance FROM balance_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    return rows[0][0]

def amba_users(refer, cur):
    cur.execute(f"SELECT Referred_Users FROM amba_info WHERE Ambassador_Code = '{refer}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:  
        return rows[0][0]

def dep_total(cur):
    cur.execute("SELECT * FROM deposits")
    rows = cur.fetchall()
    COLUMN = 5
    column=[elt[COLUMN] for elt in rows]
    tot = 0
    for a in column:
        tot += a
    d = "%.2f" % tot 
    return d

def with_total(cur):
    cur.execute("SELECT * FROM withdraws")
    rows = cur.fetchall()
    COLUMN = 6
    column=[elt[COLUMN] for elt in rows]
    tot = 0
    for a in column:
        tot += a
    d = "%.2f" % tot 
    return d

def inve_sold(product, cur):
    cur.execute(f"SELECT Time_Sold FROM investment_details WHERE Investment_Name = '{product}'")
    rows = cur.fetchall()
    return rows[0][0]

def holding_user(username, cur):
    cur.execute(f"SELECT Username FROM investment_holding WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'No'
        return rows
    else:
        return rows[0][0]

def holding_holding(username, cur):
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

def hold_stand(username, cur):
    cur.execute(f"SELECT Standard_Holding FROM investment_holding WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows[0][0]

def hold_promo(username, cur):
    cur.execute(f"SELECT Promotional_Holding FROM investment_holding WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows[0][0]
        
def descri_pro(product, cur):
    cur.execute(f"SELECT Description FROM investment_description WHERE Investment_Type = '{product}'")
    rows = cur.fetchall()
    return rows[0][0]

def trans_det(Username, cur):
    cur.execute(f"SELECT Type, Time, Product_Name, Transaction_Value FROM investment_transactions WHERE Username = '{Username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def holding_holding_two(cur):
    cur.execute("SELECT Username, Holdings FROM investment_holding")
    rows = cur.fetchall()
    return rows

def amba_bonus(username, cur):
    cur.execute(f"SELECT Bonus_Given FROM amba_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    return rows[0][0]

def inve_bonus(product, cur):
    cur.execute(f"SELECT One_Time_Bonus FROM investment_details WHERE Investment_Name = '{product}'")
    rows = cur.fetchall()
    return int(rows[0][0])

def amba_used(username, cur):
    cur.execute(f"SELECT Ambassador_Code_Used FROM amba_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    return rows[0][0]

def amba_username(amba, cur):
    cur.execute(f"SELECT Username FROM amba_info WHERE Ambassador_Code = '{amba}'")
    rows = cur.fetchall()
    return rows[0][0]

def balance_amba(username, cur):
    cur.execute(f"SELECT Ambassador_Balance FROM balance_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    return rows[0][0]
    
def balance_inte(username, cur):
    cur.execute(f"SELECT Interest_Balance FROM balance_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    return rows[0][0]

def ambaused_username(amba, cur):
    cur.execute(f"SELECT Username FROM amba_info WHERE Ambassador_Code_Used = '{amba}'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows
    else:
        return rows

def ambato_username(user, cur):
    cur.execute(f"SELECT Ambassador_Code FROM amba_info WHERE Username = '{user}'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows
    else:
        return rows[0][0]

def amba_amba(amba, cur):
    cur.execute(f"SELECT Ambassador_Code_Used FROM amba_info WHERE Ambassador_Code = '{amba}'")
    rows = cur.fetchall()
    if rows == []:
        rows = ['Nothing']
        return rows
    else:
        return rows[0][0]

def amba_all(cur):
    cur.execute(f"SELECT Ambassador_Code FROM amba_info")
    rows = cur.fetchall()
    return rows

def holding_enrolled(username, cur):
    cur.execute(f"SELECT Enrolled FROM investment_holding WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows[0][0]

def amba_tree(username, cur):
    cur.execute(f"SELECT Tree_Investment FROM amba_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:
        return rows[0][0]

def milestone_tier(username, cur):
    cur.execute(f"SELECT Tier_1,Tier_2,Tier_3,Tier_4,Tier_5,Tier_6 FROM milestone_bonus WHERE Username = '{username}'")
    rows = cur.fetchall()
    return rows[0]

def qualified_mile(username, cur):
    cur.execute(f"SELECT Qualified_Milestone FROM amba_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:
        return rows[0][0]

def ambatra_referral(username, cur):
    cur.execute(f"SELECT Type, Amount, Description FROM ambassador_transactions WHERE Username = '{username}' AND Type = 'Referral'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def ambatra_milestone(username, cur):
    cur.execute(f"SELECT Type, Amount, Description FROM ambassador_transactions WHERE Username = '{username}' AND Type = 'Milestone'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def ambatra_residual(username, cur):
    cur.execute(f"SELECT Type, Amount, Description FROM ambassador_transactions WHERE Username = '{username}' AND Type = 'Residual'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def depo_user(username, cur):
    cur.execute(f"SELECT Time, Transaction_Hash, Deposited_Amount FROM deposits WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def with_user(username, cur):
    cur.execute(f"SELECT Time, Withdrawal_Address, Transaction_Hash, Withdraw_Amount, Current_Status FROM withdraws WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def descri_pending(cur):
    cur.execute("SELECT Investment_Type FROM investment_description WHERE Payout_Pending = 'True'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        unique_list = []
        for i in rows:
            unique_list.append(i[0])
        return unique_list

def descri_false(cur):
    cur.execute("SELECT Investment_Type FROM investment_description WHERE Payout_Pending = 'False'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        unique_list = []
        for i in rows:
            unique_list.append(i[0])
        return unique_list

def inve_products(product, cur):
    cur.execute(f"SELECT Investment_Name FROM investment_details WHERE Investment_Type = '{product}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def withdraw_serial(cur):
    cur.execute("SELECT * FROM withdraws")
    rows = cur.fetchall()
    COLUMN = 8
    column=[elt[COLUMN] for elt in rows]
    return column[-1]

def deposits(cur):
    cur.execute("SELECT * FROM deposits")
    rows = cur.fetchall()
    COLUMN = 5
    column=[elt[COLUMN] for elt in rows]
    COLUMN = 2
    column2=[elt[COLUMN] for elt in rows]
    COLUMN = 3
    column3=[elt[COLUMN] for elt in rows]
    return column, column2, column3

def withdraws(cur):
    cur.execute("SELECT * FROM withdraws")
    rows = cur.fetchall()
    COLUMN = 2
    column=[elt[COLUMN] for elt in rows]
    COLUMN = 3
    column2=[elt[COLUMN] for elt in rows]
    COLUMN = 6
    column3=[elt[COLUMN] for elt in rows]
    return column, column2, column3

def pay_rate(category, cur):
    cur.execute(f"SELECT Payout_rate FROM investment_description WHERE Investment_Type = '{category}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows[0][0]

def payout_details(username, cur):
    cur.execute(f"SELECT Investment_Type, Value FROM payout_transactions WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def payout_everything(username, cur):
    cur.execute(f"SELECT Username, Investment_Type, Value FROM payout_transactions WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def payout_value(username, cur):
    cur.execute(f"SELECT Value FROM payout_transactions WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:
        full_value = 0
        for i in rows:
            full_value += i[0]
        return full_value

def quali_resi(username, cur):
    cur.execute(f"SELECT Username, Qualified_Residual, Residual_Percentage FROM amba_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:
        return rows

def all_ambabala(cur):
    cur.execute(f"SELECT Ambassador_Balance from balance_info")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:
        tot = 0
        for i in rows:
            tot += i[0]
        return tot

def all_intebala(cur):
    cur.execute(f"SELECT Interest_balance from balance_info")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:
        tot = 0
        for i in rows:
            tot += i[0]
        return tot

def all_inve(cur):
    cur.execute(f"SELECT Promotional_Holding, Standard_Holding from investment_holding")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:
        tot = 0
        for i in rows:
            tot += i[0]+i[1]
        return tot

def all_payout(cur):
    cur.execute(f"SELECT Value from payout_transactions")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:
        tot = 0
        for i in rows:
            tot += i[0]
        return tot

def pen_withdraw(cur):
    cur.execute(f"SELECT Withdraw_Amount from withdraws WHERE Current_Status = 'Pending'")
    rows = cur.fetchall()
    if rows == []:
        rows = 0
        return rows
    else:
        tot = 0
        for i in rows:
            tot += i[0]
        return tot

def help_text(cur):
    cur.execute(f"SELECT Details from plain_text WHERE Name = 'help'")
    rows = cur.fetchall()
    return rows[0][0]

def all_products(cur):
    cur.execute(f"SELECT Investment_Name, Time_Sold from investment_details")
    rows = cur.fetchall()
    return rows

def payout_alltrans(cur):
    cur.execute(f"SELECT Username, Investment_Type, Value FROM payout_transactions")
    rows = cur.fetchall()
    if rows == []:
        rows = 'Nothing'
        return rows
    else:
        return rows

def pro_all(cur):
    cur.execute(f"SELECT Investment_Name from investment_details")
    rows = cur.fetchall()
    full_list = []
    for i in rows:
        full_list.append(i[0])
    return full_list

def type_all(cur):
    cur.execute(f"SELECT Investment_Type from investment_details")
    rows = cur.fetchall()
    full_list = []
    for i in rows:
        if i[0] in full_list:
            pass
        else:
            full_list.append(i[0])
    return full_list

def payout_time(cur):
    cur.execute(f"SELECT Investment_Type from investment_description WHERE Payout_Time = '0'")
    rows = cur.fetchall()
    full_list = []
    for i in rows:
        if i[0] in full_list:
            pass
        else:
            full_list.append(i[0])
    return full_list

def payout_next(product, cur):
    cur.execute(f"SELECT Next_Payout from investment_description WHERE Investment_Type = '{product}'")
    rows = cur.fetchall()
    return rows[0][0]

def next_payout(product, cur):
    cur.execute(f"SELECT Payout_Time from investment_description WHERE Investment_Type = '{product}'")
    rows = cur.fetchall()
    return rows[0][0]

def manager_username(id_number, cur):
    cur.execute(f"SELECT Ambassador_Code from managers WHERE ID_Number = '{id_number}'")
    rows = cur.fetchall()
    return rows[0][0]

def all_pass(cur):
    cur.execute(f"SELECT Password from user_info")
    rows = cur.fetchall()
    unique = []
    for i in rows:
        unique.append(i[0])
    return unique

def all_amba(cur):
    cur.execute(f"SELECT Ambassador_Code from amba_info")
    rows = cur.fetchall()
    unique = []
    for i in rows:
        unique.append(i[0])
    return unique

def all_id(cur):
    cur.execute(f"SELECT ID_Number from managers")
    rows = cur.fetchall()
    unique = []
    for i in rows:
        unique.append(i[0])
    return unique

def all_manapass(cur):
    cur.execute(f"SELECT Password from managers")
    rows = cur.fetchall()
    unique = []
    for i in rows:
        unique.append(i[0])
    return unique

def manager_access(username, cur):
    cur.execute(f"SELECT Manager from user_info WHERE Username = '{username}'")
    rows = cur.fetchall()
    return rows[0][0]

def manage(cur):
    cur.execute(f"SELECT Username from user_info WHERE Manager = 'YES'")
    rows = cur.fetchall()
    unique = []
    for i in rows:
        unique.append(i[0])
    return unique

def amba_serial(cur):
    cur.execute(f"SELECT Serial from ambassador_transaction")
    rows = cur.fetchall()
    max_num = []
    for i in rows:
        max_num.append(i[0])
    return max(max_num)+1

def payout_serial(cur):
    cur.execute(f"SELECT Serial from Payout_Transaction")
    rows = cur.fetchall()
    max_num = []
    for i in rows:
        max_num.append(i[0])
    return max(max_num)+1

def invest_serial(cur):
    cur.execute(f"SELECT Serial from investment_transactions")
    rows = cur.fetchall()
    max_num = []
    for i in rows:
        max_num.append(i[0])
    return max(max_num)+1

def depo_serial(cur):
    cur.execute(f"SELECT Serial from deposits")
    rows = cur.fetchall()
    max_num = []
    for i in rows:
        max_num.append(i[0])
    return max(max_num)+1

def depo_trans(cur):
    cur.execute(f"SELECT Transaction_Hash from deposits")
    rows = cur.fetchall()
    unique_list = []
    for a in rows:
        if a[0] in unique_list:
            pass
        else:
            unique_list.append(a[0])
    return unique_list

def depo_text(cur):
    cur.execute(f"SELECT Details from plain_text WHERE Name = 'deposit'")
    rows = cur.fetchall()
    return rows[0][0]

def secret_text(cur):
    cur.execute(f"SELECT Details from plain_text WHERE Name = 'mass'")
    rows = cur.fetchall()
    return rows[0][0]

def tele_id(cur):
    cur.execute(f"SELECT Telegram_ID from user_info")
    rows = cur.fetchall()
    unique_list = []
    for a in rows:
        if a[0] in unique_list:
            pass
        elif str(a[0]).isnumeric() == False:
            pass
        else:
            unique_list.append(a[0])
    return unique_list

def mainte_on(cur):
    cur.execute(f"SELECT Details from plain_text WHERE Name = 'maintenance on'")
    rows = cur.fetchall()
    return rows[0][0]

def mainte_off(cur):
    cur.execute(f"SELECT Details from plain_text WHERE Name = 'maintenance off'")
    rows = cur.fetchall()
    return rows[0][0]
