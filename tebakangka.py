answer = 5 

def get_guess():
    ask = input('Guess the number! (1-9)!')
    if is_valid(ask):
        return int(ask)
    else:
        print('Invalid')
        return get_guess()

def is_valid(num):
    try:
        number = int(num)
    except:
        return False
    return 1 <= number <=9

def play():
    count = 0
    while True:
        count += 1
        guess = get_guess()
        if guess > answer:
            print ('kegedean')
        elif guess < answer:
            print ('kekecilan')
        else:
            break
    print (f'jagooo! {count} attempts!')

play()