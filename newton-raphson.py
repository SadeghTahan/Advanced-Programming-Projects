import sys
import random
equation = (sys.argv[1])              #تعریف معادله به صورت رشته
h=1e-6                                #مقدار کوچک برای محاسبه مشتق     
def f(x):                             #محاسبه مقدار تابع در نقطه x
    return eval(equation)
def df(x):                            #محاسبه مشتق تابع در نقطه x
    d=(f(x+h)-f(x))/h
    return d
def newton(x):                        #روش نیوتن-رافسون برای پیدا کردن ریشه معادله
    for i in range(100):
        if abs(df(x))<1e-10:          #اگر مشتق در نقطه x صفر باشد، ریشه پیدا نمی‌شود
            return None
        x=(x-(f(x)/df(x)))
        if (abs(f(x))<1e-10):
            return x      
    return None 
def already_found(r,roots):           #بررسی اینکه آیا ریشه r قبلا پیدا شده است یا خیر
    for old in roots:
        if abs(r-old)<1e-3:
            return True
    return False
roots= []
for t in range(100):
    x=complex(random.uniform(-20,20), random.uniform(-20,20))
    r=newton(x)
    if r!=None and not already_found(r,roots):
        roots.append(complex(round(r.real,4), round(r.imag,4)+0.0))
for root in roots:
    if abs(df(root))<1e-3:           #اگر مشتق در ریشه صفر باشد، ریشه تکراری است
        print("Root found at x =",root,"repeated root")
    else:
        print("Root found at x =",root)           
    