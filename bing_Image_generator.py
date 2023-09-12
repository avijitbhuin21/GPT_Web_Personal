import os
import random
import time
from functools import partial
from typing import Dict, List, Union
import regex
import requests
from IPython.display import Image
from chat_gpt import write_file, remove_cache

image_keywords = ['draw', 'create', 'generate', 'picture', 'image', 'graphic', 'illustration', 'artwork', 'photo', 'sketch']

#TAKEN FROM -- "https://github.com/acheong08/BingImageCreator/blob/main/src/BingImageCreator.py"

BING_URL = os.getenv("BING_URL", "https://www.bing.com")
FORWARDED_IP = f"13.{random.randint(104, 107)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "referrer": "https://www.bing.com/images/create/",
    "origin": "https://www.bing.com",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
    "x-forwarded-for": FORWARDED_IP,
}

# Error messages
error_timeout = "Your request has timed out."
error_redirect = "Redirect failed"
error_blocked_prompt = "Your prompt has been blocked by Bing. Try to change any bad words and try again."
error_being_reviewed_prompt = "Your prompt is being reviewed by Bing. Try to change any sensitive words and try again."
error_noresults = "Could not get results"
error_unsupported_lang = "\nthis language is currently not supported by bing"
error_bad_images = "Bad images"
error_no_images = "No images"

def debug(debug_file, text_var):
    with open(debug_file, "a", encoding="utf-8") as f:
        f.write(str(text_var))
        f.write("\n")


class ImageGen:

    def __init__(
        self,
        auth_cookie: str,
        auth_cookie_SRCHHPGUSR: str,
        debug_file: Union[str, None] = None,
        quiet: bool = False,
        all_cookies: List[Dict] = None,
    ) -> None:
        self.session = requests.Session()
        self.session.headers = HEADERS
        self.session.cookies.update({'_U': auth_cookie, 'SRCHHPGUSR': auth_cookie_SRCHHPGUSR})
        if all_cookies:
            for cookie in all_cookies:
                self.session.cookies.set(cookie["name"], cookie["value"])
        self.quiet = quiet
        self.debug_file = debug_file
        self.debug = partial(debug, self.debug_file) if self.debug_file else lambda *args: None

    def get_images(self, prompt: str) -> list:
        url_encoded_prompt = requests.utils.quote(prompt)
        payload = f"q={url_encoded_prompt}&qs=ds"
        urls = [f"{BING_URL}/images/create?q={url_encoded_prompt}&rt={rt}&FORM=GENCRE" for rt in [4, 3]]

        #https://www.bing.com/images/create/a-guiter-made-of-white-flower-on-a-green-backgroun/64deaa8f7aee43ad943de98537ad96e7?FORM=GENCRE
        
        for url in urls:
            response = self.session.post(url, allow_redirects=False, data=payload, timeout=200)
            if response.status_code == 302:
                break
        else:
            self.debug(f"ERROR: {error_redirect}")
            print(f"ERROR: {response.text}")
            raise Exception(error_redirect)
        
        redirect_url = response.headers["Location"].replace("&nfy=1", "")
        request_id = redirect_url.split("id=")[-1]
        self.session.get(f"{BING_URL}{redirect_url}")
        
        polling_url = f"{BING_URL}/images/create/async/results/{request_id}?q={url_encoded_prompt}"
        start_wait = time.time()
        while True:
            if int(time.time() - start_wait) > 200:
                self.debug(f"ERROR: {error_timeout}")
                raise Exception(error_timeout)
            response = self.session.get(polling_url)
            if response.status_code != 200 or not response.text or response.text.find("errorMessage") != -1:
                time.sleep(1)
                continue
            else:
                break
        image_links = list(set(regex.findall(r'src="([^"]+)"', response.text)))
        bad_images = [
            "https://r.bing.com/rp/in-2zU3AJUdkgFe7ZKv19yPBHVs.png",
            "https://r.bing.com/rp/TX9QuO3WzcCJz1uaaSwQAz39Kb0.jpg",
        ]
        normal_image_links = [link.split("?w=")[0] for link in image_links if link.split("?w=")[0] not in bad_images]
        if not normal_image_links:
            raise Exception(error_no_images)
        return normal_image_links

class img_display:
    def display(prompt,new_conversation_path):
        for i in image_keywords:
            if i in prompt:
                auth_cookie = "1glHV2CTJBuTvq2UOoJIWLB6F-ciBOvMFhRX2FNuDybkqaFPfqZofkh9FanSF1z2vBujStWGLXbWRMagfukBkoRMOUdoNEgtkVqOoTYSp_cE3RrooY754f-aYqJOy16W7C3f8yIYuaNMSdsajPmOxUkGFsGkXkXF8tIEE8yfjOjk-y-HGUbcgn-arQHONGdkZtWrkgtHr0xyVLEH6ymkSveFF9x3lM7i1jgoJk1QdJIE"
                auth_cookie_SRCHHPGUSR = "HV=1692014599&CW=1646&CH=793&SCW=1628&SCH=1991&BRW=XW&BRH=M&SRCHLANG=en&DM=1&THEME=1&PRVCW=1646&PRVCH=793&DPR=1.1&UTC=330&PV=15.0.0&EXLTT=31&cdxtone=Precise&cdxtoneopts=h3precise,clgalileo,gencontentv3&IG=4B70037EE7AC4BBCB29F7851CEA39E82&CMUID=23622FAE0541681D20E73C8804DA6996&VCW=1628&VCH=793&WEBTHEME=1"
                image_generator = ImageGen(auth_cookie, auth_cookie_SRCHHPGUSR)
                image_links = image_generator.get_images(prompt)
                for i in image_links:
                    print(i)
                    Image(url=i, width=400, height=300)
                write_file(new_conversation_path,"Assistant:\n"+"\n".join(image_links))
                print('\n\nUSER: ')
                user=input()
                if user=='q':
                    remove_cache()
                    exit()
                else:
                    write_file(new_conversation_path,"User: "+user)

