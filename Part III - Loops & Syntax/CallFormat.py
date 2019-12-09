# Page 359
import sys

# redirects output to log.txt
sys.stdout # Prints to console
sys.stderr  # Prints error???
object = 5
print(object, sep=' ', end='\n', file=sys.stdout, flush=False)
print(object, sep=' ', end='\n', file=sys.stderr, flush=False)

a = open("log.txt", "a")
print(object, sep=' ', end='\n', file=a, flush=False)
input()
