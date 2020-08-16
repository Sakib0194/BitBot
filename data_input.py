import sqlite3, datetime, time
from sqlite3 import Error

def user_info(Telegram_ID, First_Name, Username, Password, Ambassador_Code, Amba_Code_Used, Joining_Date, Telegram_Username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f''' INSERT INTO user_info(Telegram_ID, First_Name, Username, Password, Ambassador_Code, Amba_Code_Used, Joining_Date, Telegram_Username)
            VALUES(?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        project = (Telegram_ID, First_Name, Username, Password, Ambassador_Code, Amba_Code_Used, Joining_Date, Telegram_Username)
        cur.execute(sql, project)

#user_info('1211908888', 'DAM SUPPORT', 'Vito', 'TM1X46BAAD', 'LVXD4A8', 'JRIU4BW', str(datetime.datetime.fromtimestamp(time.time())), 'DAMSUPPORT')

def balance_info(Telegram_ID, First_Name, Username, Investment_Balance, Ambassador_Balance, Interest_Balance):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f''' INSERT INTO balance_info(Telegram_ID, First_Name, Username, Investment_Balance, Ambassador_Balance, Interest_Balance)
            VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        project = (Telegram_ID, First_Name, Username, Investment_Balance, Ambassador_Balance, Interest_Balance)
        cur.execute(sql, project)

#balance_info('1211908888', 'DAM SUPPORT', 'Vito', 0, 0, 0)

def amba_info(Telegram_ID, First_Name, Username, Ambassador_Code, Ambassador_Code_Used, Referred_Users):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f''' INSERT INTO amba_info(Telegram_ID, First_Name, Username, Ambassador_Code, Ambassador_Code_Used, Referred_Users, Bonus_Given, Tree_Investment)
            VALUES(?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        project = (Telegram_ID, First_Name, Username, Ambassador_Code, Ambassador_Code_Used, Referred_Users, 'False', 0)
        cur.execute(sql, project)

#amba_info('1211908888', 'DAM SUPPORT', 'Vito53', 'LVXD4A84165', 'JRIU4BW541', 0)

def deposits(Telegram_ID, First_Name, Username, Time, Transaction_Hash, Deposited_Amount_bits, Current_Status):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f''' INSERT INTO deposits(Telegram_ID, First_Name, Username, Time, Transaction_Hash, Deposited_Amount, Current_Status)
            VALUES(?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        project = (Telegram_ID, First_Name, Username, Time, Transaction_Hash, Deposited_Amount_bits, Current_Status)
        cur.execute(sql, project)

#deposits('468930122', 'Sakib', 'Sakib', '2020-07-29 14:33', '16c71623591ce4b3d531127736dd0b312f9131e64b81a0b02a02f7bcc91bb4cb', 100000, 'Success')

def withdraws(Telegram_ID, First_Name, Username, Time, Withdrawal_Address, Transaction_Hash, Withdraw_Amount_bits, Current_Status, Serial):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f''' INSERT INTO withdraws(Telegram_ID, First_Name, Username, Time, Withdrawal_Address, Transaction_Hash, Withdraw_Amount, Current_Status, Serial)
            VALUES(?,?,?,?,?,?,?,?,?) '''
        cur = conn.cursor()
        project = (Telegram_ID, First_Name, Username, Time, Withdrawal_Address, Transaction_Hash, Withdraw_Amount_bits, Current_Status, Serial)
        cur.execute(sql, project)

#withdraws('468930122', 'Sakib', 'Sakib', '2020-07-29 14:33', 'bc1q3r8xg0g2s7mt33n2yqxmmxvjslx2yuhge6q9r5', 'None', 100000, 'Pending', 1)

def managers(Telegram_ID, First_Name, Joining_Date, ID_Number, Password, Special_Access, Username, Ambassador_Code):
        database = r"/mnt/sda1/database_test/dam_bot.db"
        conn = sqlite3.connect(database)
        with conn:
            sql = f'''INSERT INTO managers(Telegram_ID, First_Name, Joining_Date, ID_Number, Password, Special_Access, Username, Ambassador_Code)
                VALUES(?,?,?,?,?,?,?,?)'''
            cur = conn.cursor()
            project = (Telegram_ID, First_Name, Joining_Date, ID_Number, Password, Special_Access, Username, Ambassador_Code)
            cur.execute(sql, project)
    
#managers('1211908888', 'DAM SUPPORT', '2020-07-29 14:33', 'TM1X46BAAD', 'LVXD4A8', 'YES', 'Vito', 'LVXD4A8')

def investment_types(Investment_Category, Investment_Type, Investment_Name, Payout_Cycle, Cost, Added_By, Time_Sold):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f'''INSERT INTO investment_details(Investment_Category, Investment_Type, Investment_Name, Payout_Cycle, Cost, Added_By, Time_Sold)
            VALUES(?,?,?,?,?,?,?)'''
        cur = conn.cursor()
        project = (Investment_Category, Investment_Type, Investment_Name, Payout_Cycle, Cost, Added_By, Time_Sold)
        cur.execute(sql, project)
#investment_types('Standard Investment','Mutual Investment', 'MFUND', 'TO BE DETERMINED', 10000, 'Sakib', 0)

def investment_holding(username, standard, promotional, holdings):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f'''INSERT INTO investment_holding(Username, Promotional_Holding, Standard_Holding, Holdings)
            VALUES(?,?,?,?)'''
        cur = conn.cursor()
        project = (username, promotional, standard, holdings)
        cur.execute(sql, project)

#investment_holding('Sakib019', 1900000, 1900000, 'PB5-1 PB10-1 PB25-1 PB50-1 PB100-1 B5-1 B10-1 B25-1 B50-1 B100-1')

def investment_description(Investment_Type, Description, Payout_Rate):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f'''INSERT INTO investment_description(Investment_Type, Description, Payout_Rate)
            VALUES(?,?,?)'''
        cur = conn.cursor()
        project = (Investment_Type, Description, Payout_Rate)
        cur.execute(sql, project)

#investment_description('Promotional Investment', 'Promotional Interest rate of 18\\.100% Monthly\nPayouts 1st/15th  of every Month\n\nPrice of Products\n\nPB5 \\- 50,000 bits\nPB10 \\- 100,000 bits\nPB25 \\- 250,000 bits\nPB50 \\- 500,000 bits\nPB100 \\- 1,000,000 bits\n\n_This product is available only for a limited time\\._', 18.1)

def investment_transactions(Username, Time, Type, Prodcuct_Name, Transaction_Value):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f'''INSERT INTO investment_transactions(Username, Time, Type, Prodcuct_Name, Transaction_Value)
            VALUES(?,?,?,?,?)'''
        cur = conn.cursor()
        project = (Username, Time, Type, Prodcuct_Name, Transaction_Value)
        cur.execute(sql, project)

def milestone_bonus(Username):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f'''INSERT INTO Milestone_Bonus(Username,Tier_1)
            VALUES(?,?)'''
        cur = conn.cursor()
        project = (Username, 'False')
        cur.execute(sql, project)
#milestone_bonus('Vito53')

def ambassador_transactions(Username, Type, Amount, Description):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f'''INSERT INTO Ambassador_Transactions(Username, Type, Amount, Description)
            VALUES(?,?,?,?)'''
        cur = conn.cursor()
        project = (Username, Type, Amount, Description)
        cur.execute(sql, project)

def feedback(Username, Time, Description):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f'''INSERT INTO Feedbacks(Username, Time, Description)
            VALUES(?,?,?)'''
        cur = conn.cursor()
        project = (Username, Time, Description)
        cur.execute(sql, project)

def payout_transaction(Username, Investment_Type, Value):
    database = r"/mnt/sda1/database_test/dam_bot.db"
    conn = sqlite3.connect(database)
    with conn:
        sql = f'''INSERT INTO payout_transactions(Username, Investment_Type, Value)
            VALUES(?,?,?)'''
        cur = conn.cursor()
        project = (Username, Investment_Type, Value)
        cur.execute(sql, project)
