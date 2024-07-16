# Write a program to fetch a file and do error handling

# path = 'C:\Manoj\homework\simple.txt'

# path = 'C:\Manoj\homework\simples.txt'

path = r'C:\Manoj\homework\simple.txt'

try:
    with open(path, 'r') as file:
        content = file.read()
        print(f'Content : {path} \n {content}')

        file.write("Thank You !☺️")

except SyntaxWarning:
    print(f'File opened')

except FileNotFoundError:
    print(f'Error : File {path} not found.')

except Exception as e:
    print(f'Error : An unexpected error of {path} and {str(e)}')

