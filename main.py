with open('passwords.txt', 'r') as check:
    count = 0
    try:
        for line in check:
            letter, start, stop, password = line.replace(':', '').replace('-', ' ').split()
            if letter in password and password.count(letter) in range(int(start), int(stop) + 1):
                count += 1
        print(count)
    except ValueError:
        print('Error, check file')
