#!/usr/bin/env python3
import requests, json, random, string, time, datetime, requests, mysql.connector
import data_input, update_data, grab_data_two, tree_tracking

class BoilerPlate:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=0, timeout=10000):         #FOR GETTING UPDATES
        function = 'getUpdates'
        fieldss = {'timeout' : timeout, 'offset': offset}
        send = requests.get(self.api_url + function, fieldss)
        result_json = send.json()['result']
        return result_json

    def send_message(self, chat_id, text, disable_web_page_preview=False):                  #FOR SENDING NORMAL MESSAGE
        fieldss = {'chat_id': chat_id, 'text': text, 'parse_mode': 'MarkdownV2', 'disable_web_page_preview':disable_web_page_preview}
        function = 'sendMessage'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send
    def send_message_two(self, chat_id, text, reply_markup, one_time_keyboard=False, resize_keyboard=True, disable_web_page_preview=True):         #FOR SENDING MESSAGE WITH KEYBOARD INCLUDED
        reply_markup = json.dumps({'keyboard': reply_markup, 'one_time_keyboard': one_time_keyboard, 'resize_keyboard': resize_keyboard, 'disable_web_page_preview':disable_web_page_preview})
        fieldss = {'chat_id': chat_id, 'text': text, 'parse_mode': 'MarkdownV2', 'reply_markup': reply_markup}
        function = 'sendMessage'
        send = requests.post(self.api_url + function, fieldss).json()
        return send

    def send_message_three(self, chat_id, text, remove_keyboard):               #FOR SENDING MESSAGES AND TO REMOVE KEYBOARD
        reply_markup = json.dumps({'remove_keyboard': remove_keyboard})
        fieldss = {'chat_id': chat_id, 'text': text, 'parse_mode': 'MarkdownV2', 'reply_markup': reply_markup}
        function = 'sendMessage'
        send = requests.post(self.api_url + function, fieldss).json()
        return send   

    def send_message_four(self, chat_id, text, reply_markup, disable_web_page_preview=True):               #FOR SENDING MESSAGES WITH INLINE KEYBOARD
        reply_markup = json.dumps({'inline_keyboard': reply_markup})
        fieldss = {'chat_id': chat_id, 'text': text, 'parse_mode': 'MarkdownV2', 'reply_markup': reply_markup, 'disable_web_page_preview':disable_web_page_preview}
        function = 'sendMessage'
        send = requests.post(self.api_url + function, fieldss).json()
        return send 

    def send_photo(self, chat_id, photo):
        fieldss = {'chat_id':chat_id, 'photo':photo}
        function = 'sendPhoto'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send 
    
    def InLineAnswer(self, inline_query_id, results):                   #FOR MANAGING INLINE REPLIES
        fieldss = {"inline_query_id": inline_query_id, "results" : results}
        function = 'answerInlineQuery'
        send = requests.post(self.api_url + function, fieldss)
        return send   

    def deleteWebhook(self):                #FOR DELETING WEBHOOK
        function = 'deleteWebhook'
        send = requests.post(self.api_url + function)
        return send

    def delete_message(self, group_id, message_id):         #FOR DELETING MESSAGES FROM GROUP
        fieldss = {'chat_id': group_id, 'message_id': message_id}
        function = 'deleteMessage'
        send = requests.post(self.api_url + function, fieldss)
        return send

    def get_admins(self, chat_id):              #ADMIN LIST IN A GROUP
        function = 'getChatAdministrators'
        fieldss = {'chat_id':chat_id}
        send = requests.get(self.api_url + function, fieldss)
        return send.json()['result']

    def edit_message (self, chat_id, message_id, text):
        fieldss = {'chat_id': chat_id, 'message_id': message_id, 'text': text, 'parse_mode':'MarkdownV2'}
        function = 'editMessageText'
        send = requests.post(self.api_url + function, fieldss)
        return send

    def edit_message_two (self, chat_id, message_id, text, reply_markup, disable_web_page_preview=True):
        reply_markup = json.dumps({'inline_keyboard': reply_markup})
        fieldss = {'chat_id': chat_id, 'message_id': message_id, 'text': text, 'parse_mode':'MarkdownV2', 'reply_markup':reply_markup, 'disable_web_page_preview':disable_web_page_preview}
        function = 'editMessageText'
        send = requests.post(self.api_url + function, fieldss)
        #print(send.json())
        return send

def generate_pass():
    everything = string.ascii_uppercase
    for i in range(9):
        everything += str(i)
    randomized = ''.join(random.sample(everything,len(everything)))
    password = ''
    ambassador = ''
    for i in range(10):
        password += random.choice(randomized)
    for i in range(7):
        ambassador += random.choice(randomized)
    both_codes = [password, ambassador]
    return both_codes

def time_splitter(time):
    b = time.split(' ')
    c = b[1][0:5]
    full_time = f'{b[0]} {c}'
    return full_time



#token = '1097474969:AAFjro39pNaKqdrWy6bZIppX1ZzbM_B6RyY'
token = '1259681061:AAHRaJrnAYzEkmhiXlw9Xw1d3l6-85MPNX8'
offset = 0

conn = mysql.connector.connect(host='62.77.159.42',user='sakib3',database='bitbot',password='@&G6hdM@EZJKQu010au*jpIjs7EsB', autocommit=True)
cur = conn.cursor()


temp_acc = {} #to update refer number
submitting = [] #While submitting pass
temp_pass = {} #While submitting pass

logged_in = [] #after logged in
report_bug = []

loggin_in = [] #login
password_in = [] #login

sumamry_pass = []#Summary

registering = [] #register
user_regis = [] #register
register_id = {}

saved_username = {} #For saving username
saved_amba = {} #for saving amba code

withdraw = []# when withdrawing
temp_with = {}# when withdrawing

pro_name = {} #product tracking
pro_price = {} #product tracking
update_success = [] #when updating database
sell_invest = [] #when selling investment
buy_invest = [] #when buying investment

mainte_on = False
mainte_message = ''


def investment_num(investment):
    a = investment
    d = "%.2f" % a
    e = "{:,}".format(float(d))
    return e


bot = BoilerPlate(token)

def starter():
    global offset, conn, cur
    while True:
        if conn.is_connected() == True:
            pass
        else:
            conn = mysql.connector.connect(host='62.77.159.42',user='sakib3',database='bitbot',password='@&G6hdM@EZJKQu010au*jpIjs7EsB', autocommit=True)
            cur = conn.cursor()
        all_updates = bot.get_updates(offset)
        for current_updates in all_updates:
            #print(current_updates)
            update_id = current_updates['update_id']
            #bot.get_updates(offset = update_id+1)
            try:
                if 'callback_query' in current_updates:
                    #print('inline keyboard detected')
                    sender_id = current_updates['callback_query']['from']['id']
                    group_id = current_updates['callback_query']['message']['chat']['id']
                    message_id = current_updates['callback_query']['message']['message_id']
                    callback_data = current_updates['callback_query']['data']
                    bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, 0, cur, callback_data=callback_data, callback=True)
                else:
                    group_id = current_updates['message']['chat']['id']
                    sender_id = current_updates['message']['from']['id']
                    message_id = current_updates['message']['message_id']
                    dict_checker = []
                    for keys in current_updates.get('message'):
                        dict_checker.append(keys)
                    if sender_id == group_id:
                        bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, dict_checker, cur)
            except:
                bot.get_updates(offset = update_id+1)

def bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, dict_checker, cur, callback_data=0, callback=False):
    global mainte_on, mainte_message
    try:
        if mainte_on == True:
            if callback == False:
                text = current_updates['message']['text']
                if grab_data_two.mainte_off(cur) in text:
                    bot.send_message(sender_id, 'Maintenance Mode Turned Off')
                    mainte_on = False
                    mainte_message = ''
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.send_message(sender_id, f'Maintenance is underway\\. Please check back later\n\n{mainte_message}')
                    bot.get_updates(offset = update_id+1)
            else:
                bot.send_message(sender_id, f'Maintenance is underway\\. Please check back later\n\n{mainte_message}')
                bot.get_updates(offset = update_id+1)
        if callback == True:
            #print(message_id)
            print(callback_data)
            if sender_id not in logged_in:
                if callback_data == 'Register' or callback_data == 'Accept' or callback_data == 'Login' or callback_data == 'Reject':
                    pass
                else:
                    bot.send_message_four(sender_id, '👤 *BitBot Client Authorization*\n\nSend /help to get more details', [[{'text':'🔑 Log In', 'callback_data': 'Login'}, {'text':'®️ Register', 'callback_data':'Register'}]])
                    bot.get_updates(offset = update_id+1)

            if callback_data == 'None':
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Login':
                bot.edit_message(group_id, message_id, 'Please enter your *BitBot Username*')
                if sender_id in registering:
                    registering.remove(sender_id)
                if sender_id in user_regis:
                    user_regis.remove(sender_id)
                if sender_id not in loggin_in:
                    loggin_in.append(sender_id)
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Register':
                if str(sender_id) in grab_data_two.user_tele(str(sender_id), cur)[0]:
                    bot.edit_message_two(group_id, message_id, 'You already have an account\\. Please Log In using your details', [[{'text':'Login', 'callback_data': 'Login'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.edit_message_two(group_id, message_id, 'By tapping "I Accept", I confirm that I am above the age of majority at my local jurisdiction\\. I agree to the [Terms of Service and the Privacy Policy](https://t.me/ChannelBitBot/11)\\.', [[{'text':'☑️ I Accept', 'callback_data':'Accept'}, {'text':'✖️ I Reject', 'callback_data':'Reject'}]])
                    if sender_id in loggin_in:
                        loggin_in.remove(sender_id)
                    if sender_id in password_in:
                        password_in.remove(sender_id)
                    if sender_id not in registering:
                        registering.append(sender_id)
                    bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Accept':
                bot.edit_message(group_id, message_id, 'Please provide your access code')
                if sender_id in loggin_in:
                    loggin_in.remove(sender_id)
                if sender_id not in registering:
                    registering.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Reject':
                bot.edit_message_two(group_id, message_id, 'You Rejected our Terms of Service and the Privacy Policy', [[{'text':'Login', 'callback_data': 'Login'}, {'text':'Register', 'callback_data':'Register'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Main Balance' and sender_id in logged_in:
                promo = grab_data_two.hold_promo(saved_username[sender_id], cur)
                stand = grab_data_two.hold_stand(saved_username[sender_id], cur)
                tol_bal = int(grab_data_two.balance_balance(saved_username[sender_id], cur))
                total = int(promo) + int(stand) + int(tol_bal)
                bot.edit_message_two(group_id, message_id, f'👤 *My BitBot Balance \\- {saved_username[sender_id]}*', [[{'text': f'💰 My BitBot Balance: {investment_num(total)} bits', 'callback_data': 'None'}], 
                                                                            [{'text':f'💵 Available Balance: {investment_num(tol_bal)} bits','callback_data':'None'}],
                                                                            [{'text':'⬇️ Make a Deposit', 'callback_data': 'Make Deposit'}], 
                                                                            [{'text':'↗️ Withdrawal', 'callback_data':'Request Withdrawal'}], 
                                                                            [{'text':'📒 Transaction History','callback_data':'History'}],
                                                                            [{'text':'↩️ Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)


            elif callback_data == 'Make Deposit' and sender_id in logged_in:
                address = grab_data_two.depo_text(cur)
                bot.edit_message(group_id, message_id, 'Send BTC/Bitcoin to the following address to Deposit in your account')
                bot.send_message(sender_id, address)
                bot.send_message_four(sender_id, 'Send the Transaction ID/Hash here after the transaction is initiated', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Request Withdrawal' and sender_id in logged_in:
                bot.edit_message(group_id,message_id, f'Your Current Balance is {investment_num(grab_data_two.balance_balance(saved_username[sender_id], cur))} bits')
                bot.send_message(sender_id, 'Enter the amount of bits to withdraw in the following manner\n\nexample message\n11540 bits\n5687 bits\n55780 bits')
                if sender_id not in withdraw:
                    withdraw.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'History' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, f'*📒 Transaction History \\- {saved_username[sender_id]}*', [[{'text':'Deposits', 'callback_data':'Deposit History'}, {'text':'Withdraws', 'callback_data':'Withdraw History'}],
                                                                                                                            [{'text':'↩️ Back', 'callback_data':'Main Balance'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Deposit History' and sender_id in logged_in:
                data = grab_data_two.depo_user(saved_username[sender_id], cur)
                if data == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'Nothing to show here', [[{'text':'↩️ Back', 'callback_data':'History'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    serial = 1
                    full_text = ''
                    for i in data:
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        amount = investment_num(float(i[2])).replace('.', '\\.')
                        date = i[0].replace('-', '\\-')
                        full_text += f'{serial}\\. Time: {date} \\| Transaction Hash: {i[1]} \\| Amount: {amount} bits\n\n'
                        serial += 1
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'↩️ Back', 'callback_data':'History'}]])
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'Withdraw History' and sender_id in logged_in:
                data = grab_data_two.with_user(saved_username[sender_id], cur)
                if data == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'Nothing to show here', [[{'text':'↩️ Back', 'callback_data':'History'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    serial = 1
                    full_text = ''
                    for i in data:
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        date = i[0].replace('-', '\\-')
                        amount = investment_num(float(i[3])).replace('.', '\\.')
                        full_text += f'{serial}\\. Time: {date} \\| Withdrawal Address: {i[1]} \\| Transaction Hash{i[2]} \\| Amount {amount} bits \\| Status {i[4]}\n\n'
                        serial += 1
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'↩️ Back', 'callback_data':'History'}]])
                    bot.get_updates(offset = update_id+1)

            if callback_data == 'Back' and sender_id in logged_in:
                if sender_id in update_success:
                    update_success.remove(sender_id)
                if sender_id in sumamry_pass:
                    sumamry_pass.remove(sender_id)
                promo = grab_data_two.hold_promo(saved_username[sender_id], cur)
                stand = grab_data_two.hold_stand(saved_username[sender_id], cur)
                tol_bal = grab_data_two.balance_balance(saved_username[sender_id], cur)
                total = int(promo) + int(stand) + int(tol_bal)
                bot.edit_message_two(group_id, message_id, f'👤 *My BitBot \\- {saved_username[sender_id]}*', [[{'text':f'💰 My BitBot Balance: {investment_num(total)} bits', 'callback_data': 'Main Balance'}], 
                                                                        [{'text':'📈 My Portfolio', 'callback_data':'Investment Account'}], 
                                                                        [{'text':'👥 My Ambassador Profile', 'callback_data':'Ambassador Account'}], 
                                                                        [{'text':'My Summary', 'callback_data':'My Summary'}],
                                                                        [{'text':'📄 More', 'callback_data':'More'},{'text':'🔐 Log Out', 'callback_data':'Log Out'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'My Summary' and sender_id in logged_in:
                sumamry_pass.append(sender_id)
                bot.edit_message_two(group_id, message_id, 'Enter your *Password*', [[{'text':'↩️ Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Ambassador Account' and sender_id in logged_in:
                details = grab_data_two.user_user(saved_username[sender_id], cur)
                dire = grab_data_two.ambaused_username(details[4], cur)
                direct = []
                for i in dire:
                    if i == 'Nothing':
                        pass
                    else:
                        direct.append(i[0])
                tree_tracking.qualified_mile(saved_username[sender_id], cur)
                tree_tracking.qualified_resi(saved_username[sender_id], cur)
                tree = grab_data_two.amba_tree(saved_username[sender_id], cur)
                amba_balance = grab_data_two.balance_amba(saved_username[sender_id], cur)
                bot.edit_message_two(group_id, message_id, f'👤 *My Ambassador \\- {saved_username[sender_id]}\n\nDirect Referrals: {len(direct)}*', [[{'text':f'My Ambassador Volume: {investment_num(tree)} bits', 'callback_data':'None'}],
                                                                                                                                                [{'text':f'My Ambassador Earnings: {investment_num(amba_balance)} bits', 'callback_data':'Ambassador Earning'}],
                                                                                                                                                [{'text':'Ambassador Compensation Plan', 'callback_data':'Ambassador Compensation'}],
                                                                                                                                                [{'text':'↩️ Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Ambassador Earning' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, '*My Ambassador Earnings*', [[{'text':'Referral Bonus', 'callback_data':'Referral Bonus'}],
                                                                                        [{'text':'Lifetime Milestone Bonus', 'callback_data':'Milestone Bonus'}],
                                                                                        [{'text':'Ambassador Residual Income', 'callback_data':'Residual Bonus'}],
                                                                                        [{'text':'↩️ Back', 'callback_data':'Ambassador Account'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Milestone Bonus' and sender_id in logged_in:
                data = grab_data_two.ambatra_milestone(saved_username[sender_id], cur)
                if data == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'Nothing to show here', [[{'text':'↩️ Back', 'callback_data':'Ambassador Earning'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    serial = 1
                    full_text = ''
                    for i in data:
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        amount = investment_num(float(i[1])).replace('.', '\\.')
                        full_text += f'{serial}\\. Type: {i[0]} \\| Amount: {amount} bits \\| Description: {i[2]}\n\n'
                        serial += 1
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'↩️ Back', 'callback_data':'Ambassador Earning'}]])
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'Referral Bonus' and sender_id in logged_in:
                data = grab_data_two.ambatra_referral(saved_username[sender_id], cur)
                if data == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'Nothing to show here', [[{'text':'↩️ Back', 'callback_data':'Ambassador Earning'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    serial = 1
                    full_text = ''
                    for i in data:
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        amount = investment_num(float(i[1])).replace('.', '\\.')
                        full_text += f'{serial}\\. Type: {i[0]} \\| Amount: {amount} bits \\| Description: {i[2]}\n\n'
                        serial += 1
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'↩️ Back', 'callback_data':'Ambassador Earning'}]])
                    bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Residual Bonus' and sender_id in logged_in:
                data = grab_data_two.ambatra_residual(saved_username[sender_id], cur)
                if data == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'Nothing to show here', [[{'text':'↩️ Back', 'callback_data':'Ambassador Earning'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    full_text = ''
                    serial = 1
                    for i in data:
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        amount = investment_num(float(i[1])).replace('.', '\\.')
                        full_text += f'{serial}\\. Type: {i[0]} \\| Amount: {amount} bits \\| Description: {i[2]}\n\n'
                        serial += 1
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'↩️ Back', 'callback_data':'Ambassador Earning'}]])
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'Ambassador Compensation' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, f'👤 *Ambassador Compensation Plan \\- {saved_username[sender_id]}*', [[{'text': 'Referral Bonus', 'callback_data':'Referral Chart'}],
                                                                                                                                [{'text':'Ambassador Milestone Bonus', 'callback_data':'Milestone Chart'}],
                                                                                                                                [{'text':'Ambassador Residual  Income', 'callback_data':'Residual Chart'}],
                                                                                                                                [{'text':'↩️ Back', 'callback_data':'Ambassador Account'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Referral Chart' and sender_id in logged_in:
                bot.send_photo(group_id, "https://dl.dropboxusercontent.com/s/87km2p65k1p70jw/photo_2020-08-12_20-31-07.jpg")
                bot.send_message_four(sender_id, '*You can use your Ambassador Code to help enrol anyone to our services\\. For each referral that successfully purchased an eligible investment product, you will earn a bonus\\. You can earn unlimited Referral Bonuses\\. You can earn 1 bonus reward per user referred\\. Please consult the following table for eligible investments and corresponding bonus\\.*', [[{'text':'↩️ Back', 'callback_data':'Ambassador Compensation'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Milestone Chart' and sender_id in logged_in:
                bot.send_photo(group_id, "https://dl.dropboxusercontent.com/s/7jjsyoobrdwd7bn/photo_2020-08-12_20-32-00.jpg")
                bot.send_message_four(sender_id, '*To qualify for Ambassador Milestone Bonus, you must personally invite two investors to enroll in our investment services and purchase an investment product\\.\\(Ex: You invested 0\\.50 BTC, and referred John and David\\. John and David then invested 0\\.25 BTC each\\. You will qualify for the Ambassador Milestone Bonus\\.\\)*', [[{'text':'↩️ Back', 'callback_data':'Ambassador Compensation'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Residual Chart' and sender_id in logged_in:
                bot.send_photo(group_id, "https://dl.dropboxusercontent.com/s/j3c3ygscahktefa/photo_2020-08-12_20-32-14.jpg")
                bot.send_message_four(sender_id, '*To qualify for Ambassador Income, you must personally invite two Ambassadors who acquired an Ambassador Volume of 1\\.00 BTC\\.\\(Ex: You invested 3\\.00 BTC, and referred John and David\\. John and David then invested 1\\.00 BTC each\\. You will qualify for the Ambassador Residual Interest Earnings\\.\\)*', [[{'text':'↩️ Back', 'callback_data':'Ambassador Compensation'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Investment Account' and sender_id in logged_in:
                if sender_id in update_success:
                    update_success.remove(sender_id)
                if sender_id in pro_name:
                    del pro_name[sender_id]
                    del pro_price[sender_id]
                if sender_id in sell_invest:
                    sell_invest.remove(sender_id)
                if sender_id in buy_invest:
                    buy_invest.remove(sender_id)
                promo = grab_data_two.hold_promo(saved_username[sender_id], cur)
                stand = grab_data_two.hold_stand(saved_username[sender_id], cur)
                total = int(promo) + int(stand)
                bot.edit_message_two(group_id, message_id, f'👤 *My Investment Portfolio \\- {saved_username[sender_id]}*', [[{'text':f'My Portfolio: {investment_num(total)} bits', 'callback_data':'None'}], 
                                                                                                            [{'text':'My Investments', 'callback_data':'My Investment'}],
                                                                                                            [{'text':'My Earnings', 'callback_data':'Earnings'}],
                                                                                                            [{'text':'Buy', 'callback_data':'Buy Investment'}, {'text':'Sell', 'callback_data':'Sell An Investment'}],
                                                                                                            [{'text':'Investments History', 'callback_data':'Investment History'}],
                                                                                                            [{'text':'↩️ Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Investment History' and sender_id in logged_in:
                if grab_data_two.trans_det(saved_username[sender_id], cur) == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'Nothing to show here', [[{'text':'Back','callback_data':'Investment Account'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    full_text = ''
                    serial = 1
                    data = grab_data_two.trans_det(saved_username[sender_id], cur)
                    for i in range(len(data)):
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        h = data[i]
                        tim = h[1].replace('-', '\\-')
                        full_text += f'{serial}\\. Type: {h[0]} Time: {tim} Product: {h[2]} Value: {h[3]}\n'
                        serial += 1
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back','callback_data':'Investment Account'}]])
                    bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Earnings' and sender_id in logged_in:
                data = grab_data_two.payout_details(saved_username[sender_id], cur)
                if data == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'Nothing to show here', [[{'text':'Back','callback_data':'Investment Account'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    full_text = ''
                    serial = 1
                    for i in range(len(data)):
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        h = data[i]
                        amount = h[1]
                        amount = investment_num(amount)
                        amount = amount.replace('.','\\.')
                        full_text += f'{serial}\\. Product: {h[0]} \\| Amount: {amount} bits\n\n'
                        serial += 1
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back','callback_data':'Investment Account'}]])
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'My Investment' and sender_id in logged_in:
                if grab_data_two.holding_holding(saved_username[sender_id], cur) == 'Nothing' or grab_data_two.holding_holding(saved_username[sender_id], cur) == None:
                    bot.edit_message_two(group_id, message_id, 'Nothing to show here', [[{'text':'Back','callback_data':'Investment Account'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    holding = grab_data_two.holding_holding(saved_username[sender_id], cur).split(' ')
                    holding_pro = []
                    holding_amount = []
                    a = 0
                    for i in holding:
                        if len(i) == 0:
                            pass
                        elif i.isnumeric():
                            holding_amount.append(i)
                        else:
                            holding_pro.append(i)
                    b = 0
                    total = 0
                    full_text = ''
                    full_text += '*Your current holdings*\n\nProduct \\| Amount \\| Value\\(bits\\)\n'
                    for i in range(len(holding_amount)):
                        if len(full_text) > 4000:
                            bot.send_message(sender_id,full_text)
                            full_text = ''
                        cost = grab_data_two.inve_price(holding_pro[b], cur)
                        full_text += f'{holding_pro[b]}      {holding_amount[b]}    {int(cost)*int(holding_amount[b])}\n'
                        total += int(cost)*int(holding_amount[b])
                        b += 1
                    e = "{:,}".format(total)
                    full_text += f'\nTotal Value: {e} bits'
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'↩️ Back', 'callback_data':'Investment Account'}]])
                    bot.get_updates(offset = update_id+1)
            elif callback_data == 'Manage Investment' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, f'*Manage Investment \\- {saved_username[sender_id]}*', [[{'text':'Buy', 'callback_data':'Buy Investment'},{'text':'Sell', 'callback_data':'Sell An Investment'}],
                                                                                                                [{'text':'Back','callback_data':'Investment Account'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Buy Investment' and sender_id in logged_in:
                products = grab_data_two.inve_cate_two(cur)
                full_code = []
                for a in products:
                    full_code.append({'text':f'{a}', 'callback_data':f'{a}'})
                c = 1
                d = 0
                part = []
                while full_code[-1] not in full_code[d:c]:
                    part.append(full_code[d:c])
                    c += 1
                    d += 1
                if full_code[-1] in full_code[d:c]:
                    part.append(full_code[d:c])
                    part.append([{'text':'Back','callback_data':'Investment Account'}])
                bot.edit_message_two(group_id, message_id, '*Choose Investment Type*', part)
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Sell An Investment' and sender_id in logged_in:
                if grab_data_two.holding_holding(saved_username[sender_id], cur) == 'Nothing' or grab_data_two.holding_holding(saved_username[sender_id], cur) == None:
                    bot.edit_message_two(group_id, message_id, 'No investment available for selling', [[{'text':'Back','callback_data':'Investment Account'}]])
                    bot.get_updates(offset = update_id+1)
                elif len(grab_data_two.holding_holding(saved_username[sender_id], cur)) == 0:
                    bot.edit_message_two(group_id, message_id, 'No investment available for selling', [[{'text':'Back','callback_data':'Investment Account'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    holding = grab_data_two.holding_holding(saved_username[sender_id], cur).split(' ')
                    holding_products = []
                    for i in range(len(holding)):
                        if holding[i].isnumeric() == False and len(holding[i]) > 0:
                            holding_products.append(holding[i])
                        else:
                            pass
                    full_code = []
                    for a in holding_products:
                        full_code.append({'text':f'{a}', 'callback_data':f'{a}'})
                    c = 3
                    d = 0
                    part = []
                    while full_code[-1] not in full_code[d:c]:
                        part.append(full_code[d:c])
                        c += 3
                        d += 3
                    if full_code[-1] in full_code[d:c]:
                        part.append(full_code[d:c])
                        part.append([{'text':'Back','callback_data':'Investment Account'}])
                    holding = grab_data_two.holding_holding(saved_username[sender_id], cur).split(' ')
                    holding_pro = []
                    holding_amount = []
                    a = 0
                    for i in holding:
                        if len(i) == 0:
                            pass
                        elif i.isnumeric():
                            holding_amount.append(i)
                        else:
                            holding_pro.append(i)
                    b = 0
                    total = 0
                    full_text = ''
                    full_text += '*Your current holdings*\n\nProduct \\| Amount \\| Value\\(bits\\)\n'
                    for i in range(len(holding_amount)):
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        cost = grab_data_two.inve_price(holding_pro[b], cur)
                        full_text += f'{holding_pro[b]}      {holding_amount[b]}    {int(cost)*int(holding_amount[b])}\n'
                        total += int(cost)*int(holding_amount[b])
                        b += 1
                    sell_invest.append(sender_id)
                    bot.edit_message_two(group_id, message_id, f'{full_text}\n\nSell An Investment', part)
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'Confirm Investment' and sender_id in logged_in:
                balance = float(grab_data_two.balance_balance(saved_username[sender_id], cur))
                if balance < pro_price[sender_id]:
                    bot.edit_message_two(group_id, message_id, 'Not Enough Balance', [[{'text':'Back', 'callback_data':'Investment Account'}]])
                    if sender_id in pro_name:
                        del pro_name[sender_id]
                        del pro_price[sender_id]
                    bot.get_updates(offset = update_id+1)
                elif balance >= pro_price[sender_id]:
                    if grab_data_two.holding_user(saved_username[sender_id], cur) == 'No':
                        data_input.investment_holding(saved_username[sender_id], 0,0, 'Nothing', cur)
                    update_data.balance_info(saved_username[sender_id], float(balance)-pro_price[sender_id], cur)
                    d = pro_price[sender_id]
                    e = "{:,}".format(int(d))
                    time_sold = int(grab_data_two.inve_sold(pro_name[sender_id], cur))
                    time_sold += 1
                    update_data.invement_sold(pro_name[sender_id], time_sold, cur)
                    holding = grab_data_two.holding_holding(saved_username[sender_id], cur)
                    if holding == None or holding == 'Nothing':
                        holding = []
                    else:
                        holding = holding.split(' ')
                    if pro_name[sender_id] in holding and sender_id not in update_success:
                        a = 0
                        while holding[a] != pro_name[sender_id]:
                            if holding[a] == pro_name[sender_id]:
                                break
                            else:
                                a += 1
                        held = holding[a+1]
                        holding.remove(holding[a])
                        holding.remove(holding[a])
                        full_text = ''
                        for i in holding:
                            if len(i) == 0:
                                holding.remove(i)
                                pass
                            else:
                                full_text += f'{str(i)} '
                        full_text += f'{pro_name[sender_id]} {int(held) + 1}'
                        if pro_name[sender_id].startswith('P') and sender_id not in update_success:
                            promo = int(grab_data_two.hold_promo(saved_username[sender_id], cur))
                            update_data.invest_promo(saved_username[sender_id], int(d)+promo, full_text, cur)
                            update_success.append(sender_id)
                            bonus_given = grab_data_two.amba_bonus(saved_username[sender_id], cur)
                            if bonus_given == 'False':
                                bonus_to_give = grab_data_two.inve_bonus(pro_name[sender_id], cur)
                                refer_used = grab_data_two.amba_used(saved_username[sender_id], cur)
                                refer_username = grab_data_two.amba_username(refer_used, cur)
                                refer_balance = grab_data_two.inve_bala(refer_username, cur)
                                refer_amba = grab_data_two.balance_amba(refer_username, cur)
                                update_data.balance_info(refer_username, refer_balance+bonus_to_give, cur)
                                update_data.balance_amba(refer_username, bonus_to_give+refer_amba, cur)
                                update_data.bonus_given(saved_username[sender_id], cur)
                                serial = grab_data_two.amba_serial(cur)
                                data_input.ambassador_transactions(refer_username, 'Referral', bonus_to_give, f'Referral Bonus from {saved_username[sender_id]}', serial, cur)
                        else:
                            d = pro_price[sender_id]
                            stand = int(grab_data_two.hold_stand(saved_username[sender_id], cur))
                            update_data.invest_stand(saved_username[sender_id], int(d)+stand, full_text, cur)
                            update_success.append(sender_id)

                    elif pro_name[sender_id] not in holding and sender_id not in update_success:
                        full_text = ''
                        for i in holding:
                            if i == 'Nothing':
                                pass
                            else:
                                full_text += f'{str(i)} '
                        full_text += f'{pro_name[sender_id]} 1'
                        if pro_name[sender_id].startswith('P'):
                            promo = int(grab_data_two.hold_promo(saved_username[sender_id], cur))
                            update_data.invest_promo(saved_username[sender_id], int(d)+promo, full_text, cur)
                        else:
                            promo = int(grab_data_two.hold_stand(saved_username[sender_id], cur))
                            update_data.invest_stand(saved_username[sender_id], int(d)+promo, full_text, cur)
                        bonus_given = grab_data_two.amba_bonus(saved_username[sender_id], cur)
                        if bonus_given == 'False' and pro_name[sender_id].startswith('P'):
                            bonus_to_give = grab_data_two.inve_bonus(pro_name[sender_id], cur)
                            refer_used = grab_data_two.amba_used(saved_username[sender_id], cur)
                            refer_username = grab_data_two.amba_username(refer_used, cur)
                            refer_balance = grab_data_two.inve_bala(refer_username, cur)
                            refer_amba = grab_data_two.balance_amba(refer_username, cur)
                            update_data.balance_info(refer_username, refer_balance+bonus_to_give, cur)
                            update_data.balance_amba(refer_username, bonus_to_give+refer_amba, cur)
                            update_data.bonus_given(saved_username[sender_id], cur)
                            serial = grab_data_two.amba_serial(cur)
                            data_input.ambassador_transactions(refer_username, 'Referral', bonus_to_give, f'Referral Bonus from {saved_username[sender_id]}', serial, cur)
                        update_success.append(sender_id)
                    enroll = grab_data_two.holding_enrolled(saved_username[sender_id], cur)
                    if enroll == 'False':
                        update_data.enrolled(saved_username[sender_id], cur)
                    tree_tracking.qualified_mile(saved_username[sender_id], cur)
                    tree_tracking.qualified_resi(saved_username[sender_id], cur)
                    amba_used = grab_data_two.amba_used(saved_username[sender_id], cur)
                    amba_username = grab_data_two.amba_username(amba_used, cur)
                    qualified = int(grab_data_two.qualified_mile(amba_username, cur))
                    tree_inve = int(grab_data_two.amba_tree(amba_username, cur))
                    tree_bala = int(grab_data_two.inve_bala(amba_username, cur))
                    tree_amba = int(grab_data_two.balance_amba(amba_username, cur))
                    tree_tier = grab_data_two.milestone_tier(amba_username, cur)
                    promo = int(grab_data_two.hold_promo(amba_username, cur))
                    stand = int(grab_data_two.hold_stand(amba_username, cur))
                    total = tree_inve + promo + stand
                    if total >= 1000000 and tree_tier[0] == 'False' and qualified >= 2:
                        update_data.balance_info(amba_username, tree_bala+200000, cur)
                        update_data.balance_amba(amba_username, tree_amba+200000, cur)
                        total += 200000
                        serial = grab_data_two.amba_serial(cur)
                        data_input.ambassador_transactions(amba_username, 'Milestone', 200000, f'Milestone 1 BTC', serial, cur)
                        update_data.tier(amba_username, 'Tier_1', cur)
                    if total >= 2000000 and tree_tier[1] == 'False' and qualified >= 2:
                        update_data.balance_info(amba_username, tree_bala+200000, cur)
                        update_data.balance_amba(amba_username, tree_amba+200000, cur)
                        total += 200000
                        update_data.tier(amba_username, 'Tier_2', cur)
                        serial = grab_data_two.amba_serial(cur)
                        data_input.ambassador_transactions(amba_username, 'Milestone', 200000, f'Milestone 2 BTC', serial, cur)
                    if total >= 5000000 and tree_tier[2] == 'False' and qualified >= 2:
                        update_data.balance_info(amba_username, tree_bala+200000, cur)
                        update_data.balance_amba(amba_username, tree_amba+200000, cur)
                        total += 200000
                        update_data.tier(amba_username, 'Tier_3', cur)
                        serial = grab_data_two.amba_serial(cur)
                        data_input.ambassador_transactions(amba_username, 'Milestone', 200000, f'Milestone 5 BTC', serial, cur)
                    if total >= 10000000 and tree_tier[3] == 'False' and qualified >= 2:
                        update_data.balance_info(amba_username, tree_bala+400000, cur)
                        update_data.balance_amba(amba_username, tree_amba+400000, cur)
                        total += 400000
                        update_data.tier(amba_username, 'Tier_4', cur)
                        serial = grab_data_two.amba_serial(cur)
                        data_input.ambassador_transactions(amba_username, 'Milestone', 400000, f'Milestone 10 BTC', serial, cur)
                    if total >= 50000000 and tree_tier[4] == 'False' and qualified >= 2:
                        update_data.balance_info(amba_username, tree_bala+2000000, cur)
                        update_data.balance_amba(amba_username, tree_amba+2000000, cur)
                        total += 2000000
                        update_data.tier(amba_username, 'Tier_5', cur)
                        serial = grab_data_two.amba_serial(cur)
                        data_input.ambassador_transactions(amba_username, 'Milestone', 2000000, f'Milestone 50 BTC', serial, cur)
                    if total >= 100000000 and tree_tier[5] == 'False' and qualified >= 2:
                        update_data.balance_info(amba_username, tree_bala+5000000, cur)
                        update_data.balance_amba(amba_username, tree_amba+5000000, cur)
                        update_data.tier(amba_username, 'Tier_6', cur)
                        serial = grab_data_two.amba_serial(cur)
                        data_input.ambassador_transactions(amba_username, 'Milestone', 5000000, f'Milestone 100 BTC', serial, cur)

                    date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                    serial = grab_data_two.invest_serial(cur)
                    print('here')
                    print(pro_name[sender_id])
                    print(serial)
                    data_input.investment_transactions(saved_username[sender_id], date, 'Buy', pro_name[sender_id], d, serial, cur)
                    bot.edit_message_two(group_id, message_id, f'Successfully Purchased 1 x *{pro_name[sender_id]}* for *{e}* bits', [[{'text':'Back', 'callback_data':'Investment Account'}]])
                    if sender_id in pro_name:
                        del pro_name[sender_id]
                        del pro_price[sender_id]
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'Cancel Investment' and sender_id in logged_in:
                if sender_id in pro_name:
                    del pro_name[sender_id]
                    del pro_price[sender_id]
                bot.edit_message_two(group_id, message_id, 'Transaction Cancelled', [[{'text':'Back', 'callback_data':'Investment Account'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data in grab_data_two.inve_type(callback_data, cur) and sender_id in logged_in:
                products = grab_data_two.inve_name(callback_data, cur)
                full_code = []
                for a in products:
                    if len(a) == 0:
                        pass
                    else:
                        full_code.append({'text':f'{a}', 'callback_data':f'{a}'})
                c = 3
                d = 0
                part = []
                while full_code[-1] not in full_code[d:c]:
                    part.append(full_code[d:c])
                    c += 3
                    d += 3
                if full_code[-1] in full_code[d:c]:
                    part.append(full_code[d:c])
                    part.append([{'text':'Back','callback_data':'Investment Account'}])
                bot.edit_message_two(group_id, message_id, f'{grab_data_two.descri_pro(callback_data, cur)}\n\n*Choose Product*', part)
                buy_invest.append(sender_id)
                bot.get_updates(offset = update_id+1)

            elif callback_data == grab_data_two.inve_name_two(callback_data, cur) and sender_id in logged_in and sender_id in buy_invest:
                d = grab_data_two.inve_price(callback_data, cur)
                e = "{:,}".format(int(d))
                bot.edit_message_two(group_id, message_id, f'Are you sure you want to Buy 1 x *{callback_data}* with *{e}* bits?', [[{'text':'Confirm','callback_data':'Confirm Investment'}, {'text':'Cancel', 'callback_data':'Cancel Investment'}]])
                pro_name[sender_id] = callback_data
                pro_price[sender_id] = int(grab_data_two.inve_price(callback_data, cur))
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == grab_data_two.inve_name_two(callback_data, cur) and sender_id in logged_in and sender_id in sell_invest:
                d = grab_data_two.inve_price(callback_data, cur)
                e = "{:,}".format(int(d))
                bot.edit_message_two(group_id, message_id, f'Are you sure you want to Sell 1 x *{callback_data}* and get *{e}* bits?', [[{'text':'Confirm','callback_data':'Sell Investment'}, {'text':'Cancel', 'callback_data':'Cancel Investment'}]])
                pro_name[sender_id] = callback_data
                pro_price[sender_id] = int(grab_data_two.inve_price(callback_data, cur))
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Sell Investment' and sender_id in logged_in:
                balance = float(grab_data_two.balance_balance(saved_username[sender_id], cur))
                update_data.balance_info(saved_username[sender_id], float(balance)+pro_price[sender_id]-1000, cur)
                holding = grab_data_two.holding_holding(saved_username[sender_id], cur).split(' ')
                a = 0
                while holding[a] != pro_name[sender_id]:
                    a += 1
                if int(holding[a+1]) != 1:
                    holding[a+1] = f'{int(holding[a+1]) - 1}'
                elif int(holding[a+1]) == 1:
                    holding.remove(holding[a])
                    holding.remove(holding[a])
                full_text = ''
                for i in holding:
                    if len(i) == 0:
                        holding.remove(i)
                        pass
                    else:
                        full_text += f'{str(i)} '
                if pro_name[sender_id].startswith('P'):
                    promo = int(grab_data_two.hold_promo(saved_username[sender_id], cur))
                    d = pro_price[sender_id]
                    update_data.invest_promo(saved_username[sender_id], promo-int(d), full_text, cur)
                else:
                    stand = int(grab_data_two.hold_stand(saved_username[sender_id], cur))
                    d = pro_price[sender_id]
                    bal = stand-int(d)
                    update_data.invest_stand(saved_username[sender_id], bal, full_text, cur)
                date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                serial = grab_data_two.invest_serial(cur)
                data_input.investment_transactions(saved_username[sender_id], date, 'Sell', pro_name[sender_id], pro_price[sender_id], serial, cur)
                bot.edit_message_two(group_id, message_id, f'Successfully Sold 1 x {pro_name[sender_id]}', [[{'text':'Back', 'callback_data':'Investment Account'}]])
                if sender_id in pro_name:
                    del pro_name[sender_id]
                    del pro_price[sender_id]
                if sender_id in buy_invest:
                    buy_invest.remove(sender_id)
                if sender_id in sell_invest:
                    sell_invest.remove(sender_id)
                bot.get_updates(offset = update_id+1)

            elif callback_data in grab_data_two.inve_cate_two(cur) and sender_id in logged_in:
                products = grab_data_two.inve_cate(callback_data, cur)
                full_code = []
                for a in products:
                    full_code.append({'text':f'{a}', 'callback_data':f'{a}'})
                c = 3
                d = 0
                part = []
                while full_code[-1] not in full_code[d:c]:
                    part.append(full_code[d:c])
                    c += 3
                    d += 3
                if full_code[-1] in full_code[d:c]:
                    part.append(full_code[d:c])
                    part.append([{'text':'Back','callback_data':'Investment Account'}])
                bot.edit_message_two(group_id, message_id, '*Choose Product Type*', part)
                bot.get_updates(offset = update_id+1)
            
            

            if callback_data == 'More' and sender_id in logged_in:
                if sender_id in report_bug:
                    report_bug.remove(sender_id)
                bot.edit_message_two(group_id, message_id, f'*👤 My BitBot \\- {saved_username[sender_id]}*', [[{'text':'📜 ToS', 'callback_data':'TOS'}, {'text':'🐛 Report Bug', 'callback_data':'Report Bug'}], 
                                                                                                            [{'text':'📚 FAQ', 'callback_data':'FAQ'}, {'text':'💬 Help', 'callback_data':'Help Buttons'}],
                                                                                                            [{'text':'ℹ️ About Us', 'callback_data':'About Us'}, {'text':'↩️ Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Report Bug' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Send your message now to record the feedback', [[{'text':'↩️ Back', 'callback_data':'More'}]])
                report_bug.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'About Us' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, '[Learn more about us from here](https://t.me/ChannelBitBot/17)', [[{'text':'↩️ Back', 'callback_data':'More'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'FAQ' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, '[BitBot FAQ is available here](https://t.me/ChannelBitBot/16)', [[{'text':'↩️ Back', 'callback_data':'More'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Help Buttons' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, f'*💬 Help \\- {saved_username[sender_id]}*', [[{'text':'Chat Support', 'callback_data':'Chat Support'}],
                                                                        [{'text':'Email Support', 'callback_data':'Email Support'}],
                                                                        [{'text':'↩️ Back', 'callback_data':'More'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'TOS' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, '*ToS Menu*\n\n\\- [Account Access and Privacy Policy](https://t.me/ChannelBitBot/12)\n\\- [Deposit & Withdrawal Policy](https://t.me/ChannelBitBot/13)\n\\- [Fund Management Policy](https://t.me/ChannelBitBot/14)\n\\- [Investment Policy](https://t.me/ChannelBitBot/15)', [[{'text':'↩️ Back', 'callback_data':'More'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Chat Support' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Message us \\@BitBotTeam for help', [[{'text':'↩️ Back', 'callback_data':'More'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Email Support' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Email us at BitBotSupport\\@protonmail\\.com', [[{'text':'↩️ Back', 'callback_data':'More'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Log Out':
                if sender_id in logged_in:
                    logged_in.remove(sender_id)
                bot.edit_message_two(group_id, message_id, 'Logged Out', [[{'text':'Login', 'callback_data': 'Login'}, {'text':'Register', 'callback_data':'Register'}]])
                bot.get_updates(offset = update_id+1)
        else:
            text = current_updates['message']['text']
            print(text)
            if text == '/help':
                special = ['@', '=', '.', '>', '-']
                texts = grab_data_two.help_text(cur)
                for i in special:
                    texts = texts.replace(i, f'\\{i}')
                bot.send_message(sender_id, texts)
                bot.send_message(sender_id, 'Type /start to get back to the main menu')
                bot.get_updates(offset = update_id+1)

            if text == '/start' and sender_id not in logged_in:
                if sender_id in loggin_in:
                    loggin_in.remove(sender_id)
                if sender_id in registering:
                    registering.remove(sender_id)
                if sender_id in submitting:
                    submitting.remove(sender_id)
                if sender_id in password_in:
                    password_in.remove(sender_id)
                if sender_id in user_regis:
                    user_regis.remove(sender_id)
                bot.send_message_four(sender_id, '👤 *BitBot Client Authorization*\n\nSend /help to get more details', [[{'text':'🔑 Log In', 'callback_data': 'Login'}, {'text':'®️ Register', 'callback_data':'Register'}]])
                bot.get_updates(offset = update_id+1)

            elif text == '/start' and sender_id in logged_in:
                if sender_id in update_success:
                    update_success.remove(sender_id)
                if sender_id in temp_pass:
                    del temp_pass[sender_id]
                if sender_id in temp_acc:
                    del temp_acc[sender_id]
                if sender_id in submitting:
                    submitting.remove(sender_id)
                if sender_id in password_in:
                    password_in.remove(sender_id)
                if sender_id in user_regis:
                    user_regis.remove(sender_id)
                if sender_id in registering:
                    registering.remove(sender_id)
                if sender_id in loggin_in:
                    loggin_in.remove(sender_id)
                if sender_id in report_bug:
                    report_bug.remove(sender_id)
                if sender_id in withdraw:
                    withdraw.remove(sender_id)
                if sender_id in temp_with:
                    del temp_with[sender_id]
                if sender_id in pro_name:
                    del pro_name[sender_id]
                if sender_id in pro_price:
                    del pro_price[sender_id]
                if sender_id in sell_invest:
                    sell_invest.remove(sender_id)
                if sender_id in buy_invest:
                    buy_invest.remove(sender_id)
                if sender_id in sumamry_pass:
                    sumamry_pass.remove(sender_id)
                promo = grab_data_two.hold_promo(saved_username[sender_id], cur)
                stand = grab_data_two.hold_stand(saved_username[sender_id], cur)
                tol_bal = int(grab_data_two.balance_balance(saved_username[sender_id], cur))
                total = int(promo) + int(stand) + int(tol_bal)
                bot.send_message_four(sender_id, f'👤 *My BitBot \\- {saved_username[sender_id]}*', [[{'text':f'💰 My BitBot Balance: {investment_num(total)} bits', 'callback_data': 'Main Balance'}], 
                                                                        [{'text':'📈 My Portfolio', 'callback_data':'Investment Account'}], 
                                                                        [{'text':'👥 My Ambassador Profile', 'callback_data':'Ambassador Account'}], 
                                                                        [{'text':'My Summary', 'callback_data':'My Summary'}],
                                                                        [{'text':'📄 More', 'callback_data':'More'},{'text':'🔐 Log Out', 'callback_data':'Log Out'}]])
                bot.get_updates(offset = update_id+1)

            
            if sender_id in loggin_in and grab_data_two.user_username(text.lower(), cur)[0] == 'Nothing':
                bot.send_message(sender_id, 'Please provide a valid *Username*')
                bot.get_updates(offset = update_id+1)

            elif sender_id in loggin_in and text.lower() in grab_data_two.user_username(text, cur)[0]:
                saved_username[sender_id] = text.lower()
                bot.send_message(sender_id, 'Please enter your *Password*')
                loggin_in.remove(sender_id)
                if sender_id not in password_in:
                    password_in.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in password_in and text != grab_data_two.user_password(saved_username[sender_id], cur):
                bot.send_message(sender_id, 'Incorrect password, please try again\n\nIf you are having trouble contact us here: [Support Team](https://t.me/BitBotTeam)')
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in password_in and text == grab_data_two.user_password(saved_username[sender_id], cur):
                bot.delete_message(sender_id, message_id)
                bot.send_message(sender_id, 'Welcome Back\\!')
                password_in.remove(sender_id)
                if sender_id not in logged_in:
                    logged_in.append(sender_id)
                if grab_data_two.holding_user(saved_username[sender_id], cur) == 'No':
                    data_input.investment_holding(saved_username[sender_id], 0,0, 'Nothing', cur)
                promo = grab_data_two.hold_promo(saved_username[sender_id], cur)
                stand = grab_data_two.hold_stand(saved_username[sender_id], cur)
                tol_bal = int(grab_data_two.balance_balance(saved_username[sender_id], cur))
                total = int(promo) + int(stand) + int(tol_bal)
                bot.send_message_four(sender_id, f'👤 *My BitBot \\- {saved_username[sender_id]}*', [[{'text':f'💰 My BitBot Balance: {investment_num(total)} bits', 'callback_data': 'Main Balance'}], 
                                                                        [{'text':'📈 My Portfolio', 'callback_data':'Investment Account'}], 
                                                                        [{'text':'👥 My Ambassador Profile', 'callback_data':'Ambassador Account'}], 
                                                                        [{'text':'My Summary', 'callback_data':'My Summary'}],
                                                                        [{'text':'📄 More', 'callback_data':'More'},{'text':'🔐 Log Out', 'callback_data':'Log Out'}]])
                bot.get_updates(offset = update_id+1)
            
            
            if sender_id in registering and text in grab_data_two.user_amba(text, cur)[0]:
                bot.send_message(sender_id, 'Please enter a username of your choice\n3\\-10 Alphanumeric')
                registering.remove(sender_id)
                if sender_id not in user_regis:
                    user_regis.append(sender_id)
                temp_acc[sender_id] = text
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in registering and grab_data_two.user_amba(text, cur)[0] == 'Nothing':
                bot.send_message(sender_id, 'Sorry, the access code is invalid\\.\nFor assistance, please contact our [Support Team](https://t.me/BitBotTeam)', disable_web_page_preview=True)
                bot.get_updates(offset = update_id+1)

            elif sender_id in user_regis and len(text) > 2 and grab_data_two.user_username(text, cur)[0] == 'Nothing' and len(text) > 2 and len(text) < 11 and '-' in text:
                bot.send_message(sender_id, 'Username Invalid\\. Please type a new one')
                bot.get_updates(offset = update_id+1)

            elif sender_id in user_regis and len(text) > 2 and grab_data_two.user_username(text, cur)[0] == 'Nothing' and len(text) > 2 and len(text) < 11 and '_' in text:
                bot.send_message(sender_id, 'Username Invalid\\. Please type a new one')
                bot.get_updates(offset = update_id+1)

            elif sender_id in user_regis and len(text) > 2 and grab_data_two.user_username(text, cur)[0] == 'Nothing' and len(text) > 2 and len(text) < 11:
                register_id[sender_id] = message_id+1
                code = generate_pass()
                passw = code[0]
                amba_code = code[1]
                while passw in grab_data_two.all_pass(cur) or amba_code in grab_data_two.all_amba(cur):
                    code = generate_pass()
                    passw = code[0]
                    amba_code = code[1]
                saved_username[sender_id] = text.lower()
                saved_amba[sender_id] = amba_code
                bot.send_message(sender_id, f'Your account is ready\\!\nUsername: {text.lower()}\nPassword: {passw}\nAmbassador Code: {amba_code}')
                if sender_id not in temp_pass:
                    temp_pass[sender_id] = passw
                if sender_id not in submitting:
                    submitting.append(sender_id)
                user_regis.remove(sender_id)
                bot.send_message(sender_id, 'Copy and submit your password to confirm you have saved your credentials')
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in user_regis and len(text) > 2 and text in grab_data_two.user_username(text, cur)[0]:
                bot.send_message(sender_id, 'Username already exist\\. Please type a new one')
                bot.get_updates(offset = update_id+1)

            elif sender_id in submitting and text == temp_pass[sender_id] and len(text) > 9:
                bot.delete_message(sender_id, register_id[sender_id])
                bot.delete_message(sender_id, message_id)
                bot.send_message(sender_id, 'Thank you for joining, your account is now ready\\!')
                if 'username' in current_updates['message']['from']:
                    username = current_updates['message']['from']['username']
                else:
                    username = 'None'
                first_name = current_updates['message']['from']['first_name']
                date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                ref = grab_data_two.amba_users(temp_acc[sender_id], cur)
                refer_number = ref + 1
                data_input.user_info(sender_id, first_name, saved_username[sender_id], temp_pass[sender_id], saved_amba[sender_id], temp_acc[sender_id], date, username, cur)
                data_input.balance_info(sender_id, first_name, saved_username[sender_id], 0, 0, 0, cur)
                data_input.amba_info(sender_id, first_name, saved_username[sender_id], saved_amba[sender_id], temp_acc[sender_id], 0, cur)
                update_data.amba_info(temp_acc[sender_id], refer_number, cur)
                manager = tree_tracking.up(saved_username[sender_id], cur)
                update_data.manager(saved_username[sender_id], manager, cur)
                if grab_data_two.holding_user(saved_username[sender_id], cur) == 'No':
                    data_input.investment_holding(saved_username[sender_id], 0,0, 'Nothing', cur)
                data_input.milestone_bonus(saved_username[sender_id], cur)
                promo = grab_data_two.hold_promo(saved_username[sender_id], cur)
                stand = grab_data_two.hold_stand(saved_username[sender_id], cur)
                tol_bal = int(grab_data_two.balance_balance(saved_username[sender_id], cur))
                total = int(promo) + int(stand) + int(tol_bal)
                bot.send_message_four(sender_id, f'👤 *My BitBot \\- {saved_username[sender_id]}*', [[{'text':f'💰 My BitBot Balance: {investment_num(total)} bits', 'callback_data': 'Main Balance'}], 
                                                                        [{'text':'📈 My Portfolio', 'callback_data':'Investment Account'}], 
                                                                        [{'text':'👥 My Ambassador Profile', 'callback_data':'Ambassador Account'}],
                                                                        [{'text':'My Summary', 'callback_data':'My Summary'}], 
                                                                        [{'text':'📄 More', 'callback_data':'More'},{'text':'🔐 Log Out', 'callback_data':'Log Out'}]])
                del temp_pass[sender_id]
                submitting.remove(sender_id)
                del temp_acc[sender_id]
                if sender_id not in logged_in:
                    logged_in.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in submitting and text != temp_pass[sender_id] and len(text) > 9:
                bot.send_message(sender_id, 'Password does not match, please try again')
                bot.get_updates(offset = update_id+1)

            if sender_id in sumamry_pass and sender_id in logged_in:
                password = grab_data_two.user_password(saved_username[sender_id], cur)
                if text != password:
                    bot.send_message_four(sender_id, 'Incorrect Password', [[{'text':'Back', 'callback_data': 'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.delete_message(sender_id, message_id)
                    details = grab_data_two.user_user(saved_username[sender_id], cur)
                    promo = grab_data_two.hold_promo(saved_username[sender_id], cur)
                    stand = grab_data_two.hold_stand(saved_username[sender_id], cur)
                    dire = grab_data_two.ambaused_username(details[4], cur)
                    direct = []
                    for i in dire:
                        if i == 'Nothing':
                            pass
                        else:
                            direct.append(i[0])
                    tree = len(tree_tracking.all_refer(details[4], cur))
                    all_inve = tree_tracking.down(details[4], cur)
                    date_joined = details[6].replace('-','\\-')
                    bot.send_message_four(sender_id, f'Username: {saved_username[sender_id]}\nPassword: {text}\nAmbassador Code: {details[4]}\nAmbassador Code Used: {details[5]}\nDate Joined: {date_joined}\nCurrent Holding: {int(promo)+int(stand)} bits\nDirect Refer: {len(direct)}\nTotal Refer: {tree}\nTotal Invest: {int(all_inve)}', [[{'text':'Back', 'callback_data': 'Back'}]])
                    bot.get_updates(offset = update_id+1)

            if len(text) > 63 and sender_id in logged_in:
                bot.send_message(sender_id, 'Transaction Hash Detected\\. Processing Deposit')
                trans_hash = grab_data_two.depo_trans(cur)
                print(trans_hash)
                if text in trans_hash:
                    bot.send_message_four(sender_id, 'Deposit failed\\. Transaction Hash already used', [[{'text':'Back', 'callback_data': 'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    a = requests.get(f'https://blockchain.info/rawtx/{text}').json()
                    data = a['out']
                    outputs = {}
                    for i in data:
                        outputs[i['addr']] = i['value']
                    if grab_data_two.depo_text(cur) in outputs:
                        balance = outputs[grab_data_two.depo_text(cur)]
                        b = int(balance)/100000000
                        c = b*1000000
                        d = "%.2f" % c
                        e = "{:,}".format(float(d))
                        f = e.replace(".","\\.")
                        first_name = current_updates['message']['from']['first_name']
                        date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                        bot.send_message_four(sender_id, f'Total Sent: {f} bits\\. Deposit is Successful', [[{'text':'Back', 'callback_data': 'Back'}]])
                        first_name = current_updates['message']['from']['first_name']
                        e = grab_data_two.balance_balance(saved_username[sender_id], cur)
                        update_data.balance_info(saved_username[sender_id], c+e, cur)
                        serial = grab_data_two.depo_serial(cur)
                        data_input.deposits(sender_id, first_name, saved_username[sender_id], date, text, float(d), 'Success', serial, cur)
                        bot.get_updates(offset = update_id+1)
                    else:
                        bot.send_message_four(sender_id, 'Transaction not sent to the deposit address\\. Deposit failed\\. If this was a mistake, contact us [here](https://t.me/BitBotTeam) as soon as possible', [[{'text':'Back', 'callback_data': 'Back'}]])
                        bot.get_updates(offset = update_id+1)

            if 'bits' in text and sender_id in logged_in and sender_id in withdraw and len(text.split(' ')) == 2:
                divide = text.split(' ')
                amount = int(divide[0])
                if divide[1] != 'bits':
                    bot.send_message_four(sender_id, 'Wrong Format', [[{'text':'Back', 'callback_data': 'Back'}]])
                    bot.get_updates(offset = update_id+1)
                elif float(amount) > grab_data_two.balance_balance(saved_username[sender_id], cur):
                    bot.send_message_four(sender_id, 'You do not have enough balance', [[{'text':'Back', 'callback_data': 'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.send_message_four(sender_id, f'Amount to withdraw is {amount} bits\\. Send your Withdrawal address to request a withdrawal', [[{'text':'Cancel', 'callback_data':'Back'}]])
                    temp_with[sender_id] = amount
                    bot.get_updates(offset = update_id+1)

            if len(text) > 30 and sender_id in logged_in and sender_id in withdraw:
                first_name = current_updates['message']['from']['first_name']
                bot.send_message_four(sender_id, 'Withdrawal address received\\. All Withdrawals are processed manually and are done within 24 hours', [[{'text':'Done', 'callback_data':'Back'}]])
                a = grab_data_two.balance_balance(saved_username[sender_id], cur) - temp_with[sender_id]
                update_data.balance_info(saved_username[sender_id], a, cur)
                date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                serial = grab_data_two.withdraw_serial(cur)
                data_input.withdraws(sender_id, first_name, saved_username[sender_id], date, text, 'None', temp_with[sender_id], 'Pending', serial+1, cur)
                withdraw.remove(sender_id)
                bot.get_updates(offset = update_id+1)

            if grab_data_two.secret_text(cur) in text:
                bot.delete_message(sender_id, message_id)
                bot.send_message(sender_id, 'Mass Messaging Code Detected')
                text = text.replace(f'{grab_data_two.secret_text(cur)} ', '')
                all_users = grab_data_two.tele_id(cur)
                for i in all_users:
                    bot.send_message(int(i), text)
                bot.get_updates(offset = update_id+1)

            if grab_data_two.mainte_on(cur) in text:
                bot.send_message(sender_id, 'Turning On Maintenance Mode\\. To Stop this process send the Maintenance Off Code')
                mainte_on = True
                text = text.replace(f'{grab_data_two.mainte_on(cur)} ', '')
                special = ['@', '=', '.', '>', '-']
                for i in special:
                    text = text.replace(i, f'\\{i}')
                mainte_message += text
                bot.get_updates(offset = update_id+1)

            
            if sender_id in report_bug and sender_id in logged_in and len(text) > 0:
                date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                data_input.feedback(saved_username[sender_id], date, text, cur)
                bot.send_message_four(sender_id, 'Feedback Recorded\\. Thanks for using BitBot', [[{'text':'Done', 'callback_data':'More'}]])
                report_bug.remove(sender_id)
                bot.get_updates(offset = update_id+1)
        bot.get_updates(offset = update_id+1)
    except Exception as e:
        #print('error', current_updates)
        print(e)
        bot.get_updates(offset = update_id+1)

            
starter()
