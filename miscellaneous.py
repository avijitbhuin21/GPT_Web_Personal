import re
from EdgeGPT.EdgeUtils import Query


def structured_response(user_prompt):
    a = str(Query(user_prompt, style="precise", cookie_files="templates\cookies.json"))
    pattern = r'```(.*?)```'
    code_blocks = re.findall(pattern, a, re.DOTALL)
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

    pattern = r'`(.*?)`'
    code_blocks = set(re.findall(pattern, a, re.DOTALL))
    for i in code_blocks:
        a=a.replace("`"+i+"`","<pre class='small'>"+i+"</pre>")
    return a

