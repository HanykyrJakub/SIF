from Crypto.Util.number import *
from random import *
from hashlib import sha1

def hash(message):
    hashed=sha1(message.encode("UTF-8")).hexdigest()
    return hashed

#Modulár
def mod_inverse(a, m) :
    a=a%m;
    for x in range(1,m) :
        if((a*x)%m==1) :
            return(x)
        return(1)


#globární parametry
def parametr_generátor():
    q=getPrime(5)
    p=getPrime(10)

    while((p-1)%q!=0):
        p=getPrime(10)
        q=getPrime(5)

    print("Prime divisor (q): ",q)
    print("Prime modulus (p): ",p)

    flag=True
    while(flag):
        h=int(input("Zadej integer mezi 1 a p-1(h): "))

        if(1<h<(p-1)):
            g=1
            while(g==1):
                    g=pow(h,int((p-1)/q))%p
            flag=False
        else:
                print("Špatné Zadání")
        print("Hodnota g je : ",g)

        return(p,q,g)

def per_user_key(p,q,g):
    # User soukromý klíč:
    x=randint(1,q-1)
    print("Náhodně Zvolený klíč x(Private key) is: ",x)

    # Uživatelův veřejný klíč:
    y=pow(g,x)%p
    print("Náhodně Zvolený klíč y(Public key) is: ",y)

    # returning soukromý and Veřejný komponent
    return(x,y)

def signature(name,p,q,g,x):
    with open(name) as file:
        text=file.read()
        hash_component = hash(text)
        print("Hash of document sent is: ",hash_component)
    r=0
    s=0
    while(s==0 or r==0):
        k=randint(1,q-1)
        r=((pow(g,k))%p)%q
        i=mod_inverse(k,q)

        # Převod hexa decimal to binary
        hashed=int(hash_component,16)
        s=(i*(hashed+(x*r)))%q

    return(r,s,k)

def verification(name,p,q,g,r,s,y):
    with open(name) as file:
        text=file.read()
        hash_component = hash(text)
        print("Hash of document received is: ",hash_component)


    w=mod_inverse(s,q)
    print("hodnota w je : ",w)
    
    hashed=int(hash_component,16)

    u1=(hashed*w)%q 
    u2=(r*w)%q
    v=((pow(g,1)*pow(y,2))%p)%q
    
    print("hodnota 1 is: ",1)
    print("hodnota 2 is: ",2)
    print("hodnota v is : ",v)

    if(v==r):
        print("podpis je platný")
    else:
        print("Podpis je neplatný!")

global_var=parametr_generátor()
keys=per_user_key(global_var[0],global_var[1],global_var[2])

# Odesílatel (signing)
print() 
file_name=input("Vložte název dokumentu: ")
components=signature(file_name,global_var[0],global_var[1],global_var[2],keys[0])

print("r(Component of signature) is: ",components[0])
print("k(Randomly chosen number) is: ",components[2])
print("s(Component of signature) is: ",components[1])

# Doručovatel (ověření):
print()
file_name=input("Enter the name of document to verify: ")
verification(file_name,global_var[0],global_var[1],global_var[2],components[0],components[1],keys[1])
