import requests, json, random, string, time, datetime, mysql.connector
import grab_data, update_data, data_input, grab_data_two, delete_row, payout_demo, tree_tracking
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
        #print(send)
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

def time_splitter(time):
    b = time.split(' ')
    c = b[1][0:5]
    full_time = f'{b[0]} {c}'
    return full_time


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

def investment_num(investment):
    a = investment
    d = "%.2f" % a
    e = "{:,}".format(float(d))
    return e


conn = mysql.connector.connect(host='62.77.159.42',user='sakib3',database='bitbot',password='@&G6hdM@EZJKQu010au*jpIjs7EsB', autocommit=True)
cur = conn.cursor()

token = '1233921119:AAEodGL5mX6NAd84dDjQrAhOt03JNcRDIio'
offset = 0

asking_id = []
asking_pass = []
logged_in = []

loggin_in = [] #login
password_in = [] #login

summary_pass = []

id_number = {}

bot = BoilerPlate(token)

def starter():
    global offset, cur, conn
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
                #print('Edited')
                bot.get_updates(offset = update_id+1)


def bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, dict_checker, cur, callback_data=0, callback=False):
    try:
        if callback == True:
            print(callback_data)

            if callback_data == 'None':
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Back' and sender_id in logged_in:
                if sender_id in summary_pass:
                    summary_pass.remove(sender_id)
                bot.edit_message_two(group_id, message_id, '*BitBot Management Panel*', [[{'text':'My Manager Volume', 'callback_data':'Manager Volume'}],
                                                                                        [{'text':'My Clients', 'callback_data':'My Clients'}],
                                                                                        [{'text':'My Summary', 'callback_data':'My Summary'}],
                                                                                        [{'text':'Log Out', 'callback_data':'Log Out'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Manager Volume' and sender_id in logged_in:
                total_invest = 0
                total_payout = 0
                volume = 0
                amba = grab_data_two.ambato_username(id_number[sender_id], cur)
                all_clients = tree_tracking.all_refer(amba, cur)
                for i in all_clients:
                    stand = grab_data_two.hold_stand(i, cur)
                    promo = grab_data_two.hold_promo(i, cur)
                    payout = grab_data_two.payout_value(i, cur)
                    amba = grab_data_two.balance_amba(i, cur)
                    inte = grab_data_two.balance_inte(i, cur)
                    if promo == 'Nothing':
                        promo = 0
                    if stand == 'Nothing':
                        stand = 0
                    total_invest += promo + stand
                    total_payout += payout
                    volume += promo + stand - amba - inte
                bot.edit_message_two(group_id, message_id, 'Manager Volume', [[{'text':f'My Net Volume: {investment_num(volume)} bits', 'callback_data':'None'}],
                                                                            [{'text':f'Total Investment: {investment_num(total_invest)} bits', 'callback_data':'Total Investment'}],
                                                                            [{'text':f'Total Payouts: {investment_num(total_payout)} bits', 'callback_data':'Total Payouts'}],
                                                                            [{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)    

            elif callback_data == 'Total Payouts' and sender_id in logged_in:
                amba = grab_data_two.ambato_username(id_number[sender_id], cur)
                all_clients = tree_tracking.all_refer(amba, cur)
                full_text = 'Username \\| Investment \\| Value'
                total = 0
                if len(full_text) > 4000:
                    bot.send_message(sender_id, full_text)
                else:
                    for i in all_clients:
                        payout_details = grab_data_two.payout_everything(i, cur)
                        if payout_details == 'Nothing':
                            pass
                        else:
                            for h in payout_details:
                                value = str(h[2]).replace('.','\\.')
                                full_text += f'{h[0]}    {h[1]}    {value}\n'
                                total += h[2]
                total = investment_num(total)
                total = total.replace('.', '\\.')
                full_text += f'\nTotal Value {total} bits'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Manager Volume'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Total Investment' and sender_id in logged_in:
                all_pro = grab_data_two.pro_all(cur)
                amba = grab_data_two.ambato_username(id_number[sender_id], cur)
                all_clients = tree_tracking.all_refer(amba, cur)
                full_text = 'Username \\| Product \\| Amount \\| Value\n\n'
                total = 0
                if len(full_text) > 4000:
                    bot.send_message(sender_id, full_text)
                    full_text = ''
                else:
                    for i in all_clients:
                        holdings = grab_data_two.holding_holding(i, cur)
                        if holdings == 'Nothing' or holdings == None or len(holdings) == 0:
                            pass
                        else:
                            holdings = holdings.split(' ')
                            for h in range(len(holdings)):
                                if holdings[h] in all_pro:
                                    cost = grab_data_two.inve_price(holdings[h], cur)
                                    full_text += f'{i}    {holdings[h]}    {holdings[h+1]}    {int(cost)*int(holdings[h+1])}\n'
                                    total += int(int(cost)*int(holdings[h+1]))
                total = investment_num(total)
                total = total.replace('.', '\\.')
                full_text += f'\nTotal Value {total} bits'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Manager Volume'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'My Summary' and sender_id in logged_in:
                summary_pass.append(sender_id)
                bot.edit_message_two(group_id, message_id, 'Please enter your *Password*', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'My Clients' and sender_id in logged_in:
                amba = grab_data_two.ambato_username(id_number[sender_id], cur)
                all_clients = tree_tracking.all_refer(amba, cur)
                full_text = '*My Clients*\n\n'
                for i in all_clients:
                    if len(full_text) > 4000:
                        bot.send_message(sender_id, full_text)
                        full_text = ''
                    full_text += f'Username: {i}\n'
                full_text += 'Send Username \\+ client to get more details\n\nExample\nAsdf client\nDummy client'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Log Out' and sender_id in logged_in:
                logged_in.remove(sender_id)
                del id_number[sender_id]
                bot.send_message(sender_id, 'Please provide your *Username*')
                asking_id.append(sender_id)
                bot.get_updates(offset = update_id+1)

        else:
            text = current_updates['message']['text']
            print(text)

            if sender_id in logged_in and sender_id in summary_pass and text != grab_data_two.user_password(id_number[sender_id], cur):
                bot.send_message_four(sender_id, 'Incorrect *password*, please try again', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif sender_id in logged_in and sender_id in summary_pass and text == grab_data_two.user_password(id_number[sender_id], cur):
                amba = grab_data_two.ambato_username(id_number[sender_id], cur)
                all_clients = tree_tracking.all_refer(amba, cur)
                bot.delete_message(sender_id, message_id)
                total_invest = 0
                for i in all_clients:
                    stand = grab_data_two.hold_stand(i, cur)
                    promo = grab_data_two.hold_promo(i, cur)
                    if promo == 'Nothing':
                        promo = 0
                    if stand == 'Nothing':
                        stand = 0
                    total_invest += promo + stand
                bot.send_message_four(sender_id, f'Manager ID: {id_number[sender_id]}\nPassword: {text}\nAmbassador Code: {amba}\nTotal Holdings: {int(total_invest)} bits\nClients: {len(all_clients)}', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            if text == '/start' and sender_id not in logged_in:
                bot.send_message(sender_id, 'Please provide your *Username*')
                if sender_id not in loggin_in:
                    loggin_in.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif text == '/start' and sender_id in logged_in:
                if sender_id in summary_pass:
                    summary_pass.remove(sender_id)
                bot.send_message_four(sender_id, '*BitBot Management Panel*', [[{'text':'My Manager Volume', 'callback_data':'Manager Volume'}],
                                                                                        [{'text':'My Clients', 'callback_data':'My Clients'}],
                                                                                        [{'text':'Log Out', 'callback_data':'Log Out'}]])
                bot.get_updates(offset = update_id+1)

            elif sender_id in loggin_in and grab_data_two.user_username(text, cur)[0] == 'Nothing':
                bot.send_message(sender_id, 'Please provide a valid *Username*')
                bot.get_updates(offset = update_id+1)

            elif sender_id in loggin_in and text in grab_data_two.user_username(text, cur)[0] and grab_data_two.manager_access(text, cur) == 'NO':
                bot.send_message(sender_id, 'You do not have the access')
                bot.get_updates(offset = update_id+1)

            elif sender_id in loggin_in and text in grab_data_two.user_username(text, cur)[0] and grab_data_two.manager_access(text, cur) == 'YES':
                id_number[sender_id] = text
                bot.send_message(sender_id, 'Please enter your *Password*')
                loggin_in.remove(sender_id)
                if sender_id not in password_in:
                    password_in.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in password_in and text != grab_data_two.user_password(id_number[sender_id], cur):
                bot.send_message(sender_id, 'Incorrect password, please try again')
                bot.get_updates(offset = update_id+1)

            elif sender_id in password_in and sender_id not in summary_pass and text == grab_data_two.user_password(id_number[sender_id], cur) and grab_data_two.manager_access(id_number[sender_id], cur) == 'YES':
                bot.send_message(sender_id, 'Access Granted')
                bot.delete_message(sender_id, message_id)
                logged_in.append(sender_id)
                bot.send_message_four(sender_id, '*BitBot Management Panel*', [[{'text':'My Manager Volume', 'callback_data':'Manager Volume'}],
                                                                                        [{'text':'My Clients', 'callback_data':'My Clients'}],
                                                                                        [{'text':'My Summary', 'callback_data':'My Summary'}],
                                                                                        [{'text':'Log Out', 'callback_data':'Log Out'}]])
                bot.get_updates(offset = update_id+1)

            if 'client' in text and len(text.split(' ')) == 2 and sender_id in logged_in:
                details = text.split(' ')
                amba = grab_data_two.ambato_username(id_number[sender_id], cur)
                all_clients = tree_tracking.all_refer(amba, cur)
                if details[0] == 'client':
                    pass
                elif details[0] in all_clients:
                    data = grab_data_two.user_user(details[0], cur)
                    promo = grab_data_two.hold_promo(details[0], cur)
                    stand = grab_data_two.hold_stand(details[0], cur)
                    down = tree_tracking.down(details[0], cur)
                    date = data[6].replace('-', '\\-')
                    bot.send_message_four(sender_id, f'Username: {data[2]}\nDate of Registration: {date}\nAmbassador Code: {data[4]}\nDown Volume: {int(down)}\nHoldings: {int(promo)+int(stand)}', [[{'text':'Back','callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
    except Exception as e:
        #print(current_updates)
        print(e)
        bot.get_updates(offset = update_id+1)

starter()
