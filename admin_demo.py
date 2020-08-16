import requests, json, random, string, time, datetime
import grab_data, update_data, data_input, grab_data_two, delete_row, payout_demo
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
        print(send.json())
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
        print(send)
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


gene_pass = {}
gene_amba = {}
create_user = []


mana_id = {}
mana_pass = {}
create_manager = []


asking_id = []
asking_pass = []
logged_in = [468930122, 1211908888]

id_number = {}

credit_acc = []
credit_acc_two = {}
debit_acc = []
debit_acc_two = {}

delete_user = {}
payout_pen = {} #When sending payout to store data
product_name = {} #When sending payout to store pruduct name



bot = BoilerPlate(token)

def starter():
    global offset
    while True:
        all_updates = bot.get_updates(offset)
        for current_updates in all_updates:
            #print(current_updates)
            update_id = current_updates['update_id']
            #bot.get_updates(offset = update_id+1)
            if 'callback_query' in current_updates:
                #print('inline keyboard detected')
                sender_id = current_updates['callback_query']['from']['id']
                group_id = current_updates['callback_query']['message']['chat']['id']
                message_id = current_updates['callback_query']['message']['message_id']
                callback_data = current_updates['callback_query']['data']
                bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, 0 , callback_data=callback_data, callback=True)
            else:
                group_id = current_updates['message']['chat']['id']
                sender_id = current_updates['message']['from']['id']
                message_id = current_updates['message']['message_id']
                dict_checker = []
                for keys in current_updates.get('message'):
                    dict_checker.append(keys)
                if sender_id == group_id:
                    bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, dict_checker)


