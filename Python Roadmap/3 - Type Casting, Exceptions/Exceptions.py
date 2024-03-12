# https://realpython.com/python-exceptions/
# most common exceptions

# SyntaxError because of an additional ), syntax type error
try:
    print(0/0)
except Exception as e:
    print(f"Exception: {e}")

# ZeroDivisionError division by 0,  execution type error
try:
    print(0/0)
except Exception as e:
    print(f"Exception: {e}")

# four different operations with exceptions
# raise - create an exception
# assert - debug and test
# try || except - handling exceptions
# else || finally - fine tuning exception handling

# RAISE
number = 10
try:
    if number > 5:
        raise Exception(f"The number should not exceed 5. ({number=})")
except Exception as e:
    print(f"Exception: {e}")


# ASSERT
# creates an AssertionError
# used to check if a condition is met
# if someone runs the script using the optimised CLI option (python -O Exceptions.py)
# then all of the assertions will fail to get called and the code will get executed
number = 10
try:
    assert (number < 5), f"The number should not exceed 5. ({number=})"
except Exception as e:
    print(f"Exception: {e}")
    
# TRY and EXCEPT
# Python will raise a runtime exception if this code is run on an OS that doesn't run Linux
def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

# if an exception happens then the code just skips it over and does nothing
try:
    linux_interaction()
except:
    pass

# can change it into something like
try:
    linux_interaction()
except Exception as e:
    print(f"Exception: {e}")
    
# can also catch different types of errors separately
try:
    linux_interaction()
    with open("file.log") as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except RuntimeError as error:
    print(error)
    print("Linux linux_interaction() function wasn't executed.")
    
    
# ELSE after TRY 
# try: ...
# except: ...
# else: ...


try:
    print("This is a simple test")
except Exception as e:
    print(f"Exception: {e}")
else: 
    print("This is another simple test")
    
    
    # FINISHED HERE 
    #If you don’t nest the print() call under the else clause, then it’ll execute even if Python encounters the RuntimeError that you handle in the except block above. On a Linux system, the output would be the same, but on macOS or Windows, you’d get the following output: 