import web

urls = (
    "/", "EncryptDecrypt",
    "/favicon.ico","icon",
)

render = web.template.render('templates')
app = web.application(urls, globals())

def ptoc(i,j):
    num1 = ord(i)-97
    num2 = j
    return(chr(((num1+num2)%26)+97))

def shiftcrypt(plain,k):
    plaintext = plain.lower()
    key = int(k)
    plaintext = plaintext.replace(' ','')
    cipher = ''
    j = 0
    for i in plaintext:
        cipher = cipher + ptoc(i,key)
    return cipher.upper()


class EncryptDecrypt:
    def GET(self):
        return render.encryption()

    def POST(self):
        pk = web.input(plaintext='',shift='')
        if (pk.plaintext=='') or (pk.shift==''):
            return render.encryption(error='You cannot leave any field empty')
        return render.encryption(error='',ciphertext = shiftcrypt(pk.plaintext,pk.shift))

class icon:
    def GET(self): raise web.seeother("/static/favicon.ico")


if __name__ == "__main__":
    app.run()
