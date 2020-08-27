import os, time

do_again = ''.lower()
while do_again != 'no':

    num = int(input('Input the number to be factorised - '))
    divisors = range(1, int(num + 1))
    factors = []



    for i in range(1, num + 1):
        quotient = num / i
        for n in divisors:
            if float(n) == quotient:
                factors.append(i)
            else:
                pass

    for i in factors:
        print(i)

    export = input("Do you want to export the factors to a file ? ").lower()
    if export == 'yes':
        os.chdir("C:\\Users\\Public\\Desktop")
        file = open(f'Factors of {num}.txt', 'w+')
        for f in factors:
            file.write(f"{str(f)} \n")
        file.close()
    elif export == 'no':
        print("Ok.")
        time.sleep(2)
    else:
        pass

    do_again = input("Would you like to factor another number ? ").lower()
    if do_again == 'no':
        print("Quitting...")
        time.sleep(2)
    else:
        pass