import requests
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-02-24&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=YIJ&purpose_codes=ADULT'
# 添加verify=False参数不验证证书
r = requests.get(url, verify=False)
print(r.json()['data'])
