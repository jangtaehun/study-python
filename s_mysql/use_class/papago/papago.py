#L9NOw4NAWbACl5M7H1l6
#3Qr3poIfhk

#https://openapi.naver.com/v1/papago/n2mt

import urllib.request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

client_id = 'L9NOw4NAWbACl5M7H1l6'
client_secret = '3Qr3poIfhk'
def translate(text):
    encoding_text = urllib.parse.quote(text)
    data = f"source=ko&target=en&text={encoding_text}"
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)

    # -H
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response = json.loads(response.read().decode("utf-8"))
        print(response['message']['result']['translatedText'])
