print('Hello Mars')
try:
    with open("mission_computer_main.log",'r',encoding='utf-8') as f:
       for line in f:
         print(line.rstrip())
except FileNotFoundError as e:
   print(e)
except PermissionError as e:
   print(e)
except UnicodeDecodeError as e:
   print(e)
except IOError as e:
   print(e)