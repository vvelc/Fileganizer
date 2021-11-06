# AUTHOR: Jonathan Sandoval

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

if __name__ == "__main__":
   s = "123456789 ABCDEF"
   c = color()
   print(c.PURPLE + s)
   print(c.CYAN  + s)
   print(c.DARKCYAN + s)
   print(c.BLUE  + s)
   print(c.GREEN + s)
   print(c.YELLOW + s)
   print(c.RED + s)
   print(c.BOLD  + s)
   print(c.UNDERLINE + s)
   print(c.END + s)
   print(c.HEADER + s)
   print(c.OKBLUE + s)
   print(c.OKGREEN + s)
   print(c.WARNING + s)
   print(c.FAIL + s) 