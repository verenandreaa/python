jawaban = 8

x = 'berapa ayam yg dimiliki bejo?'

while True:
    pertanyaan = int(input(f'{x} '))
    if pertanyaan > jawaban:
        print ('kegedean')
    elif pertanyaan < jawaban:
        print ('kekecilan')
    else:
        break
    x = 'try again'

print ('jago')
