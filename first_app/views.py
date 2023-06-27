from django.shortcuts import render
import random
# Create your views here.
def index(request):
    username = '이순신'
    
    result = {
        'username': username,
    }

    return render(request, 'index.html', result)

def lunch(request):
    menus = ['라면', '김밥', '떡볶이']

    pick = random.choice(menus)
    result = {
        'pick': pick
    }

    return render(request, 'lunch.html', result)

def lotto(request):
    lotto_num = []
    while len(lotto_num) < 6:
        pick_num = random.randint(1,45)
        if pick_num not in lotto_num:
            lotto_num.append(pick_num)
    result = {
        'lotto': lotto_num
    }        

    return render(request, 'lotto.html', result)        
    
