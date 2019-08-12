def checkPalindrome(num, i, j):
    # So a number or string which needs to checked for being palindrome or not will 
    # have a length thats odd or even
    # If length is odd, there will be middle character thats not repeated but a number on the right and that
    # on the left at a corresponding location will be the same
    # If length is even, there wont be any middle character but mid and mid + 1 will be the same characters

    if i >= j:
        return True
    else:
        return (num[i] == num[j]) and checkPalindrome(num, i+1, j-1)   

    

def main():
    num1  = "1234567654321"
    num2 = "1221"
    num3 = [1,2,2,1, 5]

    print checkPalindrome(num1, 0, len(num1) - 1)
    print checkPalindrome(num2, 0, len(num2) - 1)
    print checkPalindrome(num3, 0, len(num3) - 1)


if __name__ == "__main__":
    main()    