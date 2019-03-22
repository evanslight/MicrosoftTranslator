# -*- coding: utf-8 -*-
import requests, json, uuid, os
from langdetect import detect 
import re
import time

class Translate():
    def __init__(self):
        # register on Azure and get the keys
        self.subscriptionKey = '**********************'
    
    def translate(self, trans_text):       
        base_url = 'https://api.cognitive.microsofttranslator.com'
        # path = '/detect?api-version=3.0'
        path = '/translate?api-version=3.0'
        params = '&from=zh-Hans&to=en'
        constructed_url = base_url + path + params
        
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscriptionKey,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        # where the data needs to be translated 
        body = [{
            'text': trans_text
        }]

        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()
        # print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))       
        return(response)

    def do_translate(self, path, dest_path):
        # use 'rb' rather than 'r' to avoid UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 263: illegal multibyte sequence
        with open(path, 'rb') as f:
            with open(dest_path,'ab') as file_append:
                for line in f.readlines():
                    check_list = line.decode().split("=")      
                    # first check the line whether has parts to be translated      
                    if(len(check_list) > 1):
                        # pre process for the text before detecting the language
                        new_source = re.sub('[0-9 \n\.\r\{\}<>()]', '', check_list[1])
                        # first detect whether chinese or not
                        if(("zh-cn" not in [detect(x) for x in new_source.split()]) and ("ko" not in [detect(x) for x in new_source.split()]) and ("et" not in [detect(x) for x in new_source.split()]) ):
                            file_append.write(line)
                            pass
                        else:
                            # print the part that needed to be translated
                            print(line.decode().split("=")[1])
                            # translate
                            phrase_translated = self.translate(line.decode().split("=")[1]) #translating phrase
                            # get the transalted result
                            d = phrase_translated[0]['translations'][0]['text']
                            result = line.decode().split("=")[0]+"="+d
                            print (result)
                            # append to file
                            file_append.write(result.encode())
                    else:
                        file_append.write(line)
                        pass
                    time.sleep(1)

if __name__ == '__main__':
    path = './翻译源文件.txt'
    dest_path = './翻译结果.txt'
    trans = Translate()
    trans.do_translate(path, dest_path)
