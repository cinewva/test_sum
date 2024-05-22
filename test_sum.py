import random

def main():
    print("Khansole Academy")
    # write a while statement that stopps after 3 correct
    correct = 0
    while correct != 3:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        sum = num1 + num2
        print("What is " + str(num1) + " + " + str(num2) + "? ")

        sum_user = input("Your answer: ")
        if sum == int(sum_user):            
            print("Correct!")
            correct += 1
        else:
            correct = 0            
            print("Incorrect.")
            print("The expected answer is", sum)
        
    print("Congratulations! You mastered addition.")
    
    
if __name__ == '__main__':
    main()
