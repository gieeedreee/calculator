# Calculator
Calculator package
## Introduction
Calculator package contains 2 modules - calculator (code with main aspects of OOP) and test (pytest).
    Calculator is able to perform these actions:
    
    * Addition / Subtraction
    
    * Multiplication / Division
    
    * Take (n) root of number
    
    * Reset memory
    
 ## Technologies
 Python 3.x
 
 ## Launch
 Install the package into the Google Collab's env using pip:
 
    ! pip install git+https://github.com/gieeedreee/calculator

    from calculator.calculator import Calculator

    calculator = Calculator()

For testing (working in the notebooks) it is need to install the package using pip:

    !pip install pytest ipython_pytest

    import pytest

    And add %%pytest at every cell that contains test.
    
