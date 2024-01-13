class Speed(Exception):
    pass

def student():
    speed= 10         # attention in percent
    try:
        if speed<50:
            raise Speed('You are not a rider.')
        print("You are a rider.")
    except Speed as s:
        print(s)
        
student()

