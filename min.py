''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

    N = int(input("N : "))

    stud = []
    for i in range(N):
        name = input("Name : ")
        rating = int(input("R : "))
        if rating > 10 and rating < 1:
            return False
        else:
            stud.append([name,rating])

    # names = min(stud[rating].sort())
    names = sorted(stud, key=lambda x:x[1])
    print(names)
main()