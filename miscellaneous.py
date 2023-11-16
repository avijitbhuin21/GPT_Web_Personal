import re
import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard
import time, random, os


def structured_response(user_prompt):
    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", 'cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.')
    session.cookies.set("__Secure-1PSIDTS", "sidts-CjEBNiGH7vRa89IuM6Jf4PoXJh0ukbAHn23xENACptTwGeDrNaVDdYjmQybgqaBLt_kcEAA")
    # session.cookies.set("__Secure-1PSIDCC", "ACA-OxPxLahP-2RVSB-iVdW0CREk4oNG6hcTJgdUFjDkPFYJxJxPCjHZGhFEp_TO7mKoSWdzRQ")

    bard = Bard(token='cwhfrYva4ipuvq8-jKzSZ6jAa5HM0XVM8nDF14O9-_A6VESEQ4dL7nEEJo-9fwjy49v7HA.', session=session)

    res=bard.get_answer('Write me a code to check if a number is prime or not in python')
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


def image_bytes(url):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_word = ''.join(random.choice(letters) for i in range(random.randint(3,9)))
    current_time = time.time()
    formatted_date = time.strftime("%Y%m%d", time.localtime(current_time))
    name = 'temp\\'+random_word + formatted_date+'.jpg'
    res=requests.get(url)
    with open(name, "wb") as f:
            f.write(res.content)

    with open(name, 'rb') as image_file:
        image_bytes = image_file.read()
    os.remove(name)
    return image_bytes