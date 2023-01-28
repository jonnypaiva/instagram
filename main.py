from js import console

def envio(*args, **kwargs):

    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')
    texto =Element('text-input').element.value
    console.log(texto)
    Element('text-output').element.innerText = texto