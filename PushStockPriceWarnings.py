import itchat
import datetime
import time
import tushare as TS

def login():
    itchat.auto_login()

def InputList(all_list = []):
    stock_symbol_list = []
    price_min_list = []
    price_max_list = []
    for i in range(int(len(all_list) / 3)):
        stock_symbol_list.append(all_list[3 * i])
        price_min_list.append(all_list[3 * i + 1])
        price_max_list.append(all_list[3 * i + 2])
    return stock_symbol_list, price_min_list, price_max_list

def get_push(all_list = [], UserName):
    str(UserName)
    stock_symbol_list, price_min_list, price_max_list = InputList(all_list)
    localtime = datetime.datetime.now() # get the current time
    now = localtime.strftime('%H:%M:%S') # get the hour, min, second
    data = TS.get_realtime_quotes(stock_symbol_list) # get the index of stocks
    price_list = data['price']
    itchat.send(now, toUserName='filehelper')
    print(now)

    for i in range(int(len(all_list) / 3)):
        content = stock_symbol_list[i] + ' 当前价格为 ' + price_list[i] + '\n'
        if float(price_list[i]) <= float(price_min_list[i]):
            itchat.send(content + '低于最低预警价格', toUserName= UserName)

        elif float(price_list[i]) >=  float(price_max_list[i]):
            itchat.send(content + '高于最高预警价格', toUserName= UserName)


def push(all_list = [], UserName):
    str(UserName)
    itchat.send('PushStockPriceWarnings', toUserName= UserName)
    print('Start push warnings! Commander!')
    while True:
        try:
            get_push(all_list)
            time.sleep(1)
        except KeyboardInterrupt:
            itchat.send('Stop push warnings! Commander!')
            print('\n'
                'Stop push warnings! Commander!')
            break


