from playsound import playsound
import time

CLEAR = "\033[2J" # these are called ANSI they are commands or escape sequences that are invisible characters that when printed to the terminal manipulate it like clearing it changing colour making it bold etc
CLEAR_AND_RETURN = "\033[H"

def alarm (seconds):
    time_elapsed = 0
    
    print(CLEAR) # clears the terminal
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        time_left = seconds - time_elapsed 
        minutes_left = time_left // 60 # // is integer so integer divided if you have 125 // 60 the result is 2 as 60 goes in two times as a full number
        seconds_left = time_left % 60 # modulo gives you the remainder after division so for the above comment it would be 5 as 60 goes into 125 twice with a remainder of 5
        
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") # 02d is a python thing for formatting that means pad with 0 and then use two digits the clear and return clears and returns to the same position ie prints on the same line
        
    playsound("alarm.wav")
minutes = int(input("How many minutes? "))
seconds = int(input("How many seconds? "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
        
    
    


