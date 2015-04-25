# Python Refresher Exercise

#So after a while, I have been reinspired to revisit Python
#This was after reading renonwed hacker Eric S. Raymond's paper
#on "How To Become a Hacker"
#He's a co-founder of the Open-Source initiative


def product(list):
    product = 1
    for i in list:
        if i==0:
            return 0

    return product

#this implementation skips zeros
def product_ignore_zero(list):
    product = 1
    for i in list:
        if i!=0:
            product*=i

    return product

def test_me():
    print(product_ignore_zero([1,2,3,4]) )
