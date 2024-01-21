#https: // ocr.space / OCRAPI
#K89461803688957
#https://api.ocr.space/parse/imageurl?=helloworld&url=

#https://api.ocr.space/parse/imageurl?apikey=&url=&language=&isOverlayRequired=true

import requests
def ocr(path):
    url = f'https://api.ocr.space/parse/imageurl?apikey=K89461803688957&url={path}&language=kor&isOverlayRequired=true'
    response = requests.get(url)
    response.raise_for_status()
    result = response.json()
    return result['ParsedResults'][0]['ParsedText']