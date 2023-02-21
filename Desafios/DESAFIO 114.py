from urllib import request
import urllib

try:
    siteP = request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro!!')
else:
    print('Ta tudo ok!!')

