import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard
from miscellaneous import image_bytes

session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", 'cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.')
session.cookies.set("__Secure-1PSIDTS", "sidts-CjEBNiGH7vRa89IuM6Jf4PoXJh0ukbAHn23xENACptTwGeDrNaVDdYjmQybgqaBLt_kcEAA")
session.cookies.set("__Secure-1PSIDCC", "ACA-OxOzhCDRJNyclB7URnynkQcso8WMarpKNIitqxz19PI11jhStHIFtSrK-ry6ctVyzSgUCS0")

bard = Bard(token='cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.', session=session)

url='https://th.bing.com/th/id/OIG.s2E8mw2TFqGGCsevwUtX?pid=ImgGn'
image_bytes=image_bytes(url)
res=bard.get_answer(image=image_bytes, input_text='can you explain this image?')
print(res['content'])
