
"""def html_tags(tags):
    def wrapper_(func):
        def wrapper(*arg, **warg):
            # print(arg) 
            # (["course math", "course chinese", "course english", "course physics"], '')
            result = arg[1]
            for tag in tags:
                # result = result.join(['', tag + 'this is the start']) # didn't work the arg is still ''
                result += tag + 'this is the start'
                arg[1] = result # still didn't work cause arg is a tuple
                result = func(*arg, **warg)
                result = result.join(['', '/' + tag + 'this is the end'])
            return result
        return wrapper
    return wrapper_"""

"""def html_tags(tags):
    def wrapper_(func):
        def wrapper(template, result): # this works
            for tag in tags:
                result = result.join(['', '<' + tag + '>' + 'this is the start'])
                result = func(template, result)
                result = result.join(['', '</' + tag + '>' + 'this is the end' + '>\n'])
            return result
        return wrapper
    return wrapper_

data = ["html", "body", "div"]

@html_tags(data)
def hello(template, result):
    for ele in template:
        result = result.join(['', ele])
    return result
    
template = ['course math-', 'course chinese-', 'course english-', 'course physics']
print(hello(template, ""))
# <html>this is the startcourse math-course chinese-course english-course physics</html>this is the end>
# <body>this is the startcourse math-course chinese-course english-course physics</body>this is the end>
# <div>this is the startcourse math-course chinese-course english-course physics</div>this is the end>
"""

"""def html_tags(tags):
    def wrapper_(func):
        result  = ''
        def wrapper(*arg):
            template = arg[0]
            nonlocal result
            # print(arg) 
            # (["course math", "course chinese", "course english", "course physics"], '')
            for tag in tags:
                result = result.join(['', '<' + tag + '>' + 'this is the start']) 
                result = func(*arg)
                result = result.join(['', '</' + tag + '>' + 'this is the end' + '\n'])
            return result
        return wrapper
    return wrapper_

data = ["html", "body", "div"]

@html_tags(data)
def hello(template, result):
    for ele in template:
        result = result.join(['', ele])
    return result
    
template = ['course math-', 'course chinese-', 'course english-', 'course physics']
print(hello(template, ""))
# course math-course chinese-course english-course physics</div>this is the end
"""

def html_tags(tags):
    def wrapper_(func):
        def wrapper(**warg):
            print(warg)
            # {'template': ['course math-', 'course chinese-', 'course english-', 'course physics'], 'result': ''}
            for tag in tags:
                warg["result"] = warg["result"].join(['', '<' + tag + '>' + 'this is the start']) # didn't work
                warg["result"] = func(**warg)
                warg["result"] = warg["result"].join(['', '</' + tag + '>' + 'this is the end' + '\n'])
            return warg["result"]
        return wrapper
    return wrapper_

data = ["html", "body", "div"]

@html_tags(data)
def hello(template, result):
    for ele in template:
        result = result.join(['', ele])
    return result
    
template = ['course math-', 'course chinese-', 'course english-', 'course physics']
print(hello(template=template, result=""))
# <html>this is the startcourse math-course chinese-course english-course physics</html>this is the end
# <body>this is the startcourse math-course chinese-course english-course physics</body>this is the end
# <div>this is the startcourse math-course chinese-course english-course physics</div>this is the end

