#https: // ocr.space / OCRAPI
#K89461803688957
#https://api.ocr.space/parse/imageurl?=helloworld&url=

#https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true

import requests

url = 'https://api.ocr.space/parse/imageurl?apikey=K89461803688957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true'
response = requests.get(url)
response.raise_for_status()
result = response.json()
print(result['ParsedResults'][0]['ParsedText'])