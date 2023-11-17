import re
import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard
import time, random, os
import cv2,pytesseract
 

# collecting and structuring the response received from the api in order to display here
def structured_response(user_prompt):
    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", 'cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.')
    session.cookies.set("__Secure-1PSIDTS", "sidts-CjEBNiGH7vRa89IuM6Jf4PoXJh0ukbAHn23xENACptTwGeDrNaVDdYjmQybgqaBLt_kcEAA")
    session.cookies.set("__Secure-1PSIDCC", "ACA-OxPxLahP-2RVSB-iVdW0CREk4oNG6hcTJgdUFjDkPFYJxJxPCjHZGhFEp_TO7mKoSWdzRQ")

    bard = Bard(token='cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.', session=session)

    res=bard.get_answer(user_prompt)
    a=res['content']
    pattern1 = r'```(.*?)```'
    code_blocks = re.findall(pattern1, a, re.DOTALL)
    c_b = code_blocks[:]  # Make a copy

    for i in range(len(code_blocks)):
        h = code_blocks[i].split('\n')[0]
        if len(h.split()) == 1:
            h = "<h2>" + h + "</h2>"
            code_blocks[i] = "\n".join(code_blocks[i].split('\n')[1:])
        else:
            h = ""
        code_blocks[i] = h + "<pre class='code-block'>" + '\n' + '\n'.join(code_blocks[i].split('\n')) + "<button class='copy-button'>🗐</button>" + "</pre>"

    for i in range(len(c_b)):
        a = a.replace('```' + c_b[i] + '```', code_blocks[i])  # Reassign 'a' with replaced content

    block_letter=re.findall(r'\*\*(.*?)\*\*', a)
    for i in block_letter:
        a=a.replace('**'+i+'**','<strong>'+i+'</strong>')
    pattern3 = r'`(.*?)`'
    code_blocks = set(re.findall(pattern3, a, re.DOTALL))
    for i in code_blocks:
        a=a.replace("`"+i+"`","<pre class='small'>"+i+"</pre>")
    a=re.sub(r'(\d+\.)', r'<br>\1', a)
    a=re.sub(r'\(\^\d+\^\)|\[\^\d+\^\]', '', a)
    return a

#If a image is available the we are processing it here and sending the query to the api 
def image_bytes(url):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_word = ''.join(random.choice(letters) for i in range(random.randint(3,9)))
    current_time = time.time()
    formatted_date = time.strftime("%Y%m%d", time.localtime(current_time))
    path = 'temp\\'+random_word + formatted_date+'.jpg'
    res=requests.get(url)
    with open(path, "wb") as f:
            f.write(res.content)
    text_in_image=OCR(path)
    with open(path, 'rb') as image_file:
        image_bytes = image_file.read()
    os.remove(path)
    return image_bytes,text_in_image

def OCR(path):
    pytesseract.pytesseract.tesseract_cmd = "D:\\tessaract\\tesseract.exe"
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adap=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 31, 5)
    text = pytesseract.image_to_string(adap)
    return text