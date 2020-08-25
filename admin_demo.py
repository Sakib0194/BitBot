#!/usr/bin/env python3
import requests, json, random, string, time, datetime, mysql.connector
import update_data, data_input, grab_data_two, delete_row, payout_demo, tree_tracking
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


token = '1371918305:AAG2p4z5aYJ1VNAWq9CGcnXKDZH-64Yq6sM'
offset = 0

conn = mysql.connector.connect(host='62.77.159.42',user='sakib3',database='bitbot',password='@&G6hdM@EZJKQu010au*jpIjs7EsB', autocommit=True)
cur = conn.cursor()

gene_pass = {}
gene_amba = {}
create_user = []


mana_id = {}
mana_pass = {}
create_manager = []


asking_id = []
asking_pass = []
logged_in = [1211908888, 468930122]

id_number = {}

credit_acc = []
credit_acc_two = {}
debit_acc = []
debit_acc_two = {}

delete_user = {}
payout_pen = {} #When sending payout to store data
product_name = {} #When sending payout to store pruduct name

residual = {}#when sending residual

create_inve = []
inve_create = []
inve_category = {}
inve_type = {}
inve_name = {}
inve_payout = {}
inve_paydate = {}
inve_cost = {}

create_admin = []
admin_user = {}

add_payout = []
payout_pro = {}

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
                #print('Edited')
                bot.get_updates(offset = update_id+1)


def bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, dict_checker, cur, callback_data=0, callback=False):
    try:
        if callback == True:
            if sender_id not in logged_in:
                bot.send_message(sender_id, 'Please provide your *ID*')
                if sender_id not in asking_id:
                    asking_id.append(sender_id)
                bot.get_updates(offset = update_id+1)
            print(callback_data)
            if callback_data == 'None':
                bot.get_updates(offset = update_id+1)

            if callback_data == 'General Ledger' and sender_id in logged_in:
                if sender_id in payout_pen:
                    del payout_pen[sender_id]
                if sender_id in product_name:
                    del product_name[sender_id]
                if residual != {}:
                    residual.clear()
                dep = float(grab_data_two.dep_total(cur))
                withdraw = float(grab_data_two.with_total(cur))
                amba = float(grab_data_two.all_ambabala(cur))
                inte = float(grab_data_two.all_intebala(cur))
                inve = float(grab_data_two.all_inve(cur))
                payout = float(grab_data_two.all_payout(cur))
                pen_with = float(grab_data_two.pen_withdraw(cur))
                bot.edit_message_two(group_id, message_id, '*General Ledger*', [[{'text':f'Net Balance: {investment_num(dep - withdraw)} bits', 'callback_data':'None'}], 
                                                                                [{'text':f'Net Value: {investment_num(dep-withdraw-amba-inte)}  bits', 'callback_data':'Total Payouts'}],
                                                                                [{'text':f'Total Investment: {investment_num(inve)} bits', 'callback_data':'None'}],
                                                                                [{'text':f'Total Deposits: {investment_num(dep)} bits', 'callback_data':'Total Deposits'}],
                                                                                [{'text':f'Total Payouts: {investment_num(payout)} bits', 'callback_data':'Total Payouts'}],
                                                                                [{'text':f'Total Withdrawals: {investment_num(withdraw)} bits', 'callback_data':'Total Withdrawals'}], 
                                                                                [{'text':f'Pending Withdrawals: {investment_num(pen_with)} bits', 'callback_data':'Manage Withdrawals'}],
                                                                                [{'text':'Pending Payouts', 'callback_data':'Manage Payouts'}],
                                                                                [{'text':'Pending Residual', 'callback_data':'Manage Residual'}],
                                                                                [{'text':'Back', 'callback_data': 'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Manage Payouts' and sender_id in logged_in:
                pending = grab_data_two.descri_pending(cur)
                if pending == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'No payout is pending', [[{'text':'Back', 'callback_data': 'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    full_code = []
                    for a in pending:
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
                        part.append([{'text':'Back','callback_data':'General Ledger'}])
                    bot.edit_message_two(group_id, message_id, '*Select a Investment to send Payout*', part)
                    bot.get_updates(offset = update_id+1)

            elif callback_data in grab_data_two.descri_pending(cur) and sender_id in logged_in:
                data = payout_demo.details(callback_data, cur)
                if data == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'No one is holding any product of this category', [[{'text':'Back', 'callback_data': 'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    pay_rate = float(grab_data_two.pay_rate(callback_data, cur))
                    full_text = ''
                    total = 0
                    rate = str(pay_rate).replace('.','\\.')
                    full_text += f'Payout Rate: {rate}\n\n'
                    pending = {}
                    for i in data:
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        interest = float(data[i]) * float(pay_rate)/100
                        d = "%.2f" % interest
                        e = investment_num(float(d))
                        inte = str(e).replace('.', '\\.')
                        full_text += f'{i} is to get {inte} bits payout\n'
                        total += interest
                        pending[i] = float(d)
                    payout_pen[sender_id] = pending
                    product_name[sender_id] = callback_data
                    tot = investment_num(float(total))
                    tot = str(tot).replace('.', '\\.')
                    full_text += f'\nTotal Payout to send: {(tot)} bits'
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Confirm', 'callback_data': 'Confirm Payout'}],
                                                                            [{'text':'Cancel', 'callback_data': 'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'Confirm Payout' and sender_id in logged_in:
                data = payout_pen[sender_id]
                product = product_name[sender_id]
                for i in data:
                    invest_bala = float(grab_data_two.inve_bala(i, cur))
                    inte_bala = float(grab_data_two.balance_inte(i, cur))
                    update_data.balance_info(i, invest_bala+float(data[i]), cur)
                    update_data.balance_interest(i, inte_bala+float(data[i]), cur)
                    serial = grab_data_two.payout_serial(cur)
                    data_input.payout_transaction(i, product, float(data[i]), serial, cur)
                del payout_pen[sender_id]
                update_data.payout_pending(product, cur)
                bot.edit_message_two(group_id, message_id, 'Payout successfully sent', [[{'text':'Back', 'callback_data': 'General Ledger'}]])
                bot.get_updates(offset = update_id+1)
                
            elif callback_data == 'Manage Residual' and sender_id in logged_in:
                all_users = grab_data_two.user_all(cur)
                sorted_data = {}
                for i in all_users:
                    tree_tracking.qualified_mile(i[0], cur)
                    tree_tracking.qualified_resi(i[0], cur)
                    tree_tracking.resi_per(i[0], cur)
                    resi = grab_data_two.quali_resi(i[0], cur)
                    for h in resi:
                        if h[0] == 'Vito':
                            pass
                        elif h[1] == 0 or h[1] == 1:
                            pass
                        elif h[2] == 0:
                            pass
                        else:
                            sorted_data[h[0]] = h[1]
                full_text = ''
                if sorted_data == {}:
                    bot.edit_message_two(group_id, message_id, 'Nothing is pending', [[{'text':'Back', 'callback_data': 'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    for i in sorted_data:
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        tree = grab_data_two.amba_tree(i, cur)
                        promo = int(grab_data_two.hold_promo(i, cur))
                        stand = int(grab_data_two.hold_stand(i, cur))
                        num = investment_num(float(tree+stand+promo)).replace('.','\\.')
                        calculated = investment_num(((tree+promo+stand)*int(sorted_data[i])/100)).replace('.','\\.')
                        full_text += f'{i} is to get {sorted_data[i]}\\% and {calculated} bits Residual on {num} bits\n\n'
                        residual[i] = (tree+promo+stand)*int(sorted_data[i])/100
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Confirm', 'callback_data': 'Confirm Residual'}],
                                                                                [{'text':'Cancel', 'callback_data': 'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'Confirm Residual' and sender_id in logged_in:
                for i in residual:
                    balance = grab_data_two.balance_balance(i, cur)
                    amba = grab_data_two.balance_amba(i, cur)
                    update_data.balance_info(i, residual[i]+balance, cur)
                    update_data.balance_amba(i, residual[i]+amba, cur)
                    serial = grab_data_two.amba_serial(cur)
                    data_input.ambassador_transactions(i, 'Residual', residual[i], 'Ambassador Residual Bonus', serial, cur)
                residual.clear()
                bot.edit_message_two(group_id, message_id, 'Residual Successfully Sent', [[{'text':'Done', 'callback_data': 'General Ledger'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Total Deposits' and sender_id in logged_in:
                full_text = ''
                grabbing = grab_data_two.deposits(cur)
                i = len(grabbing[0])
                for d in range(i):
                    if len(full_text) > 3800:
                        bot.send_message(sender_id, full_text)
                        full_text = ''
                    tim = time_splitter(grabbing[2][d]).replace("-", "\\-")
                    bala = str(grabbing[0][d]).replace(".", "\\.")
                    name = str(grabbing[1][d]).replace(".", "\\.")
                    full_text += f'{name} deposited {bala} bits on {tim}\n\n'
                dep = 0
                for g in grabbing[0]:
                    dep += float(g)
                depo = str(dep).replace(".", "\\.")
                full_text += f'Total Deposit {str(depo)} bits'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'General Ledger'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Total Payouts' and sender_id in logged_in:
                all_trans = grab_data_two.payout_alltrans(cur)
                if grab_data_two == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'Nothing to show here', [[{'text':'Back', 'callback_data': 'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    full_text = ''
                    for i in all_trans:
                        if len(full_text) > 4000:
                            bot.send_message(sender_id, full_text)
                            full_text = ''
                        amount = str(i[2]).replace('.', '\\.')
                        full_text += f'Username: {i[0]} \\| Investment: {i[1]} \\| Amount: {amount}\n'
                    bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data': 'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)

            elif callback_data == 'Total Withdrawals' and sender_id in logged_in:
                full_text = ''
                grabbing = grab_data_two.withdraws(cur)
                i = len(grabbing[0])
                for d in range(i):
                    if len(full_text) > 3800:
                        bot.send_message(sender_id, full_text)
                        full_text = ''
                    tim = time_splitter(grabbing[1][d]).replace("-", "\\-")
                    bala = str(grabbing[2][d]).replace(".", "\\.")
                    name = str(grabbing[0][d]).replace(".", "\\.")
                    full_text += f'{name} requested withdrawal of {bala} bits on {tim}\n\n'
                dep = 0
                for g in grabbing[2]:
                    dep += float(g)
                depo = str(dep).replace(".", "\\.")
                full_text += f'Total Withdraws {str(depo)} bits'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'General Ledger'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Manage Withdrawals' and sender_id in logged_in:
                if grab_data_two.with_status(cur)[0][0] == 'Pending':
                    pending_amount = len(grab_data_two.with_status(cur))
                    serials = grab_data_two.with_serial(cur)
                    pending_serials = ''
                    for i in range(pending_amount):
                        pending_serials += f'{str(serials[i][0])} '
                    bot.edit_message_two(group_id, message_id, f'Total Pending Withdrawals: {pending_amount}\nPending Withdrawal Serials: {pending_serials}\n\nEnter a Serial Number \\+ withdraw to get full details\n\nEnter Serial Number \\+ TX Hash to Complete a withdrawal\n\nexample\n57 withdraw\n91 64\\-length\\-TX\\-hash', [[{'text':'Back', 'callback_data':'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.edit_message_two(group_id, message_id, 'No Withdrawal is Pending', [[{'text':'Back', 'callback_data':'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)

            if callback_data == 'Back':
                if sender_id in credit_acc:
                    credit_acc.remove(sender_id)
                if sender_id in debit_acc:
                    debit_acc.remove(sender_id)
                if sender_id in credit_acc_two:
                    del credit_acc_two[sender_id]
                if sender_id in debit_acc_two:
                    del debit_acc_two[sender_id]
                bot.edit_message_two(group_id, message_id, '*BitBot Company Panel*', [
                                                                        [{'text':'General Ledger', 'callback_data':'General Ledger'}], 
                                                                        [{'text':'Managers', 'callback_data':'Managers'}],
                                                                        [{'text':'Clients', 'callback_data':'Client'}],
                                                                        [{'text':'Investments', 'callback_data':'Investments'}],
                                                                        [{'text':'Tools', 'callback_data':'Tools'}],
                                                                        [{'text':'Log Out', 'callback_data':'Log Out'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Investments' and sender_id in logged_in:
                if sender_id in inve_category:
                    del inve_category[sender_id]
                if sender_id in inve_type:
                    del inve_type[sender_id]
                if sender_id in inve_name:
                    del inve_name[sender_id]
                if sender_id in inve_payout:
                    del inve_payout[sender_id]
                if sender_id in inve_cost:
                    del inve_cost[sender_id]
                if sender_id in create_inve:
                    create_inve.remove(sender_id)
                if sender_id in inve_create:
                    inve_create.remove(sender_id)
                if sender_id in payout_pro:
                    del payout_pro[sender_id]
                if sender_id in add_payout:
                    add_payout.remove(sender_id)
                bot.edit_message_two(group_id, message_id, 'Investments', [[{'text':'Active Investments', 'callback_data':'Active Investments'}],
                                                                        [{'text':'Create New Investment', 'callback_data':'New Investment'}],
                                                                        [{'text':'Add Payout Time', 'callback_data':'Payout Time'}],
                                                                        [{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Active Investments' and sender_id in logged_in:
                all_pro = grab_data_two.all_products(cur)
                full_text = ''
                for i in all_pro:
                    if len(full_text) > 4000:
                        bot.send_message(sender_id, full_text)
                        full_text = ''
                    full_text += f'Product:{i[0]} \\| Time Sold: {i[1]}\n\n'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Investments'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'New Investment' and sender_id in logged_in:
                categories = grab_data_two.inve_cate_two(cur)
                full_text = 'Type a Category name to add a new Investment\\. If the category is not listed, type a new Category to begin\nAvailable Categories\n'
                for i in categories:
                    full_text += f'{i}\n'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Investments'}]])
                create_inve.append(sender_id)
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Payout Time' and sender_id in logged_in:
                pending = grab_data_two.payout_time(cur)
                full_code = []
                for a in pending:
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
                    part.append([{'text':'Back','callback_data':'Investments'}])
                add_payout.append(sender_id)
                bot.edit_message_two(group_id, message_id, 'Select an Investment where Payout Time is missing', part)
                bot.get_updates(offset = update_id+1)

            elif callback_data in grab_data_two.payout_time(cur) and sender_id in add_payout and sender_id in logged_in:
                payout_pro[sender_id] = callback_data
                bot.edit_message_two(group_id, message_id, f'{callback_data} Payout is currently sent every 0 days\\. Send after how many days payout would be available to be sent\n\nExample\nIf you want X Product to be available for payout everey 30 days, send 30, if every 3 months, send 90', [[{'text':'Back', 'callback_data':'Investments'}]])
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Confirm Delete' and sender_id in logged_in:
                delete_row.user_info(delete_user[sender_id])
                bot.edit_message_two(group_id, message_id, f'{delete_user[sender_id]} has been deleted', [[{'text':'Back', 'callback_data':'Tools'}]])
                del delete_user[sender_id]
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Client' and sender_id in logged_in:
                full_text = ''
                grabbing = grab_data_two.user_all(cur)
                i = len(grabbing)
                for d in range(i):
                    if len(full_text) > 4000:
                        bot.send_message(sender_id, full_text)
                        full_text = ''
                    full_text += f'Username: {grabbing[d][0]}\n'
                full_text += 'End of List\n\nType a Username \\+ client to get full details of a user\n\nexample\nSakib0194 client'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)
            
            if callback_data == 'Managers' and sender_id in logged_in:
                full_text = ''
                grabbing = grab_data_two.manage(cur)
                i = len(grabbing)
                for d in range(i):
                    if len(full_text) > 4000:
                        bot.send_message(sender_id, full_text)
                        full_text = ''
                    full_text += f'Manager Username: {grabbing[d]}\n'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            
            if callback_data == 'Log Out' and sender_id in logged_in:
                bot.send_message(sender_id, 'Logged Out')
                bot.send_message(sender_id, 'Please Provide your *ID*')
                if sender_id not in asking_id:
                    asking_id.append(sender_id)
                logged_in.remove(sender_id)
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Tools' and sender_id in logged_in:
                if sender_id in gene_amba:
                    del gene_amba[sender_id]
                if sender_id in gene_pass:
                    del gene_pass[sender_id]
                if sender_id in create_user:
                    create_user.remove(sender_id)
                if sender_id in create_manager:
                    create_manager.remove(sender_id)
                if sender_id in mana_id:
                    del mana_id[sender_id]
                if sender_id in mana_pass:
                    del mana_pass[sender_id]
                if sender_id in delete_user:
                    del delete_user[sender_id]
                if sender_id in create_admin:
                    create_admin.remove(sender_id)
                if sender_id in admin_user:
                    del admin_user[sender_id]
                bot.edit_message_two(group_id, message_id, '*Admin Tools*', [[{'text':'Create Client', 'callback_data':'Create User'}], 
                                                                    [{'text':'Create Manager Admin', 'callback_data':'Create Manager Admin'}], 
                                                                    [{'text':'Credit An Account', 'callback_data':'Credit Account'}],
                                                                    [{'text':'Debit An Account', 'callback_data':'Debit Account'}],
                                                                    [{'text':'Password Reset', 'callback_data':'Password Reset'}],
                                                                    [{'text':'Delete Account', 'callback_data':'Delete Account'}],
                                                                    [{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Credit Account' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Enter a Client Username', [[{'text':'Back', 'callback_data':'Back'}]])
                credit_acc.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Debit Account' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Enter a Client Username', [[{'text':'Back', 'callback_data':'Back'}]])
                debit_acc.append(sender_id)
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Create Manager Admin' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Select an Option', [[{'text':'Create Admin', 'callback_data':'Create Manager'}],
                                                                                [{'text':'Create Manager', 'callback_data':'Create Admin'}],
                                                                                [{'text':'Back', 'callback_data':'Tools'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Password Reset' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Enter a Client Username \\+ reset to get a new password\n\nExample\nSakib0194 reset', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Delete Account' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Enter a Client Username \\+ delete to delete an account\\.\n\nExample\nSakib0194 delete', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Create User' and sender_id in logged_in:
                code = generate_pass()
                passw = code[0]
                amba_code = code[1]
                while passw in grab_data_two.user_password(passw, cur)[0] or amba_code in grab_data_two.user_amba(amba_code, cur)[0]:
                    code = generate_pass()
                    passw = code[0]
                    amba_code = code[1]
                gene_pass[sender_id] = passw
                gene_amba[sender_id] = amba_code
                bot.edit_message_two(group_id, message_id, f'Generated Password: {passw}\nGenerated Ambassador Code: {amba_code}\n\nInsert the Required Credential sequentially following with a space\n\nTelegram ID None if not available\nFirst Name one word only, None if not available\nDAM Username One Word\nEnter your Ambassador Code\nTelegram Username None if not available\n\nexample of the message\nNone Hawl Snake53 LVXD4A8 Hawl754', [[{'text':'Back', 'callback_data':'Tools'}]])
                if sender_id not in create_user:
                    create_user.append(sender_id)
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Create Admin' and sender_id in logged_in:
                create_admin.append(sender_id)
                bot.edit_message_two(group_id, message_id, 'Enter the Username of the account to Promote', [[{'text':'Back', 'callback_data':'Tools'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Create Manager' and sender_id in logged_in:
                code = generate_pass()
                passw = code[0]
                amba_code = code[1]
                while passw in grab_data_two.all_manapass(cur) or amba_code in grab_data_two.all_id(cur):
                    code = generate_pass()
                    passw = code[0]
                    amba_code = code[1]
                mana_id[sender_id] = passw
                mana_pass[sender_id] = amba_code
                bot.edit_message_two(group_id, message_id, f'Generated ID: {amba_code}\nGenerated Password: {passw}\n\nInsert the Required Credential sequentially following with a space\n\nTelegram ID None if not available\nFirst Name one word only, None if not available\nSpecial Access YES or NO only, only uppercase letter\nUsername from Client Bot\nAmbassador Code from Client Bot\n\nexample of the message\n468930122 Ruth NO Vito LVXD4A8', [[{'text':'Back', 'callback_data':'Tools'}]])
                if sender_id not in create_manager:
                    create_manager.append(sender_id)
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Confirm Admin' and sender_id in logged_in:
                update_data.manager_access(admin_user[sender_id], cur)
                bot.edit_message_two(group_id, message_id, f'{admin_user[sender_id]} has been promoted to Manager', [[{'text':'Back', 'callback_data':'Tools'}]])
                bot.get_updates(offset = update_id+1)
            
            if callback_data == 'Cancel':
                if sender_id in gene_amba:
                    del gene_amba[sender_id]
                if sender_id in gene_pass:
                    del gene_pass[sender_id]
                if sender_id in create_user:
                    create_user.remove(sender_id)
                if sender_id in create_manager:
                    create_manager.remove(sender_id)
                if sender_id in mana_id:
                    del mana_id[sender_id]
                if sender_id in mana_pass:
                    del mana_pass[sender_id]
                bot.edit_message_two(group_id, message_id, '*Tools*', [[{'text':'Create Client', 'callback_data':'Create User'}], 
                                                                    [{'text':'Create Manager', 'callback_data':'Create Manager'}], 
                                                                    [{'text':'Credit An Account', 'callback_data':'Credit Account'}],
                                                                    [{'text':'Debit An Account', 'callback_data':'Debit Account'}],
                                                                    [{'text':'Password Reset', 'callback_data':'Password Reset'}],
                                                                    [{'text':'Delete Account', 'callback_data':'Delete Account'}],
                                                                    [{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

        else:
            text = current_updates['message']['text']
            print(text)
            if sender_id not in logged_in:
                if sender_id not in asking_id and sender_id not in asking_pass:
                    bot.send_message(sender_id, 'Please provide your *ID*')
                    if sender_id not in asking_id:
                        asking_id.append(sender_id)
                    bot.get_updates(offset = update_id+1)
            if text == '/start' and sender_id in logged_in:
                bot.send_message_four(sender_id, '*BitBot Company Panel*', [
                                                                        [{'text':'General Ledger', 'callback_data':'General Ledger'}], 
                                                                        [{'text':'Managers', 'callback_data':'Managers'}],
                                                                        [{'text':'Clients', 'callback_data':'Client'}],
                                                                        [{'text':'Investments', 'callback_data':'Investments'}],
                                                                        [{'text':'Tools', 'callback_data':'Tools'}],
                                                                        [{'text':'Log Out', 'callback_data':'Log Out'}]])
                bot.get_updates(offset = update_id+1)

            if text == '/start' and sender_id not in logged_in:
                bot.send_message(sender_id, 'Please provide your *ID*')
                if sender_id not in asking_id:
                    asking_id.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in asking_id and grab_data_two.mana_id(text, cur)[0] == 'Nothing':
                bot.send_message(sender_id, 'Please provide a valid *ID*')
                bot.get_updates(offset = update_id+1)

            elif sender_id in asking_id and text in grab_data_two.mana_id(text, cur)[0]:
                bot.send_message(sender_id, 'Please provide your *password*')
                id_number[sender_id] = text
                asking_id.remove(sender_id)
                asking_pass.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in asking_pass and text != grab_data_two.mana_password(id_number[sender_id], cur):
                bot.send_message(sender_id, 'Incorrect *password*, please try again')
                bot.get_updates(offset = update_id+1)

            elif sender_id in asking_pass and text == grab_data_two.mana_password(id_number[sender_id], cur) and grab_data_two.mana_access(id_number[sender_id], cur) == 'YES':
                bot.send_message(sender_id, 'Access Granted')
                bot.delete_message(sender_id, message_id)
                bot.send_message_four(sender_id, '*BitBot Company Panel*', [
                                                                        [{'text':'General Ledger', 'callback_data':'General Ledger'}], 
                                                                        [{'text':'Managers', 'callback_data':'Managers'}],
                                                                        [{'text':'Clients', 'callback_data':'Client'}],
                                                                        [{'text':'Investments', 'callback_data':'Investments'}],
                                                                        [{'text':'Tools', 'callback_data':'Tools'}],
                                                                        [{'text':'Log Out', 'callback_data':'Log Out'}]])
                asking_pass.remove(sender_id)
                logged_in.append(sender_id)
                bot.get_updates(offset = update_id+1)

            if sender_id in create_user and len(text.split(' ')) == 5 and sender_id in logged_in:
                bot.send_message(sender_id, 'Details detected, creating user')
                a = text.split(' ')
                if a[2] == grab_data_two.user_username(a[2], cur)[0][0]:
                    bot.send_message_four(sender_id, 'Username already exist\\! Try again', [[{'text':'Back', 'callback_data':'Cancel'}]])
                    bot.get_updates(offset = update_id+1)
                elif a[2] != grab_data_two.user_username(a[2], cur)[0][0]:
                    ref = grab_data_two.amba_users(a[4], cur)
                    refer_number = ref + 1
                    data_input.user_info(a[0], a[1], a[2], gene_pass[sender_id], gene_amba[sender_id], a[3],time_splitter(str(datetime.datetime.fromtimestamp(time.time()))), a[4], cur)
                    data_input.balance_info(a[0], a[1], a[2], 0,0,0, cur)
                    data_input.amba_info(a[0], a[1], a[2], gene_amba[sender_id], a[3], 0, cur)
                    update_data.amba_info(a[3], refer_number, cur)
                    manager = tree_tracking.up(a[2], cur)
                    update_data.manager(a[2], manager, cur)
                    if grab_data_two.holding_user(a[2], cur) == 'No':
                        data_input.investment_holding(a[2], 0,0, 'Nothing', cur)
                    data_input.milestone_bonus(a[2], cur)
                    bot.send_message_four(sender_id, f'User Successfully Created\\.\nUsername: {a[2]}\nPassword: {gene_pass[sender_id]}\nAmbassador Code: {gene_amba[sender_id]}', [[{'text':'Back', 'callback_data':'Tools'}]])
                    bot.get_updates(offset = update_id+1)

            elif sender_id in create_user and len(text.split(' ')) < 5 or sender_id in create_user and len(text.split(' ')) > 5 and sender_id in logged_in:
                bot.send_message_four(sender_id, 'Details Missing or too many keywords\\. Try again', [[{'text':'Back', 'callback_data':'Tools'}]])
                bot.get_updates(offset = update_id+1)
            
            if sender_id in create_manager and len(text.split(' ')) == 5 and sender_id in logged_in:
                bot.send_message(sender_id, 'Details detected, creating manager')
                a = text.split(' ')
                for b in a:
                    print(b)
                if a[2] == 'YES' or a[2] == 'NO':
                    date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                    data_input.managers(a[0], a[1], date, mana_pass[sender_id], mana_id[sender_id], a[2],a[3], a[4], cur)
                    bot.send_message_four(sender_id, f'Manager Successfully Created\nManager ID: {mana_id[sender_id]}\nManager Password: {mana_pass[sender_id]}', [[{'text':'Back', 'callback_data':'Cancel'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.send_message_four(sender_id, 'Wrong Format\\. Type YES or NO in uppercase letters\\. Try again', [[{'text':'Back', 'callback_data':'Tools'}]])
                    bot.get_updates(offset = update_id+1)

            elif sender_id in create_manager and len(text.split(' ')) > 5 or sender_id in create_manager and len(text.split(' ')) < 5:
                bot.send_message_four(sender_id, 'Details Missing or too many keywords\\. Try again', [[{'text':'Back', 'callback_data':'Tools'}]])
                bot.get_updates(offset = update_id+1)
            
            if 'client' in text and len(text.split(' ')) == 2 and sender_id in logged_in:
                b = text.split(' ')
                bot.send_message(sender_id, 'Fetching Details')
                if b[1] != 'client':
                    bot.send_message_four(sender_id, 'Wrong Format\\. Try again', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    a=grab_data_two.user_user(b[0], cur)
                    if a == 'Nothing':
                        bot.send_message_four(sender_id, 'Username not found', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)
                    else:
                        tim = a[6]
                        time_two = tim.replace("-", "\\-")
                        name = a[1]
                        if "-" in name:
                            name = name.replace("-", "\\-")
                        full_text = f'Telgram ID: {a[0]}\nFirst Name: {name}\nUsername: {a[2]}\nPassword: {a[3]}\nAmbassador ID: {a[4]}\nAmbassador ID Used: {a[5]}\nTime Joined: {time_two}\nTelgram Username: {a[7]}'
                        bot.send_message_four(sender_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)
            
            if 'manager' in text and len(text.split(' ')) == 2 and sender_id in logged_in:
                b = text.split(' ')
                bot.send_message(sender_id, 'Fetching Details')
                if b[1] != 'manager':
                    bot.send_message_four(sender_id, 'Wrong Format\\. Try again', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    a=grab_data_two.mana_mana(b[0], cur)
                    if a == 'Nothing':
                        bot.send_message_four(sender_id, 'ID not found', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)
                    else:
                        tim = a[2]
                        time_two = tim.replace("-", "\\-")
                        full_text = f'Telgram ID: {a[0]}\nFirst Name: {a[1]}\nJoining Date: {time_two}\nID Number: {a[3]}\nPassword: {a[4]}\nSpecial Access {a[5]}\nUsername: {a[6]}\nAmbassador Code: {a[7]}'
                        bot.send_message_four(sender_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)

            if sender_id in debit_acc and sender_id in logged_in and len(text) > 2:
                bot.send_message(sender_id, 'Checking Username validity')
                validity = grab_data_two.user_username(text, cur)
                if validity[0] != 'Nothing':
                    balance = int(grab_data_two.inve_bala(text, cur))
                    bot.send_message_four(sender_id, f'User Current Balance: {balance} bits\\. Enter the amount of bits to debit', [[{'text':'Back', 'callback_data':'Back'}]])
                    debit_acc.remove(sender_id)
                    debit_acc_two[sender_id] = text
                    bot.get_updates(offset = update_id+1)
                elif validity[0] == 'Nothing':
                    bot.send_message_four(sender_id, 'Username Not Found', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)

            if sender_id in debit_acc_two and sender_id in logged_in and text.isnumeric():
                bot.send_message(sender_id, 'Updating Balance')
                balance = float(grab_data_two.inve_bala(debit_acc_two[sender_id], cur))
                to_add = balance - int(text)
                date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                update_data.balance_info(debit_acc_two[sender_id], to_add, cur)
                serial = grab_data_two.withdraw_serial(cur)
                data_input.withdraws('Admin', 'None', debit_acc_two[sender_id], date, 'Debited By Admin','Debited By Admin', text, 'CONFIRMED', serial+1, cur)
                bot.send_message_four(sender_id, 'Balance Successfully Debited', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            if sender_id in credit_acc and sender_id in logged_in and len(text) > 2:
                bot.send_message(sender_id, 'Checking Username validity')
                validity = grab_data_two.user_username(text, cur)
                if validity[0] != 'Nothing':
                    balance = int(grab_data_two.inve_bala(text, cur))
                    bot.send_message_four(sender_id, f'User Current Balance: {balance} bits\\. Enter the amount of bits to credit', [[{'text':'Back', 'callback_data':'Back'}]])
                    credit_acc.remove(sender_id)
                    credit_acc_two[sender_id] = text
                    bot.get_updates(offset = update_id+1)
                elif validity[0] == 'Nothing':
                    bot.send_message_four(sender_id, 'Username Not Found', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)

            if sender_id in credit_acc_two and sender_id in logged_in and text.isnumeric():
                bot.send_message(sender_id, 'Updating Balance')
                balance = float(grab_data_two.inve_bala(credit_acc_two[sender_id], cur))
                to_add = balance + int(text)
                date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                update_data.balance_info(credit_acc_two[sender_id], to_add, cur)
                serial = grab_data_two.depo_serial(cur)
                data_input.deposits('Admin', 'None', credit_acc_two[sender_id], date, 'Credited By Admin', float(text), 'Success', serial, cur)
                bot.send_message_four(sender_id, 'Balance Successfully Credited', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            if sender_id in create_inve and sender_id in logged_in:
                types = grab_data_two.inve_cate(text, cur)
                if types == []:
                    bot.send_message_four(sender_id, 'Category Name do not exist\\. Creating new category\n\nInput a new Invesment Type name', [[{'text':'Back', 'callback_data':'Investments'}]])
                    inve_category[sender_id] = text
                    create_inve.remove(sender_id)
                    bot.get_updates(offset = update_id+1)
                else:
                    full_text = 'Category Exist\\. Enter an existing or a new invesment type\\. Current Investment Types\n\n'
                    for i in types:
                        full_text += f'{i}\n'
                    inve_category[sender_id] = text
                    create_inve.remove(sender_id)
                    bot.send_message_four(sender_id, full_text, [[{'text':'Back', 'callback_data':'Investments'}]])
                    bot.get_updates(offset = update_id+1)

            elif sender_id in inve_category and sender_id not in inve_type and sender_id not in inve_name and sender_id in logged_in:
                types = grab_data_two.inve_type(text, cur)
                if types == []:
                    inve_type[sender_id] = text
                    bot.send_message_four(sender_id, 'Investment Type do no exist\\. Creating new type\n\nInput a new investment name', [[{'text':'Back', 'callback_data':'Investments'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    full_text = 'Investment type exist\\. Enter an existing or a new invesment product name\\. Product name must be unique\\. First Letter of a Promotional Investments product must be P\\. Current Investment Products\n\n'
                    products = grab_data_two.inve_products(text, cur)
                    for i in products:
                        full_text += f'{i[0]}\n'
                    inve_type[sender_id] = text
                    bot.send_message_four(sender_id, full_text, [[{'text':'Back', 'callback_data':'Investments'}]])
                    bot.get_updates(offset = update_id+1)
            
            elif sender_id in inve_type and sender_id in inve_category and sender_id not in inve_name and sender_id in logged_in:
                all_products = grab_data_two.pro_all(cur)
                if text in all_products:
                    bot.send_message_four(sender_id, 'Product already exist. Try again', [[{'text':'Back', 'callback_data':'Investments'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    inve_name[sender_id] = text
                    bot.send_message_four(sender_id, 'Enter Prodcut cost in bits', [[{'text':'Back', 'callback_data':'Investments'}]])
                    bot.get_updates(offset = update_id+1)

            elif sender_id in inve_name and sender_id not in inve_payout and sender_id not in inve_create and sender_id not in inve_cost and sender_id in inve_type and sender_id in logged_in:
                inve_cost[sender_id] = int(text)
                all_types = grab_data_two.type_all(cur)
                if inve_type[sender_id] in all_types:
                    rate = float(grab_data_two.pay_rate(inve_type[sender_id], cur))
                    data_input.investment_types(inve_category[sender_id], inve_type[sender_id], inve_name[sender_id], rate, int(text), 0, cur)
                    bot.send_message_four(sender_id, f'Successfully Created Investment Product\n\nCategory: {inve_category[sender_id]}\nType: {inve_type[sender_id]}\nName: {inve_name[sender_id]}\nCost: {int(inve_cost[sender_id])}\nPayout Rate: {int(rate)}',[[{'text':'Done', 'callback_data':'Investments'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    inve_cost[sender_id] = int(text)
                    inve_create.append(sender_id)
                    bot.send_message_four(sender_id, 'Enter Producut Payout Rate', [[{'text':'Back', 'callback_data':'Investments'}]])
                    bot.get_updates(offset = update_id+1)

            elif sender_id in inve_name and sender_id in inve_cost and sender_id in inve_create and sender_id in logged_in:
                inve_payout[sender_id] = float(text)
                data_input.investment_description(inve_type[sender_id], 'To be added', float(inve_payout[sender_id]), cur)
                data_input.investment_types(inve_category[sender_id], inve_type[sender_id], inve_name[sender_id], float(text), int(inve_cost[sender_id]), 0, cur)
                bot.send_message_four(sender_id, f'Successfully Created Investment Product\n\nCategory: {inve_category[sender_id]}\nType: {inve_type[sender_id]}\nName: {inve_name[sender_id]}\nCost: {int(inve_cost[sender_id])}\nPayout Rate: {int(inve_payout[sender_id])}',[[{'text':'Done', 'callback_data':'Investments'}]])
                bot.get_updates(offset = update_id+1)

            if 'withdraw' in text and len(text.split(' ')) == 2 and sender_id in logged_in:
                b = text.split(' ')
                bot.send_message(sender_id, 'Fetching Details')
                if b[1] != 'withdraw':
                    bot.send_message_four(sender_id, 'Wrong Format\\. Try again', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                elif b[1] == 'withdraw':
                    details = grab_data_two.with_details(int(b[0]), cur)
                    a = details[1]
                    b = a.replace("-", "\\-")
                    balance = str(details[2])
                    c = balance.replace(".", "\\.")
                    bot.send_message(sender_id, f'Username: {details[0]}\nTime: {b}\nAmount: {c} bits\nSerial: {details[3]}')
                    bot.send_message_four(sender_id, f'{details[4]}', [[{'text':'Back', 'callback_data':'Tools'}]])
                    bot.get_updates(offset = update_id+1)
            
            if 'reset' in text and len(text.split(' ')) == 2 and sender_id in logged_in:
                b = text.split(' ')
                a = grab_data_two.user_user(b[0], cur)
                if a == 'Nothing':
                    bot.send_message_four(sender_id, 'Username not found', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    new_pass = generate_pass()[0]
                    update_data.password(b[0], new_pass, cur)
                    bot.send_message(sender_id, 'Successfully Updated Password\\. New Pass:')
                    bot.send_message_four(sender_id, new_pass, [[{'text':'Back', 'callback_data':'Tools'}]])
                    bot.get_updates(offset = update_id+1)

            if sender_id in create_admin and sender_id in logged_in:
                all_user = grab_data_two.user_all(cur)
                if text in all_user:
                    bot.send_message_four(sender_id, 'Username not found', [[{'text':'Cancel','callback_data':'Tools'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    admin_user[sender_id] = text
                    bot.send_message_four(sender_id, f'Are you sure you want to promote {text} to a Manager?', [[{'text':'Confirm', 'callback_data':'Confirm Admin'}],
                                                                                                                [{'text':'Cancel','callback_data':'Tools'}]])
                    bot.get_updates(offset = update_id+1)

            if 'delete' in text and len(text.split(' ')) == 2 and sender_id in logged_in:
                b = text.split(' ')
                a = grab_data_two.user_user(b[0], cur)
                if a == 'Nothing':
                    bot.send_message_four(sender_id, 'Username not found', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.send_message_four(sender_id, f'Are you sure you want to delete {b[0]}?', [[{'text':'Confirm', 'callback_data':'Confirm Delete'},{'text':'Back', 'callback_data':'Tools'}]])
                    delete_user[sender_id] = b[0]
                    bot.get_updates(offset = update_id+1)
            
            if sender_id in add_payout and sender_id in payout_pro and sender_id in logged_in:
                days = 86400*int(text)
                update_data.payout_time(payout_pro[sender_id], days, cur)
                bot.send_message_four(sender_id, 'Payout TIme Updated', [[{'text':'Done', 'callback_data':'Investments'}]])
                bot.get_updates(offset = update_id+1)


            if len(text) > 64 and len(text.split(' ')) == 2 and sender_id in logged_in:
                b = text.split(' ')
                btc_hash = ''
                serial_num = 0
                if len(b[0]) > 63:
                    btc_hash += b[0]
                    serial_num = b[1]
                else:
                    btc_hash += b[1]
                    serial_num = b[0]
                bot.send_message(sender_id, 'hash detected, updating database')
                update_data.withdraws(serial_num, btc_hash, cur)
                bot.send_message_four(sender_id, 'Successfully Updated', [[{'text':'Back', 'callback_data':'Tools'}]])
                bot.get_updates(offset = update_id+1)

    except Exception as e:
        #print(current_updates)
        print(e)
        bot.get_updates(offset = update_id+1)

starter()
