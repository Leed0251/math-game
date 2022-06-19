import os

def clear_console():
    command = "clear"
    if os.name in ('nt','dos'):
        command = "cls"
        
    # Run the clear command
    os.system(command)