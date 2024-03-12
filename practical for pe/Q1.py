def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    sequence = []
    while True:
        num = input("Enter a positive integer (or 'done' to finish): ")
        if num.lower() == 'done':
            break
        try:
            num = int(num)
            if num > 0:
                sequence.append(num)
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer or 'done'.")
    
    prime_num = []
    for num in sequence:
        if is_prime(num):
            prime_num.append(num)
    
    if prime_num:
        print('The sequence:', set(prime_num))
        print("Max:", max(prime_num))
    else:
        print('No prime number found.')

main()
            
        