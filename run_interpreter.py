import interpreter
message = '''
    Please git clone the following repository and run the sample code following the instructions in the README.
    https://github.com/kojima-takeshi188/zero_shot_cot 
    Note that the environment variables are already defined, so there is no need to define them again.
'''
interpreter.chat(message) # Executes a single command
interpreter.chat() # Starts an interactive chat