'''contador de palabras'''
from urllib import request
from urllib.error import URLError

def contar_palabras (url)
    try:
        f = request.urlopen(url)
    except URLError:
        return "error de url"
    else:
        contenido = f.read()
        return len(contenido.split())


n = contar_palabras('https://www.abc.com.py/')
print(f"Cantidad palabras en ABC color: {n}")