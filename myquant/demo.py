def initialize(context):  # 初始化
    g.security = '002043.XSHE'  # 股票名:兔宝宝


def handle_data(context, data):  # 每日循环
    last_price = data[g.security].close  # 取得最近日收盘价 # 取得过去二十天的平均价格
    average_price = data[g.security].mavg(20, 'close')


cash = context.portfolio.cash  # 取得当前的现金 # 如果昨日收盘价高出二十日平均价, 则买入，否则卖出。
# if last_price > average_price:
#     order_value(g.security, cash)  # 用当前所有资金买入股票
# else if last_price < average_price: order_target(g.security, 0)  # 将股票仓位调整到0，即全卖出
