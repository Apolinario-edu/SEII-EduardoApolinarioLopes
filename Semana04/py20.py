#Blocos de tentativas 

try:
    f = open('curruptfile.txt') #arquivo texto na mesma pasta 
    
except IOError as e:
    print('First!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')

