# Local Scope
# Variables declared inside functions have local scope, They are only seen by the other code within the same block of code. 

# Global Scope
player_health = 10 

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# There's is no Block Scope in Python!
# def creates a local scope
# if, while, for, are all block scope, they don't create local scope and maintain the variable
# a global scope.

#__________________________________________________________________________________________________
# Check if a number is a prime number 

def is_prime(num):

    if num == 2:
        return True
    elif num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
            
    return True
            
    is_prime(1)
 