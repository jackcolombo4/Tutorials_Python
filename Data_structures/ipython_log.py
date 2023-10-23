# IPython log file

get_ipython().run_line_magic('time', 'sum(range(1000000))')
get_ipython().run_cell_magic('time', '', 'a = [i for i in range(1000000)]\nb = sum(a)\n')
get_ipython().run_line_magic('whos', '')
# Get a description of all variables
x = 5
y = "hello"
get_ipython().run_line_magic('who', '')
#Lists all variables in the namespace
get_ipython().run_line_magic('whos', '')
# Get a description of all variables
get_ipython().run_line_magic('whos', '')
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('history', '-n 1-5')
# Shows the history of commands 1 through 5
get_ipython().run_line_magic('lsmagic', '')
#Lists all available magic commands
print(%lsmagic)
#Lists all available magic commands
#Lists all available magic commands
get_ipython().run_line_magic('lsmagic', '')
get_ipython().run_line_magic('alias', 'showdir ls -l .')
showdir
get_ipython().run_line_magic('alias', 'showdir ls -l .')
get_ipython().run_line_magic('showdir', '')
get_ipython().run_line_magic('alias', 'showdir ls -loX .')
get_ipython().run_line_magic('showdir', '')
get_ipython().run_line_magic('alias', 'showdir ls -loX . | head')
get_ipython().run_line_magic('showdir', '')
get_ipython().run_line_magic('cd', './Data_structures/')
#%cd ./Data_structures/
# Debug errors with a debugger
def divide(a, b):
    return a / b

divide(1, 0)
get_ipython().run_line_magic('debug', '')
# Debug errors with a debugger
def divide(a, b):
    return a / b

divide(1, 0)
#%debug  
# Debug errors with a debugger
def divide(a, b):
    return a / b

divide(1, 0)
get_ipython().run_line_magic('debug', '')
# Debug errors with a debugger
def divide(a, b):
    return a / b

divide(1, 0)
#%debug  
# Debug errors with a debugger
def divide(a, b):
    return a / b

divide(1, 0)
get_ipython().run_line_magic('debug', '')
# Debug errors with a debugger
def divide(a, b):
    return a / b

divide(1, 0)
get_ipython().run_line_magic('env', 'PATH')
get_ipython().run_line_magic('autocall', '1')
print "Hello, World!"
get_ipython().run_line_magic('autosave', '60  # Autosave every minute')
get_ipython().run_line_magic('autosave', '60  # Autosave every minute')
# Autosave every minute
get_ipython().run_line_magic('autosave', '60')
get_ipython().run_line_magic('bookmark', 'return_here')
get_ipython().run_line_magic('cls', '')
#%dirs
get_ipython().run_line_magic('dirs', '')
get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('logstop', '')
