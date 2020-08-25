import mysql.connector
def balance_info(username, balance, cur):
    sql = f"UPDATE balance_info SET Investment_Balance = '{balance}' WHERE Username = '{username}'"
    cur.execute(sql)

def balance_amba(username, balance, cur):
    sql = f"UPDATE balance_info SET Ambassador_Balance = '{balance}' WHERE Username = '{username}'"
    cur.execute(sql)

def balance_interest(username, balance, cur):
    sql = f"UPDATE balance_info SET Interest_Balance = '{balance}' WHERE Username = '{username}'"
    cur.execute(sql)

def amba_info(Ambassador_Code, referred_number, cur):
    sql = f"UPDATE amba_info SET Referred_Users = {referred_number} WHERE Ambassador_Code = '{Ambassador_Code}'"
    cur.execute(sql)

def withdraws(serial, btc_hash, cur):
    sql = f"UPDATE withdraws SET Transaction_Hash = '{btc_hash}' WHERE Serial = {serial}"
    cur.execute(sql)
    sql = f"UPDATE withdraws SET Current_Status = 'CONFIRMED' WHERE Serial = {serial}"
    cur.execute(sql)

def password(username, new_pass, cur):
    sql = f"UPDATE user_info SET Password = '{new_pass}' WHERE Username = '{username}'"
    cur.execute(sql)

def invement_sold(product, sold, cur):
    sql = f"UPDATE investment_details SET Time_Sold = '{sold}' WHERE Investment_Name = '{product}'"
    cur.execute(sql)

def invest_promo(username, balance, holding, cur):
    sql = f"UPDATE investment_holding SET Promotional_Holding = '{balance}' WHERE Username = '{username}'"
    cur.execute(sql)
    sql = f"UPDATE investment_holding SET Holdings = '{holding}' WHERE Username = '{username}'"
    cur.execute(sql)

def invest_stand(username, balance, holding, cur):
    sql = f"UPDATE investment_holding SET Standard_Holding = '{balance}' WHERE Username = '{username}'"
    cur.execute(sql)
    sql = f"UPDATE investment_holding SET Holdings = '{holding}' WHERE Username = '{username}'"
    cur.execute(sql)

def bonus_given(username, cur):
    sql = f"UPDATE amba_info SET Bonus_Given = 'True' WHERE Username = '{username}'"
    cur.execute(sql)

def tree_investment(amba, balance, cur):
    sql = f"UPDATE amba_info SET Tree_Investment = '{balance}' WHERE Ambassador_Code = '{amba}'"
    cur.execute(sql)

def manager(username, manager, cur):
    sql = f"UPDATE amba_info SET Manager = '{manager}' WHERE Username = '{username}'"
    cur.execute(sql)

def qualified_milestone(username, amount, cur):
    sql = f"UPDATE amba_info SET Qualified_Milestone = '{amount}' WHERE Username = '{username}'"
    cur.execute(sql)

def qualified_residual(username, amount, cur):
    sql = f"UPDATE amba_info SET Qualified_Residual = '{amount}' WHERE Username = '{username}'"
    cur.execute(sql)

def enrolled(username, cur):
    sql = f"UPDATE investment_holding SET Enrolled = 'True' WHERE Username = '{username}'"
    cur.execute(sql)

def tier(username, tier, cur):
    sql = f"UPDATE milestone_bonus SET {tier} = 'True' WHERE Username = '{username}'"
    cur.execute(sql)

def payout_pending(product, cur):
    sql = f"UPDATE investment_description SET Payout_Pending = 'False' WHERE Investment_Type = '{product}'"
    cur.execute(sql)

def tree_percentage(username, rate, cur):
    sql = f"UPDATE amba_info SET Residual_Percentage = '{rate}' WHERE Username = '{username}'"
    cur.execute(sql)

def payout_time(product, time, cur):
    sql = f"UPDATE investment_description SET Payout_time = '{time}' WHERE Investment_Type = '{product}'"
    cur.execute(sql)

def manager_access(username, cur):
    sql = f"UPDATE user_info SET Manager = 'YES' WHERE Username = '{username}'"
    cur.execute(sql)
