from calc import add
from greeting import greet


def main():
   greet()
   output = add(5,5)
   print(f'calc operation {add.__name__} = {output}')

if __name__ == '__main__':
   main()