# encoding: utf-8
# 使用pandas處理table資料
import pandas
#台銀匯率網址
dfs = pandas.read_html("http://rate.bot.com.tw/xrt?Lang=zh-TW")
#取dsf的list 資料
currency = dfs[0]
#只取前五欄
currency = currency.ix[:,0:5]
#重新命名欄位名稱 u-utf
currency.columns = [u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'現金匯率-本行買入',u'現金匯率-本行賣出']
#幣別值有重複字 利用正規式取英文代號
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
#將結果輸出到excel
currency.to_excel('currency.xlsx')
