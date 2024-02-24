import fourtyNine
fourtyNine.greet()
# Hello dear! 
# Hello dear! -> executes 2 times because we have called greet in imported file
# therefore we use if __name__ == "__main__" to avoid this

# when we print(__name__) in fourtyNine.py, it prints __main__ because it is the main file that is being executed
# when we print(__name__) in this file, it prints fourtyNine because it is the imported file that is being executed