import web

urls = (
    "/", "Encrypt",
    "/decryption", "Decrypt",
    "/favicon.ico","icon",
)

render = web.template.render('templates')
app = web.application(urls, globals())
inverses = {1:1 , 3:9 , 5:21 , 7:15 , 9:3 , 11:19 , 15:7 , 17:23 , 19:11 , 21:5 , 23:17 , 25:25 }
def ptoc(i,j):
    num1 = ord(i)-97
    #for i in range()
    return(chr(((num1+num2)%26)+97))

def ctop(i,j):
    num1 = ord(i)-97
    num2 = ord(j)-97
    return(chr(((num1-num2)%26)+97))

def hillcrypt(plain,k):
    plaintext = plain.lower()
    plaintext = plaintext.replace(' ','')
    cipher = ''
    for i in plaintext:
        cipher = cipher + ptoc(i,key[j])
        j = j+1
    return cipher.upper()

def hilldecrypt(cipher,k):
    ciphertext = cipher.lower()
    ciphertext = ciphertext.replace(' ','')
    plain = ''
    for i in ciphertext:
        if(j>keylen-1):
            j= 0
        plain = plain + ctop(i,k)
        j = j+1
    return plain

class Encrypt:
    def GET(self):
        return render.encryption()

    def POST(self):
        p = web.input(plaintext='')
        key = web.input(a=0,b=0,c=0,d=0)
        if (pk.plaintext=='') or (pk.key==''):
            return render.encryption(error='You cannot leave any field empty')
        return render.encryption(error='',ciphertext = hillcrypt(p.plaintext,key))

class Decrypt:
    def GET(self):
        return render.decryption()

    def POST(self):
        ck = web.input(ciphertext='',key='')
        if (ck.ciphertext=='') or (ck.key==''):
            return render.decryption(error='You cannot leave any field empty')
        return render.decryption(error='',plaintext = hilldecrypt(ck.ciphertext,ck.key))

class icon:
    def GET(self): raise web.seeother("/static/favicon.ico")


if __name__ == "__main__":
    app.run()
