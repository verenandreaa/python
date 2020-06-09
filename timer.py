import time

print ('Countdown')
print ('------------')

while True:
        uin = input ('>>')
        try:
            when_to_stop = abs(int(uin))
        except KeyboardInterrupt:
                break
        except:
                print("bukan angka")

        while when_to_stop > 0:
                print(when_to_stop)
                when_to_stop -= 1
                
