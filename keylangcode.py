# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 20:32:54 2019

@author: astrobout
"""
cypherDict={'a':'_-_' ,'b':'_=' ,'c':'-_' ,'d':'-=_' ,'e':'=_' ,'f':'=' ,'g':'-_=_' ,'h':'-' ,'i':'_' ,'j':'_-' ,'k':'-_-=' ,'l':'-__' ,'m':'_-_-_' ,'n':'_--_' ,'o':'-=-' ,'p':'_-=-' ,'q':'-=-_' ,'r':'-_--' ,'s':'_=_' ,'t':'-_=' ,'u':'-__-' ,'v':'-_-' ,'w':'-_-_-' ,'x':'-_-_' ,'y':'=_=' ,'z':'=-_','0':'-==-','1':'_-=_','2':'--=_','3':'--=-_','4':'-=_=','5':'-==_','6':'--_=','7':'-_=-','8':'-=-=_','9':'-=-_-','!':'----=','@':'=_-_-','#':'--__=','$':'-_=_-','%':'-=--_','^':'__-__','&':'_-=_=-','*':'-_-=-_'}


decypherDict = {}
for k, v in cypherDict.items():
    decypherDict[v] = k


def keyencrypt(message, key):
    
    keydict={'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','a':'10' ,'b':'11' ,'c':'12' ,'d':'13' ,'e':'14' ,'f':'15' ,'g':'16' ,'h':'17' ,'i':'18' ,'j':'19' ,'k':'20' ,'l':'21' ,'m':'22' ,'n':'23' ,'o':'24' ,'p':'25' ,'q':'26' ,'r':'27' ,'s':'28' ,'t':'29' ,'u':'30' ,'v':'31' ,'w':'32' ,'x':'33' ,'y':'34' ,'z':'35','!':'36','@':'37','#':'38','$':'39','%':'40','^':'41','&':'42','*':'43',' ':'44'}

    convert = {}
    for u, v in keydict.items():
        convert[v] = u


    keylist=list(key)
    messagelist=list(message)
    k=len(keylist)
    m=len(messagelist)
    a=m%k
    b=int(m/k)


    keyiterate=[]
    for i in range(0,b):
        for j in range(0,k):    
            keyiterate.append(keylist[j])
    for i in range(0,a):
        keyiterate.append(keylist[i])


    final=[]
    for i in range(0,m):
        mm=int(keydict.get(messagelist[i]))
        mv=int(mm*int(keyiterate[i]))
        q=int(mv/44)
        p=int(mv%44)
        r=convert.get(str(p))
        final.append(r)
        final.append(q)

    return ''.join(map(str, final))


def Decrypter(message):
    eachWord =message.split(':')
    dec=[]
    for letter in eachWord:
        if letter in decypherDict.keys():
            a=decypherDict.get(letter)
            dec.append(a)
    return dec




def KLCencrypter(keymessage,key):
    statement=keyencrypt(keymessage,key)
    p=[]
    letters=list(statement)
    cyp=[]
    for l in letters:
        if l in cypherDict.keys():
            b=cypherDict.get(l)
            cyp.append(b)
    string = ':'.join(cyp)
    p.append(string)        
    pr = '::'.join(p)
    print(pr)





def KLCdecrypter(messagel,key):
    
    keydict={'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','a':'10' ,'b':'11' ,'c':'12' ,'d':'13' ,'e':'14' ,'f':'15' ,'g':'16' ,'h':'17' ,'i':'18' ,'j':'19' ,'k':'20' ,'l':'21' ,'m':'22' ,'n':'23' ,'o':'24' ,'p':'25' ,'q':'26' ,'r':'27' ,'s':'28' ,'t':'29' ,'u':'30' ,'v':'31' ,'w':'32' ,'x':'33' ,'y':'34' ,'z':'35','!':'36','@':'37','#':'38','$':'39','%':'40','^':'41','&':'42','*':'43',' ':'44'}

    convert = {}
    for u, v in keydict.items():
        convert[v] = u


    keylist=list(key)
    messagelist=Decrypter(messagel)
    k=len(keylist)
    m=len(messagelist)
    q=messagelist[1::2]
    p=messagelist[::2]
    z=len(p)
    
    a=int(m%(2*k))
    b=int(m/(2*k))
    print(a)
    print(k)
    keyiterate=[]
    for i in range(0,b):
        for j in range(0,k):    
            keyiterate.append(keylist[j])
    if(k<a):
        for i in range(0,k):
            keyiterate.append(keylist[i])
        for i in range(0,a-k):
            keyiterate.append(keylist[i])
    else:
        for i in range(0,a):
            keyiterate.append(keylist[i])
    
        
        
    ccc=[]
    final1=[]
    for i in range(0,z):    
        aaa=int(keydict.get(p[i]))
        bbb=int(q[i])
        ccc=(44*bbb)+aaa       
        ddd=int(ccc/int(keyiterate[i]))
        ri=convert.get(str(ddd))
        final1.append(ri)
    return print(''.join(map(str, final1)))


