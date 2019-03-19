import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
"""data['i'] = 'hola'
data['from'] = ''
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15528766458136'
data['sign'] = '173a0b180c28102fc5e1d932efd2d3d9'
data['ts'] = '1552876645813'
data['bv'] = '33a62fdcf6913d2da91495dad54778d1'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'
data['typoResult'] = 'false'"""

with open('youdaoConfig.txt') as file:
    r = file.read()
    s = r.split('\n')
    for string in s:
        d = string.split(':')
        data[d[0].rstrip()] = d[1].lstrip()

content = input(
    'Please key in the content you want to translate(end with Enter):')
data['i'] = content

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
result = json.loads(html)
print('Translation result: %s'% (result['translateResult'][0][0]['tgt']))
input()



