### KEY: Really excellent job both with comments and testing all the expected outcomes! 

# Python Review of Misc Topics - JavaScript/Python comparison, Loops, Functions

### Problem 1:
##### We will keep having this problem until EVERYONE gets it right without help
Create a function that has a loop that quits with ```q```. If the user doesn't enter ```q```, ask them to input another string.

BONUS: Make sure the code can handle whatever case the User enters the ```q``` as (uppercase or lowercase).

### Problem 2:
Write 2 functions: ```exercise2()``` and ```exercise2_helper(num1, num2, num3. operation)```

The function ```exercise2_helper(num1, num2, num3)``` should expect 3 numbers, and an operation to perform as a String as parameters. 

The function should support 3 operations:
* ```SUM``` - Return the sum of the 3 numbers
* ```PROD``` - Return the product of the 3 numbers
* ```AVG``` - Return the average of the 3 numbers

The operation and the returned value should then be printed out back in the main ```exercise2()``` function. Return ```INVALID OPERATION``` if an operation passed in that isn't supported. HINT: Use ```switch/case```

#### Examples:
```
exercise2_helper(2,4,6,"SUM")
exercise2_helper(2,4,6,"PROD")
exercise2_helper(2,4,6,"AVG")
```
Expected Output:
```
The SUM of 2,4,6 is 12
The PROD of 2,4,6 is 48
The AVG of 2,4,6 is 4
```

### CHALLENGE 1:
Write a function that prompts the User for the number of stars to print. Then use a loop to print a number of stars/asterisks starting with 1 and up to the number entered by the User.

If rows is 5, it should print the following:
```
*
**
***
****
*****
```

### CHALLENGE 2:
Write a function for checking the speed of drivers. Prompt the User to enter the speed that a driver was observed driving at.

If speed is less than 70, it should print ```Ok```.

Otherwise, for every 5mph above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. 

For example, if the speed is 80, it should print: ```Points: 2```.

If the driver gets more than 12 points, the function should print: ```License Suspended```

