# Method 1
def palindrome_number(n: int) -> bool:

    # using the strings to confront the two numbers
    num_text = str(n)
    num_text_inv = num_text[::-1]
    return num_text == num_text_inv


# Method 2
def palindrome_number_while(n: int) -> bool:
    
    n_original = n # rember of the original number
    inverted_num = 0 # inverted number

    while n > 0:
        remainder = n % 10 # dividing the number by ten and taking only the remainder
        inverted_num = (inverted_num * 10) + remainder # summing the inverted number (multiplicated by ten, to rappresent the increasing order) and adding the remainder
        n //= 10 # dividing the number for 10 without considering the remainder and as an intger number

    return n_original == inverted_num

if __name__ == '__main__':
    print(palindrome_number(121))
    print(palindrome_number_while(121))