import time
import string
import itertools

chars = string.printable

password = '2R'   # here, i am setting the password string.
max_length = 10    #set up max length of password
start_time = time.time() 

print("------------------PASSWORD CRACKER ------------------")
for length in range(1, max_length + 1):                               # length -> 1 se 10 tk chalegi 
    for combination in itertools.product(chars, repeat=length):       # itertools ke andar humare sare chars hai eg. A a s b @ 3 ...(used in brute forcing)
        candidate = "".join(combination)                              # "" => converts int into string => i get comb. 123 -> it gets conv. to "123" -> which are further used in comparision
        print("Trying Password:", candidate)
        if candidate == password:
            end_time = time.time()
            print("____PASSWORD fOUND______:", candidate)
            time_taken = end_time-start_time
            print("Time Taken:", time_taken)
            raise SystemExit
