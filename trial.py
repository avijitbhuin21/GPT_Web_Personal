# import cv2
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = "D:\\tessaract\\tesseract.exe"

# path=r"C:\Users\iamga\Downloads\WhatsApp Image 2023-06-11 at 16.59.18.jpeg"
# path=path.replace('\\','\\\\')
# print(path)
# img = cv2.imread(path)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# adap=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 31, 5)

# cv2.imshow('original',img)
# cv2.imshow('res',adap)

# text = pytesseract.image_to_string(adap)

# print(text)
# cv2.waitKey(0)



import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard
from miscellaneous import image_bytes

# session = requests.Session()
# session.headers = SESSION_HEADERS
# session.cookies.set("__Secure-1PSID", 'cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.')
# session.cookies.set("__Secure-1PSIDTS", "sidts-CjEBNiGH7vRa89IuM6Jf4PoXJh0ukbAHn23xENACptTwGeDrNaVDdYjmQybgqaBLt_kcEAA")
# session.cookies.set("__Secure-1PSIDCC", "ACA-OxOzhCDRJNyclB7URnynkQcso8WMarpKNIitqxz19PI11jhStHIFtSrK-ry6ctVyzSgUCS0")

# bard = Bard(token='cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.', session=session)

# url='https://www.lifewire.com/thmb/98B5_98YSUmcX6u0gJWembGL7_M=/1756x1171/filters:no_upscale():max_bytes(150000):strip_icc()/IncreaseRange-5bea061ac9e77c00512ba2f2.jpg'
# image_byte,text=image_bytes(url)
# res=bard.get_answer(image=image_byte, input_text=f'can you remake a pandas dataframe of the table from the image for me? here is all the text from the image {text} ')
# print(res['content'])



import re
import requests

def valid(url):
    response = requests.head(url)
    if response.status_code == 200:
        if response.headers['content-type'].startswith('image/'):
            return True

def has_url(text):
    pattern = re.compile(r'''(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))''')
    matches = pattern.findall(text)
    if len(matches)>0:
        return matches


text = r'My Profile:https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of www.geeksforgeeks.org/ google.com '
def query(text):
    l=[]
    links= has_url(text)
    if links:
        for i in links:
            if valid(i)==True:
                i_b,txt=image_bytes(i)
                if txt!="":
                    txt='All the text from this image:'+txt
                    l.append((i_b,txt))
                else:
                    l.append(i_b)
    q=
            
    



