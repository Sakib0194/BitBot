#!/usr/bin/env python3

def user_info(Telegram_ID, First_Name, Username, Password, Ambassador_Code, Amba_Code_Used, Joining_Date, Telegram_Username, cur):
    sql = f''' INSERT INTO user_info(Telegram_ID, First_Name, Username, Password, Ambassador_Code, Amba_Code_Used, Joining_Date, Telegram_Username)
        VALUES('{Telegram_ID}', '{First_Name}', '{Username}', '{Password}', '{Ambassador_Code}', '{Amba_Code_Used}', '{Joining_Date}', '{Telegram_Username}') '''
    cur.execute(sql)

#user_info('1211908888', 'DAM SUPPORT', 'Vito', 'TM1X46BAAD', 'LVXD4A8', 'JRIU4BW', str(datetime.datetime.fromtimestamp(time.time())), 'DAMSUPPORT')

def balance_info(Telegram_ID, First_Name, Username, Investment_Balance, Ambassador_Balance, Interest_Balance, cur):
    sql = f''' INSERT INTO balance_info(Telegram_ID, First_Name, Username, Investment_Balance, Ambassador_Balance, Interest_Balance)
        VALUES('{Telegram_ID}', '{First_Name}', '{Username}', '{Investment_Balance}', '{Ambassador_Balance}', '{Interest_Balance}') '''
    cur.execute(sql)

#balance_info('1211908888', 'DAM SUPPORT', 'Vito', 0, 0, 0)

def amba_info(Telegram_ID, First_Name, Username, Ambassador_Code, Ambassador_Code_Used, Referred_Users, cur):
    sql = f''' INSERT INTO amba_info(Telegram_ID, First_Name, Username, Ambassador_Code, Ambassador_Code_Used, Referred_Users, Bonus_Given, Tree_Investment)
        VALUES('{Telegram_ID}', '{First_Name}', '{Username}', '{Ambassador_Code}', '{Ambassador_Code_Used}', {Referred_Users}, 'False', 0) '''
    cur.execute(sql)

#amba_info('1211908888', 'DAM SUPPORT', 'Vito53', 'LVXD4A84165', 'JRIU4BW541', 0)

def deposits(Telegram_ID, First_Name, Username, Time, Transaction_Hash, Deposited_Amount_bits, Current_Status, serial, cur):
    sql = f''' INSERT INTO deposits(Telegram_ID, First_Name, Username, Time, Transaction_Hash, Deposited_Amount, Current_Status, Serial)
        VALUES('{Telegram_ID}', '{First_Name}', '{Username}', '{Time}', '{Transaction_Hash}', {Deposited_Amount_bits}, '{Current_Status}', {serial}) '''
    cur.execute(sql)

#deposits('468930122', 'Sakib', 'Sakib', '2020-07-29 14:33', '16c71623591ce4b3d531127736dd0b312f9131e64b81a0b02a02f7bcc91bb4cb', 100000, 'Success', 3, cur)

def withdraws(Telegram_ID, First_Name, Username, Time, Withdrawal_Address, Transaction_Hash, Withdraw_Amount_bits, Current_Status, Serial, cur):
    sql = f''' INSERT INTO withdraws(Telegram_ID, First_Name, Username, Time, Withdrawal_Address, Transaction_Hash, Withdraw_Amount, Current_Status, Serial)
        VALUES('{Telegram_ID}', '{First_Name}', '{Username}', '{Time}', '{Withdrawal_Address}', '{Transaction_Hash}', {Withdraw_Amount_bits}, '{Current_Status}', {Serial}) '''
    cur.execute(sql)

#withdraws('468930122', 'Sakib', 'Sakib', '2020-07-29 14:33', 'bc1q3r8xg0g2s7mt33n2yqxmmxvjslx2yuhge6q9r5', 'None', 100000, 'Pending', 1)

def managers(Telegram_ID, First_Name, Joining_Date, number, Password, Special_Access, Username, Ambassador_Code, cur):
    sql = f'''INSERT INTO managers(Telegram_ID, First_Name, Joining_Date, ID_Number, Password, Special_Access, Username, Ambassador_Code)
        VALUES('{Telegram_ID}', '{First_Name}', '{Joining_Date}', '{number}', '{Password}', '{Special_Access}', '{Username}', '{Ambassador_Code}')'''
    cur.execute(sql)
    
#managers('1211908888', 'DAM SUPPORT', '2020-07-29 14:33', 'TM1X46BAAD', 'LVXD4A8', 'YES', 'Vito', 'LVXD4A8')

def investment_types(Investment_Category, Investment_Type, Investment_Name, Payout_Rate, Cost, Time_Sold, cur):
    sql = f'''INSERT INTO investment_details(Investment_Category, Investment_Type, Investment_Name, Payout_Rate, Cost, Time_Sold)
        VALUES('{Investment_Category}', '{Investment_Type}', '{Investment_Name}', {Payout_Rate}, {Cost}, {Time_Sold})'''
    cur.execute(sql)
