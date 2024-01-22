import random 
import time
OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10;

def generate_problem():
    left= random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    exp = str(left)+ " "+operator+" "+str(right)
    ans = eval(exp)

    
    return exp,ans;

wrong = 0;
input("press enter to start the game")
print("------------------00000000000000000000--------------------------------")


start_time = time.time();
for i in range(TOTAL_PROBLEMS):
    exp,ans = generate_problem()
    guess = input("problems #s"+ str(i+1) + ":" + exp +"=")
    while True:
        if guess==str(ans):
            break

        wrong+=1
        

end_time = time.time();
total_time = end_time-start_time;
print("--------------------==========--------------")   
print(total_time)