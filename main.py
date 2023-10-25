from calc import add, divide
from greeting import greet


def main():
   greet()
   operation = str(input('type a calc operation (add/divide): '))
   # print(operation is add.__name__) # bag
   # print(operation ==  add.__name__) # fix bag
   if operation == add.__name__:
      output = add(5,5)
      print(f'calc operation {add.__name__} = {output}')
   elif operation == divide.__name__:
      output = divide(5,5)
      print(f'calc operation {divide.__name__} = {output}')
   else:
      raise Exception(operation)

if __name__ == '__main__':
   main()