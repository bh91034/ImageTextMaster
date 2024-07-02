import googletrans
from httpcore import SyncHTTPProxy

ENABLE_PROXY = False

if ENABLE_PROXY:
    proxies_def = {'https': SyncHTTPProxy((b'http', b'www-proxy.us.oracle.com', 80, b''))}
    translator = googletrans.Translator(proxies=proxies_def)
else:
    translator = googletrans.Translator()

str1 = "나는 한국인 입니다."
str2 = "I like burger."
result1 = translator.translate(str1, dest='en')
result2 = translator.translate(str2, dest='ko')

print(f"나는 한국인 입니다. => {result1.text}")
print(f"I like burger. => {result2.text}")
