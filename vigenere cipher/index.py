import web

urls = (
    "/", "Encrypt",
    "/decryption", "Decrypt",
    "/favicon.ico","icon",
)

render = web.template.render('templates')
app = web.application(urls, globals())

def ptoc(i,j):
    num1 = ord(i)-97
    num2 = ord(j)-97
    return(chr(((num1+num2)%26)+97))

def ctop(i,j):
    num1 = ord(i)-97
    num2 = ord(j)-97
    return(chr(((num1-num2)%26)+97))

def vigencrypt(plain,k):
    plaintext = plain.lower()
    key = k.lower()
    plaintext = plaintext.replace(' ','')
    key = key.replace(' ','')
    cipher = ''
    j = 0
    keylen = len(key)
    for i in plaintext:
        if(j>keylen-1):
            j= 0
        cipher = cipher + ptoc(i,key[j])
        j = j+1
    return cipher.upper()

def vigendecrypt(cipher,k):
    ciphertext = cipher.lower()
    key = k.lower()
    ciphertext = ciphertext.replace(' ','')
    key = key.replace(' ','')
    plain = ''
    j = 0
    keylen = len(key)
    for i in ciphertext:
        if(j>keylen-1):
            j= 0
        plain = plain + ctop(i,key[j])
        j = j+1
    return plain

class Encrypt:
    def GET(self):
        return render.encryption()

    def POST(self):
        pk = web.input(plaintext='',key='')
        if (pk.plaintext=='') or (pk.key==''):
            return render.encryption(error='You cannot leave any field empty')
        return render.encryption(error='',ciphertext = vigencrypt(pk.plaintext,pk.key))

class Decrypt:
    def GET(self):
        return render.decryption()

    def POST(self):
        ck = web.input(ciphertext='',key='')
        if (ck.ciphertext=='') or (ck.key==''):
            return render.decryption(error='You cannot leave any field empty')
        return render.decryption(error='',plaintext = vigendecrypt(ck.ciphertext,ck.key))

class icon:
    def GET(self): raise web.seeother("/static/favicon.ico")


if __name__ == "__main__":
    app.run()
