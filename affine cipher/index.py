import web

urls = (
    "/", "Encrypt",
    "/decryption", "Decrypt",
    "/favicon.ico","icon",
)

render = web.template.render('templates')
app = web.application(urls, globals())

inverses = {1:1 , 3:9 , 5:21 , 7:15 , 9:3 , 11:19 , 15:7 , 17:23 , 19:11 , 21:5 , 23:17 , 25:25 }

def ptoc(i,a,b):
    num1 = ord(i)-97
    return(chr((((num1*a)+b)%26)+97))

def ctop(i,a,b):
    num1 = ord(i)-97
    a = inverses[a]
    return(chr((((num1-b)*a)%26)+97))

def affinencrypt(plain,a,b):
    plaintext = plain.lower()
    plaintext = plaintext.replace(' ','')
    a = int(a)
    b = int(b)
    cipher = ''
    for i in plaintext:
        cipher = cipher + ptoc(i,a,b)
    return cipher.upper()

def affinedecrypt(cipher,a,b):
    ciphertext = cipher.lower()
    ciphertext = ciphertext.replace(' ','')
    a = int(a)
    b = int(b)
    plain = ''
    for i in ciphertext:
        plain = plain + ctop(i,a,b)
    return plain

class Encrypt:
    def GET(self):
        return render.encryption()

    def POST(self):
        pk = web.input(plaintext='',a='',b='')
        pk.a = int(pk.a)
        #print pk.plaintext , pk.a ,pk.b
        if (pk.plaintext=='') or (pk.a=='') or (pk.b==''):
            return render.encryption(error='You cannot leave any field empty')
        elif pk.a not in inverses :
            return render.encryption(error='Inverse %d does not exist'%(int(pk.a)))
        else:
            return render.encryption(error='',ciphertext = affinencrypt(pk.plaintext,pk.a,pk.b))

class Decrypt:
    def GET(self):
        return render.decryption()

    def POST(self):
        ck = web.input(ciphertext='',a='',b='')
        ck.a = int(ck.a)
        if (ck.ciphertext=='') or (ck.a=='') or (ck.b==''):
            return render.decryption(error='You cannot leave any field empty')
        elif ck.a not in inverses :
            return render.decryption(error='Inverse %d does not exist'%(int(ck.a)))
        else:
            return render.decryption(error='',plaintext = affinedecrypt(ck.ciphertext,ck.a,ck.b))

class icon:
    def GET(self): raise web.seeother("/static/favicon.ico")


if __name__ == "__main__":
    app.run()
