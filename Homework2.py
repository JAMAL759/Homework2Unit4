def print_greeting() :
   python_is_fun = True
   if python_is_fun: 
        print("Python is fun!")


print_greeting()



def check_letter(argument1):
    if argument1 == 'a' or argument1 == 'e' or argument1 == 'i' or argument1 == 'u' :
            print("The letter" + argument1 + " is a vowel")
    
    else: 
         print("The letter is a consonant")


check_letter("a")


#

def check_voting_eligibility():

      age = input("Enter your age: ")
      if int(age) > 0:
           print("Please enter a valid age")
   
    # Your control flow logic goes here

# Call the function
check_voting_eligibility()



# Exercise 3: Calculate Dog Years


def calculate_dog_years():
        dogAge = int(input("Enter your dog age"))

        if dogAge  <= 2 :
              dogAge += 10
              print(dogAge)

        elif dogAge >= 3 : 
              dogAge += 7
              print( dogAge)
              

# Call the function
calculate_dog_years()



# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
  cold = bool (input("is it cold"))
  rain = bool(input("is it raining"))

  if cold == True and rain == True :
       print("Wear a waterproof coat")

  elif cold == True and rain == False:
          print("Wear a waterproof coat")

  elif cold == False and rain == True:
          print("Carry an umbrella")
          
  elif cold == False and rain == False:
          print("Wear light clothing")

# Call the function
weather_advice()


def fizz_buzz():
    


    for x in range(1 , 51):
     print(x)
     if x % 3 == 0 :
          print("Fizz")
    
     if x % 5 == 0 :
          print("Buzz")

     if x % 5 == 0 and x % 3 == 0 :
          print("FizzBuzz") 

# Call the function
fizz_buzz()