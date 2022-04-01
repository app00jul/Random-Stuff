"""
Goldbach's Conjecture
Made by: Julian Noeske
To test different range of even number, change the range in #1 and #2 down below!
"""
def prime_number(num):
    if num > 1:
        for i in range(2, num//2):
            if (num%i) == 0:
                #print(num, " is not a prime number!")
                return False
        else:
            #print(num, " is a prime number!!!!!")
            return True

    else:
        #print(num, " is not a prime number!")
        return False

def result(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res

def check_result(lst_1,lst_2):
    if lst_1 == lst_2:
        return True
    else:
        return False

result_answer = []

def goldback_conjecture():
    for i in range(4,10000,2): #1
        print(f"\n{i}")
        prime_num = []
        for l in range(2,i):
            if prime_number(l) == True:
                prime_num.append(l)
            else:
                pass
        for m in prime_num:
            for n in prime_num:
                goldbach = m+n
                if goldbach == i:
                    #print(f"\n{m}+{n}={i}")
                    result_answer.append(i)
                    #print(result_answer)

goldback_conjecture()                
#prime_number_list = list(filter(lambda x: (prime_number(x) == True),range(1,100,2)))
#print(prime_number_list)
#print(result(result_answer))
#print(list(range(4,100,2)))

def final_result():
    if check_result(list(range(4,10000,2)),result(result_answer)) == True: #2
        print("\nThe Goldback Conjecture is valid!")
    else:
        print("\nNOT CORRECT")

final_result()