#investment_types('Standard Investment','Mutual Investment', 'MFUND', 'TO BE DETERMINED', 10000, 0)

def investment_holding(username, standard, promotional, holdings, cur):
    sql = f'''INSERT INTO investment_holding(Username, Promotional_Holding, Standard_Holding, Holdings)
        VALUES('{username}', {promotional}, {standard}, '{holdings}')'''
    cur.execute(sql)

#investment_holding('Sakib019', 1900000, 1900000, 'PB5-1 PB10-1 PB25-1 PB50-1 PB100-1 B5-1 B10-1 B25-1 B50-1 B100-1')

def investment_description(Investment_Type, Description, Payout_Rate, cur):
    sql = f'''INSERT INTO investment_description(Investment_Type, Description, Payout_Rate)
        VALUES('{Investment_Type}', '{Description}', {Payout_Rate})'''
    cur.execute(sql)

#investment_description('Promotional Investment', 'Promotional Interest rate of 18\\.100% Monthly\nPayouts 1st/15th  of every Month\n\nPrice of Products\n\nPB5 \\- 50,000 bits\nPB10 \\- 100,000 bits\nPB25 \\- 250,000 bits\nPB50 \\- 500,000 bits\nPB100 \\- 1,000,000 bits\n\n_This product is available only for a limited time\\._', 18.1)

def investment_transactions(Username, Time, Type, Prodcuct_Name, Transaction_Value, serial, cur):
    sql = f'''INSERT INTO investment_transactions(Username, Time, Type, Product_Name, Transaction_Value, serial)
        VALUES('{Username}', '{Time}', '{Type}', '{Prodcuct_Name}', '{Transaction_Value}', {serial})'''
    cur.execute(sql)

def milestone_bonus(Username, cur):
    sql = f'''INSERT INTO milestone_bonus(Username)
        VALUES('{Username}')'''
    cur.execute(sql)
#milestone_bonus('Vito53')

def ambassador_transactions(Username, Type, Amount, Description, serial, cur):
    sql = f'''INSERT INTO Ambassador_Transactions(Username, Type, Amount, Description, Serial)
        VALUES('{Username}', '{Type}', {Amount}, '{Description}', {serial})'''
    cur.execute(sql)

def feedback(Username, Time, Description, cur):
    sql = f'''INSERT INTO Feedbacks(Username, Time, Description)
        VALUES('{Username}', '{Time}', '{Description}')'''
    cur.execute(sql)

def payout_transaction(Username, Investment_Type, Value, serial, cur):
    sql = f'''INSERT INTO payout_transactions(Username, Investment_Type, Value, Serial)
        VALUES('{Username}', '{Investment_Type}', {Value}, {serial})'''
    cur.execute(sql)

def plain_text(Name, Details, cur):
    sql = f'''INSERT INTO plain_text(Name, Details)
        VALUES('{Name}', '{Details}')'''
    cur.execute(sql)

#plain_text('help', '''This is the official Telegram Bot of BitBot, a Digital Asset Management Service\\.\nThis section will help you get familiar with the Bot\\.\n\nStart the bot by typing /start\\. Then, you have the option to Login or Register\\. In order to proceed with registration, you must have an access code or ambassador code\\. If you do not have a code, contact us here \\@BitBotTeam to get one\\.\n\nWhen you choose to Register, you will have to provide your code, press Register \\=\\> Accept our Terms of Service \\=\\> Provide your code\\. Follow the steps to complete your registration\\. Choose a unique username and the bot will provide you a password and an ambassador code\\. Follow steps and save your personal credentials, once completed you will be redirected to the “Main Menu”\\.\n\nThe Main Menu is composed of 5 buttons which will bring you to 5 different sections\nBalance is counted as bits\n1 million bits = 1 BTC or\n1,000,000 bits = 1 BTC\\.\n\n*My BitBot Balance*\nMy BitBot Balance \\- Your Total Balance\nAvailable Balance \\- Balance Available for Purchase or Withdrawal\nMake a Deposit \\- To Deposit Funds\nWithdrawal \\- To Request Withdrawal\nTransaction History \\- Your Deposit and Withdrawal History\n\n*My Portfolio*\nMy Portfolio \\- Your Total Investment Value\nMy Investments \\- Your Current Investment Product Holdings\nMy Earnings \\- Your Earnings from Investment Products\nBuy \\- To Purchase an Investment Product\nSell \\- To Sell an Investment Product.\nSelling Investments has a fee of 1000 bits\nInvestments History \\- Your Investment Buy or Sell History\n\n*My Ambassador Profile*\nMy Ambassador Volume \\- Total\nInvestment Holdings of your referrals\nMy Ambassador Earnings \\- Details of Referral Bonus, Earnings for Reaching Milestone or Residual Income\nAmbassador Compensation Plan \\- Detailed Plans and Rewards for Referrals\n\n*More*\nToS \\- Terms of Service\nFAQ \\- Frequently Asked Questions, Find answers faster\nAbout Us \\- Details about our company\nReport Bug \\- To Report any Bug in the bot or Feedback\nHelp \\- How to Contact us''')
