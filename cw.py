def main():
    def quest1():
    #Create a function that has a loop that quits with ```q```.
    # If the user doesn't enter ```q```, ask them to input another string.
    #BONUS: Make sure the code can handle whatever case the User enters the ```q``` as (uppercase or lowercase).
        def q_loop():
            escape=""
            while(escape!='q'):
                escape= input("Please enter 'q' to escape. Otherwise, you'll never escape. ")
                escape = escape.lower() #switches to lowercase
        q_loop()
    def quest2():
    # Write 2 functions: exercise2() and exercise2_helper(num1, num2, num3. operation)
    # The function exercise2_helper(num1, num2, num3) should expect 3 numbers, and an
    # operation to perform as a String as parameters.
        def exercise2():                                                #calls helper function
            exercise2_helper(3,4,7,"SUM")
            exercise2_helper(5,4,3, "PROD")
            exercise2_helper(5,7,3,"AVG")
            exercise2_helper(4,3,6,"HI")

        def exercise2_helper(num1, num2, num3,operation):                #accepts 4 parameters
                operation = operation.lower()                            #switch to lowercase
                if operation== "sum":
                    print("The Sum  of "+str(num1)+ ", "+str(num2)+", and "+str(num3)+" is " + str(num1+num2+num3))
                elif operation=="avg":
                    print("The Average of "+str(num1)+ ", "+str(num2)+", and "+str(num3)+" is " + str((num1+num2+num3)/3))
                elif operation=="prod":
                    print("The Product of "+str(num1)+ ", "+str(num2)+", and "+str(num3)+" is " + str(num1*num2*num3))

                else:                                                  # case where operation is not sum, average,
                                                                       # or product
                    print("Invalid Operation")
        exercise2()

    def Challenge():
    #Write a function that prompts the User for the number of stars to print.
    #Then use a loop to print a number of stars/asterisks starting with 1 and up to the number entered by the User.
        def stars():
            star="*"        # This variable acts as a counter
            copystar="*"    # This acts as an incrementer
            numOfstars= int(input("Enter the number of rows of stars you'd like to see. "))
            for x in range(numOfstars):   # for loop to iterate all the rows of stars
                print(star)
                star+=copystar            #adds star to the end of each count
        stars()
    def ChallengeRedux():        #Second method to Challenge
        def starsRedux():
            increment=0          #Set incrementer to zero
            numOfstars=int(input("Enter the number of rows of stars you'd like to see. "))    #ask for input
            for x in range(numOfstars):    #loop for stars
                while (increment<numOfstars):  #continues until increment is greater than numOfstars
                    increment+=1          #Adds a to incrementer then prints.
                    print("*"*increment)
        starsRedux()
    def Challenge2():
        def speedometer():
            demerit = 0
            speed = int(input("Enter the speed the driver was driving at. "))      #ask user input for speed
            if (speed <=70):
                print("OK")
            else:                                                         #case when speed is greater than 70
                for x in range (speed,70,-5):
                    demerit+=1                                            #adds 1 point for every 5 miles over the speed
                if demerit>12:
                    print("License Suspended")
                else:
                    print("Points: ",demerit)
        speedometer()


    #quest1()
    #quest2()
    #Challenge()
    #ChallengeRedux()
    #Challenge2()





if __name__ == '__main__':
    main()