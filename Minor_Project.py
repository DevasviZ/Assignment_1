#Devasvi
import time 

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Timer end')
      
print("Enter S to set","Enter P to pause and resume")
print("gy")
t = input("Enter the time in seconds: ")
countdown(int(t))
