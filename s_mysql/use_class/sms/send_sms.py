import json
from s_mysql.task.mysql_with_api.sms import message

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
def send_message(phone, certification):
    data = {
        'messages': [
            {
                'to': phone,
                'from': '01090890655',
                'text': certification
            },
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
