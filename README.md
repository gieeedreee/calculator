# Calculator
Calculator package

## Introduction
   Calculator is able to perform these actions:
    
   * Addition / Subtraction
    
   * Multiplication / Division
    
   * Take (n) root of number
    
   * Reset memory
   
   Calculator have its own memory, meaning it manipulates its starting number 0 until it is reseted. 
   It means that each of actions return the last 'starting value' and continues to perform actions with that value: add/ subtract/ multiply/ divided/ take (n) root of provided number. 
      
   It is necessary to pay attention to division action - division of zero is not possible. So result is last 'starting value' in this case.
    
 ## Technologies
 Python 3.x
 
 ## Launch
 Install the package into the Google Collab's env using pip:
 
    ! pip install git+https://github.com/gieeedreee/calculator

    from calculator.calculator import Calculator

    calculator = Calculator()
    
