import random 


flag = True 
while flag:
    n = int(input('please guess a number between 1 to 10 : '))
    r = random.randint(1, 10)
    
    if n >=1 and n <= 10:
        if n == r:
            flag = False
            print(f'computer num = {r}'); print(f'your num = {n}')
            print('Spot on!')
        elif n > r:
            print('try smaller')  
        else:
            print('try bigger')          
    else:
        print(f'{n} is not an available number')

    