def bot_message_handler(current_updates, update_id, message_id, sender_id, group_id, dict_checker, callback_data=0, callback=False):
    try:
        if callback == True:
            print(callback_data)
            if callback_data == 'General Ledger' and sender_id in logged_in:
                if sender_id in payout_pen:
                    del payout_pen[sender_id]
                if sender_id in product_name:
                    del product_name[sender_id]
                dep = grab_data_two.dep_total()
                withdraw = grab_data_two.with_total()
                bot.edit_message_two(group_id, message_id, '*General Ledger*', [[{'text':'Net Balance: TO BE EDITED bits', 'callback_data':'None'}], 
                                                                                [{'text':'Net Value: TO BE EDITED bits', 'callback_data':'Total Payouts'}],
                                                                                [{'text':'Total Investment: TO BE EDITED bits', 'callback_data':'Total Payouts'}],
                                                                                [{'text':f'Total Deposits: {dep} bits', 'callback_data':'Total Deposits'}],
                                                                                [{'text':'Total Payouts: TO BE EDITED bits', 'callback_data':'Total Payouts'}],
                                                                                [{'text':f'Total Withdrawals: {withdraw} bits', 'callback_data':'Total Withdrawals'}], 
                                                                                [{'text':'Pending Withdrawals: TO BE EDITED bits', 'callback_data':'Manage Withdrawals'}],
                                                                                [{'text':'Pending Payouts', 'callback_data':'Manage Payouts'}],
                                                                                [{'text':'Pending Residual', 'callback_data':'Manage Residual'}],
                                                                                [{'text':'Back', 'callback_data': 'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Manage Payouts' and sender_id in logged_in:
                pending = grab_data_two.descri_pending()
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

            elif callback_data in grab_data_two.descri_pending() and sender_id in logged_in:
                data = payout_demo.details(callback_data)
                if data == 'Nothing':
                    bot.edit_message_two(group_id, message_id, 'No one is holding any product of this category', [[{'text':'Back', 'callback_data': 'General Ledger'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    pay_rate = float(grab_data_two.pay_rate(callback_data))
                    full_text = ''
                    total = 0
                    rate = str(pay_rate).replace('.','\\.')
                    full_text += f'Payout Rate: {rate}\n\n'
                    pending = {}
                    for i in data:
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
                    invest_bala = float(grab_data_two.inve_bala(i))
                    inte_bala = float(grab_data_two.balance_inte(i))
                    update_data.balance_info(i, invest_bala+float(data[i]))
                    update_data.balance_interest(i, inte_bala+float(data[i]))
                    data_input.payout_transaction(i, product, float(data[i]))
                del payout_pen[sender_id]
                update_data.payout_pending(product)
                bot.edit_message_two(group_id, message_id, 'Payout successfully sent', [[{'text':'Back', 'callback_data': 'General Ledger'}]])

            elif callback_data == 'Total Deposits':
                full_text = ''
                grabbing = grab_data_two.deposits()
                i = len(grabbing[0])
                for d in range(i):
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

            elif callback_data == 'Total Withdrawals':
                full_text = ''
                grabbing = grab_data_two.withdraws()
                i = len(grabbing[0])
                for d in range(i):
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
                if 'Pending' in grab_data_two.with_status()[0]:
                    pending_amount = len(grab_data_two.with_status())
                    serials = grab_data_two.with_serial()
                    pending_serials = ''
                    for i in range(pending_amount):
                        pending_serials += f'{str(serials[i][0])} '
                    bot.edit_message_two(group_id, message_id, f'Total Pending Withdrawals: {pending_amount}\nPending Withdrawal Serials: {pending_serials}\n\nEnter a Serial Number \\+ withdraw to get full details\n\nexample\n57 withdraw', [[{'text':'Back', 'callback_data':'Tools'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.edit_message_two(group_id, message_id, 'No Withdrawal is Pending', [[{'text':'Back', 'callback_data':'Tools'}]])
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
            
            if callback_data == 'Confirm Delete' and sender_id in logged_in:
                delete_row.delete_user(delete_user[sender_id])
                bot.edit_message_two(group_id, message_id, f'{delete_user[sender_id]} has been deleted', [[{'text':'Back', 'callback_data':'Tools'}]])
                del delete_user[sender_id]
                bot.get_updates(offset = update_id+1)

            if callback_data == 'Client' and sender_id in logged_in:
                full_text = ''
                grabbing = grab_data_two.user_all()
                i = len(grabbing)
                for d in range(i):
                    full_text += f'Username: {grabbing[d][0]}\n'
                full_text += 'End of List\n\nType a Username \\+ client to get full details of a user\n\nexample\nSakib0194 client'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)
            
            if callback_data == 'Managers' and sender_id in logged_in:
                full_text = ''
                grabbing = grab_data_two.mana_all()
                i = len(grabbing)
                for d in range(i):
                    full_text += f'Manager ID: {grabbing[d][0]}\n'
                full_text += 'End of List\n\nType a ID \\+ manager to get full details of a manager\n\nexample\nTM1X46BAAD manager'
                bot.edit_message_two(group_id, message_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            
            if callback_data == 'Log Out' and sender_id in logged_in:
                bot.send_message(sender_id, 'Logged Out')
                bot.send_message(sender_id, 'Please Provide your *ID*')
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
                bot.edit_message_two(group_id, message_id, '*Tools*', [[{'text':'Create Client', 'callback_data':'Create User'}], 
                                                                    [{'text':'Create Manager', 'callback_data':'Create Manager'}], 
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
            
            elif callback_data == 'Password Reset' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Enter a Client Username \\+ reset to get a new password\n\nExample\nSakib0194 reset', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)
            
            elif callback_data == 'Delete Account' and sender_id in logged_in:
                bot.edit_message_two(group_id, message_id, 'Enter a Client Username \\+ delete to delete an account\\.\nNote: deleting will cause the username cease to exist however, his data will still remain in the database\n\nExample\nSakib0194 delete', [[{'text':'Back', 'callback_data':'Back'}]])
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Create User' and sender_id in logged_in:
                code = generate_pass()
                passw = code[0]
                amba_code = code[1]
                while passw in grab_data_two.user_password(passw)[0] or amba_code in grab_data_two.user_amba(amba_code)[0]:
                    code = generate_pass()
                    passw = code[0]
                    amba_code = code[1]
                gene_pass[sender_id] = passw
                gene_amba[sender_id] = amba_code
                bot.edit_message_two(group_id, message_id, f'Generated Password: {passw}\nGenerated Ambassador Code: {amba_code}\n\nInsert the Required Credential sequentially following with a space\n\nTelegram ID None if not available\nFirst Name one word only, None if not available\nDAM Username One Word\nEnter your Ambassador Code\nTelegram Username None if not available\n\nexample of the message\nNone Hawl Snake53 LVXD4A8 Hawl754', [[{'text':'Back', 'callback_data':'Tools'}]])
                if sender_id not in create_user:
                    create_user.append(sender_id)
                bot.get_updates(offset = update_id+1)

            elif callback_data == 'Create Manager' and sender_id in logged_in:
                code = generate_pass()
                passw = code[0]
                amba_code = code[1]
                while passw in grab_data_two.mana_id(passw)[0] or amba_code in grab_data_two.mana_password(amba_code)[0]:
                    code = generate_pass()
                    passw = code[0]
                    amba_code = code[1]
                mana_id[sender_id] = passw
                mana_pass[sender_id] = amba_code
                bot.edit_message_two(group_id, message_id, f'Generated ID: {amba_code}\nGenerated Password: {passw}\n\nInsert the Required Credential sequentially following with a space\n\nTelegram ID None if not available\nFirst Name one word only, None if not available\nSpecial Access YES or NO only, only uppercase letter\nUsername from Client Bot\nAmbassador Code from Client Bot\n\nexample of the message\n468930122 Ruth NO Vito LVXD4A8', [[{'text':'Back', 'callback_data':'Tools'}]])
                if sender_id not in create_manager:
                    create_manager.append(sender_id)
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

            if text == '/start' and sender_id in logged_in:
                bot.send_message_four(sender_id, '*BitBot Company Panel*', [
                                                                        [{'text':'General Ledger', 'callback_data':'General Ledger'}], 
                                                                        [{'text':'Managers', 'callback_data':'Managers'}],
                                                                        [{'text':'Clients', 'callback_data':'Client'}],
                                                                        [{'text':'Investments', 'callback_data':'Investments'}],
                                                                        [{'text':'Tools', 'callback_data':'Tools'}],
                                                                        [{'text':'Log Out', 'callback_data':'Log Out'}]])
            if text == '/start' and sender_id not in logged_in:
                bot.send_message(sender_id, 'Please provide your *ID*')
                asking_id.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in asking_id and grab_data_two.mana_id(text)[0] == 'Nothing':
                bot.send_message(sender_id, 'Please provide a valid *ID*')
                bot.get_updates(offset = update_id+1)

            elif sender_id in asking_id and text in grab_data_two.mana_id(text)[0]:
                bot.send_message(sender_id, 'Please provide your *password*')
                id_number[sender_id] = text
                asking_id.remove(sender_id)
                asking_pass.append(sender_id)
                bot.get_updates(offset = update_id+1)
            
            elif sender_id in asking_pass and grab_data_two.mana_password(text)[0] == 'Nothing':
                bot.send_message(sender_id, 'Incorrect *password*, please try again')
                bot.get_updates(offset = update_id+1)

            elif sender_id in asking_pass and text in grab_data_two.mana_password(text)[0] and grab_data_two.mana_access(id_number[sender_id]) == 'YES':
                bot.send_message(sender_id, 'Access Granted')
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
                if a[2] == grab_data_two.user_username(a[2])[0][0]:
                    bot.send_message_four(sender_id, 'Username already exist\\! Try again', [[{'text':'Back', 'callback_data':'Cancel'}]])
                    bot.get_updates(offset = update_id+1)
                elif a[2] != grab_data_two.user_username(a[2])[0][0]:
                    ref = grab_data_two.amba_users(a[4])
                    print(ref)
                    print(a[4])
                    refer_number = ref + 1
                    print(refer_number)
                    data_input.user_info(a[0], a[1], a[2], gene_pass[sender_id], gene_amba[sender_id], a[3],time_splitter(str(datetime.datetime.fromtimestamp(time.time()))), a[4])
                    data_input.balance_info(a[0], a[1], a[2], 0,0,0)
                    data_input.amba_info(a[0], a[1], a[2], gene_amba[sender_id], a[3], 0)
                    update_data.amba_info(a[3], refer_number)
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
                    data_input.managers(a[0], a[1], date, mana_pass[sender_id], mana_id[sender_id], a[2],a[3], a[4])
                    bot.send_message_four(sender_id, f'Manager Successfully Created\nManager ID: {mana_id[sender_id]}\nManager Password: {mana_pass[sender_id]}', [[{'text':'Back', 'callback_data':'Cancel'}]])
                else:
                    bot.send_message_four(sender_id, 'Wrong Format\\. Type YES or NO in uppercase letters\\. Try again', [[{'text':'Back', 'callback_data':'Tools'}]])

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
                    a=grab_data_two.user_user(b[0])
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
                    a=grab_data_two.mana_mana(b[0])
                    if a == 'Nothing':
                        bot.send_message_four(sender_id, 'ID not found', [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)
                    else:
                        tim = a[2]
                        time_two = tim.replace("-", "\\-")
                        print(a)
                        full_text = f'Telgram ID: {a[0]}\nFirst Name: {a[1]}\nJoining Date: {time_two}\nID Number: {a[3]}\nPassword: {a[4]}\nSpecial Access {a[5]}\nUsername: {a[6]}\nAmbassador Code: {a[7]}'
                        bot.send_message_four(sender_id, full_text, [[{'text':'Back', 'callback_data':'Back'}]])
                        bot.get_updates(offset = update_id+1)

            if sender_id in debit_acc and sender_id in logged_in and len(text) > 2:
                bot.send_message(sender_id, 'Checking Username validity')
                validity = grab_data_two.user_username(text)
                if validity[0] != 'Nothing':
                    balance = int(grab_data_two.inve_bala(text))
                    bot.send_message_four(sender_id, f'User Current Balance: {balance} bits\\. Enter the amount of bits to debit', [[{'text':'Back', 'callback_data':'Back'}]])
                    debit_acc.remove(sender_id)
                    debit_acc_two[sender_id] = text
                    bot.get_updates(offset = update_id+1)
                elif validity[0] == 'Nothing':
                    bot.send_message_four(sender_id, 'Username Not Found', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)

            if sender_id in debit_acc_two and sender_id in logged_in and text.isnumeric():
                bot.send_message(sender_id, 'Updating Balance')
                balance = float(grab_data_two.inve_bala(debit_acc_two[sender_id]))
                to_add = balance - int(text)
                date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                update_data.balance_info(debit_acc_two[sender_id], to_add)
                serial = grab_data_two.withdraw_serial()
                data_input.withdraws('Admin', 'None', debit_acc_two[sender_id], date, 'Debited By Admin','Debited By Admin', text, 'CONFIRMED', serial+1)
                bot.send_message_four(sender_id, 'Balance Successfully Debited', [[{'text':'Back', 'callback_data':'Back'}]])
            
            if sender_id in credit_acc and sender_id in logged_in and len(text) > 2:
                bot.send_message(sender_id, 'Checking Username validity')
                validity = grab_data_two.user_username(text)
                if validity[0] != 'Nothing':
                    balance = int(grab_data_two.inve_bala(text))
                    bot.send_message_four(sender_id, f'User Current Balance: {balance} bits\\. Enter the amount of bits to credit', [[{'text':'Back', 'callback_data':'Back'}]])
                    credit_acc.remove(sender_id)
                    credit_acc_two[sender_id] = text
                    bot.get_updates(offset = update_id+1)
                elif validity[0] == 'Nothing':
                    bot.send_message_four(sender_id, 'Username Not Found', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)

            if sender_id in credit_acc_two and sender_id in logged_in and text.isnumeric():
                bot.send_message(sender_id, 'Updating Balance')
                balance = float(grab_data_two.inve_bala(credit_acc_two[sender_id]))
                to_add = balance + int(text)
                date = time_splitter(str(datetime.datetime.fromtimestamp(time.time())))
                update_data.balance_info(credit_acc_two[sender_id], to_add)
                data_input.deposits('Admin', 'None', credit_acc_two[sender_id], date, 'Credited By Admin', text, 'Success')
                bot.send_message_four(sender_id, 'Balance Successfully Credited', [[{'text':'Back', 'callback_data':'Back'}]])

            if 'withdraw' in text and len(text.split(' ')) == 2 and sender_id in logged_in:
                b = text.split(' ')
                bot.send_message(sender_id, 'Fetching Details')
                if b[1] != 'withdraw':
                    bot.send_message_four(sender_id, 'Wrong Format\\. Try again', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                elif b[1] == 'withdraw':
                    details = grab_data_two.with_details(int(b[0]))
                    a = details[1]
                    b = a.replace("-", "\\-")
                    balance = str(details[2])
                    c = balance.replace(".", "\\.")
                    bot.send_message(sender_id, f'Username: {details[0]}\nTime: {b}\nAmount: {c} bits\nSerial: {details[3]}')
                    bot.send_message_four(sender_id, f'{details[4]}', [[{'text':'Back', 'callback_data':'Tools'}]])
                    bot.get_updates(offset = update_id+1)
            
            if 'reset' in text and len(text.split(' ')) == 2 and sender_id in logged_in:
                b = text.split(' ')
                a = grab_data_two.user_user(b[0])
                if a == 'Nothing':
                    bot.send_message_four(sender_id, 'Username not found', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    new_pass = generate_pass()[0]
                    update_data.password(b[0], new_pass)
                    bot.send_message(sender_id, 'Successfully Updated Password\\. New Pass:')
                    bot.send_message_four(sender_id, new_pass, [[{'text':'Back', 'callback_data':'Tools'}]])
                    bot.get_updates(offset = update_id+1)

            if 'delete' in text and len(text.split(' ')) == 2 and sender_id in logged_in:
                b = text.split(' ')
                a = grab_data_two.user_user(b[0])
                if a == 'Nothing':
                    bot.send_message_four(sender_id, 'Username not found', [[{'text':'Back', 'callback_data':'Back'}]])
                    bot.get_updates(offset = update_id+1)
                else:
                    bot.send_message_four(sender_id, f'Are you sure you want to delete {b[0]}?', [[{'text':'Confirm', 'callback_data':'Confirm Delete'},{'text':'Back', 'callback_data':'Tools'}]])
                    delete_user[sender_id] = b[0]
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
                update_data.withdraws(serial_num, btc_hash)
                bot.send_message_four(sender_id, 'Successfully Updated', [[{'text':'Back', 'callback_data':'Tools'}]])
                bot.get_updates(offset = update_id+1)

    except Exception as e:
        print(current_updates)
        print(e)
        bot.get_updates(offset = update_id+1)

starter()
