import pymysql
import html2text
import requests
import re

connectionObject = pymysql.connect(host="localhost", user="root", port=3307, database="test", autocommit=True)

url = "https://rest.coinapi.io/v1/symbols?apikey=E9948224-4D41-4BE2-BEFA-BC634C5E4DEE&filter_symbol_id=BINANCE_SPOT_LTC_BTC;BINANCE_SPOT_LTC_ETH;BINANCE_SPOT_BCH_BTC;BINANCE_SPOT_WAVES_BTC;BINANCE_SPOT_BCH_USDT&filter_price="

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

html_response = requests.get(url=url, headers=headers)

with open("sample.html", "w") as html_file:
    html_file.write(html_response.text)

with open("sample.html", "r") as html_file:
    html = html_file.read()
    text_ = html2text.html2text(html)

fs = str(text_)
s = str("BINANCE_SPOT_")
pattern = s
match = re.findall(pattern, fs)

s1 = str(text_)
print(text_)
pattern = r'(?<=, "price":\s)\d+\.[0-9]{1,10}\,'
s2 = (re.findall(pattern, s1))
z = str(" ".join(s2))
d = {}

for index, value in enumerate(s2):
    d[index] = value
print(d)
lst = s2
key = set(s2)
rez = dict.fromkeys(key, 0)
for key in lst:
    rez[key] += 1
sql1 = (d.get(0))
print(sql1)
sql2 = (d.get(1))
print(sql2)
sql3 = (d.get(2))
print(sql3)
sql4 = (d.get(3))
print(sql4)
sql5 = (d.get(4))
print(sql5)
asql1 = (sql1.rstrip(','))
asql2 = (sql2.rstrip(','))
asql3 = (sql3.rstrip(','))
asql4 = (sql4.rstrip(','))
asql5 = (sql5.rstrip(','))
LTC_BTC = asql1.replace('.', ',')
BCH_BTC = asql2.replace('.', ',')
BCH_USDT = asql3.replace('.', ',')
LTC_ETH = asql4.replace('.', ',')
WAVES_BTC = asql5.replace('.', ',')
f = open('sql.txt', 'w', encoding='utf-8')
f.write(f'{[LTC_BTC, BCH_BTC, BCH_USDT, LTC_ETH, WAVES_BTC]}')
f.close()
try:
    cursorObject = connectionObject.cursor()

    cursorObject = connectionObject.cursor()
    # sqlCreateTableCommand = "create TABLE `csv1` (`LTC_BTC` float NOT NULL,`BCH_BTC` float NOT NULL, `BCH_USDT`
    # float NOT NULL, `LTC_ETH` float NOT NULL, `WAVES_BTC` float NOT NULL)" cursorObject.execute(
    # sqlCreateTableCommand)
    insertStatement = "INSERT INTO `csv1` (LTC_BTC, BCH_BTC, BCH_USDT, LTC_ETH, WAVES_BTC) VALUES (%s,%s,%s,%s,%s)"
    cursorObject.execute(insertStatement, (LTC_BTC, BCH_BTC, BCH_USDT, LTC_ETH, WAVES_BTC))
finally:
    connectionObject.commit()
    connectionObject.close()
