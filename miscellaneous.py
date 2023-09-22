import re
from EdgeGPT.EdgeUtils import Query


def structured_response(user_prompt):
    a = str(Query(user_prompt, style="precise", cookie_files="templates\cookies.json"))
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

