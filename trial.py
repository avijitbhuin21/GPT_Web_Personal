from bing_Image_generator import Image_Gen
from IPython.display import Image,display
import json

prompt='a half humanoid made of a lot of watch wheels'

data = json.load(open("templates\cookies.json"))
image_generator = Image_Gen(all_cookies=data)

res=image_generator.Generate(prompt=prompt)
for link in res:    
    print(link)    
    display(Image(url=link))