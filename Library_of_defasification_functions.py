import math  

def Method_of_division_in_half(P, eps):     #Метод деления пополам для метода USt1 (Bisection method for USt1 method)
    tL=0 
    tR=1
    teps=0.5
    while teps>eps:
        t=(tL+tR)/2
        f=t-t*math.log(t)
        if f == P:
            fi=t
            break
        elif f < P:
            tL=t
            teps=teps/2
        else:
            tR=t
            teps=teps/2
        fi=t
    return fi

def Adamo(a, b, c, A, B, C, alfa = 0.5):    #Метод Адамо (Adamo method)
    o=c-(c-b)*alfa
    O=C-(C-B)*alfa
    return o, O

def CofMax(a, b, c, A, B, C):               #Метод центра максимумов (Center maxima method)
    o=b
    O=B
    return o, O

def CofMass(a, b, c, A, B, C):              #Метод Центра масс (Center of Mass Method)
    o=(a+b+c)/3
    O=(A+B+C)/3
    return o, O

def Medians(a, b, c, A, B, C):              #Метод Медианы (Median Method)
    o=(a+2*b+c)/4
    O=(A+2*B+C)/4
    return o, O

def Chang(a, b, c, A, B, C):                #Метод - индекс Чанга (Method - Chang Index)
    o=(c**2-a**2-a*b+b*c)/6
    O=(C**2-A**2-A*B+B*C)/6
    return o, O

def PAv(a, b, c, A, B, C):                  #Метод - возможное среднее (Method - Possible Average)
    o=(a+4*b+c)/6
    O=(A+4*B+C)/6
    return o, O

def Jager(a, b, c, A, B, C):                #Метод - индекс Ягера (Method - Yager index)
    o=(a+2*b+c)/4
    O=(A+2*B+C)/4
    return o, O

def USt1(a, b, c, A, B, C):                 #Метод - USt1 (Method - USt1)
    eps=0.0001
    if (a+c)/2==b:
        o=b
    elif(a+c)/2<b:
        o=b-(b-a)*Method_of_division_in_half((((b-a)-(c-b))/(2*(b-a))), eps)
    elif(a+c)/2>b:
        o=b+(c-b)*Method_of_division_in_half((((c-b)-(b-a))/(2*(c-b))), eps)
    if (A+C)/2==B:
        O=B
    elif(A+C)/2<B:
        O=B-(B-A)*Method_of_division_in_half((((B-A)-(C-B))/(2*(B-A))), eps)
    elif(A+C)/2>B:
        O=B+(C-B)*Method_of_division_in_half((((C-B)-(B-A))/(2*(C-B))), eps)
    return o, O
