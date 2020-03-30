"""def html_tags(tag_name):
    def wrapper_(func):
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            return "<{tag}>{content}</{tag}>".format(tag=tag_name, content=content)
        return wrapper
    return wrapper_

@html_tags('h1')
def hello(name='great!!!'):
    return 'Hello {}!'.format(name)
    
print(hello())  
# <h1>Hello great!!!!</h1>
print(hello('world'))
# <h1>Hello world!</h1>"""

# once you write the input pararmeter of wrapper as a specific input
# then you must pass the value to this parameter in real function
def html_tags(tag_name):
    def wrapper_(func):
        def wrapper(input):
            content = func(input)
            return "<{tag}>{content}</{tag}>".format(tag=tag_name, content=content)
        return wrapper
    return wrapper_

@html_tags('h1')
def hello(input='great!!!'):
    return 'Hello {}!'.format(input)

print(hello('must have pass value in here'))  
# <h1>Hello must have pass value in here!</h1>
print(hello('world'))
# <h1>Hello world!</h1>