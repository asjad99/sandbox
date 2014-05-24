class myclass:

    #__a,__b=0,0;
    __var1 = 99;
    def __init__(self):
        self.a = 10;
        self.b = 20;
        print("instantiating");
#swaps a number without using a temporary variables...
    def swap_values(self):
        temp = 99; print ("temp is 20", 20);
        print("before swaping",self.a,self.b);
        self.a = self.a + self.b
        self.b = self.a - self.b
        self.a = self.a -self.b; print ("After swapping", self.a,self.b);
        return 
  
#isprime is used to see if the number is prime or not.         
def isprime(n):
        if n == 1:
             print ("1 is special")
             return False
        for x in range(2,n):
            if n%x == 0:
                print("number is not prime")
                return False
        else:
            print("number is prime")       

#calculate factorial of a number
def cal_factorial(f):
    t = 1;result = 1;
    if f == 1:
        print ("the factorial is one");
    else:
        while (f>0):
            result = result*f;
            f=f-1;
        print ("the factorial is", result)
 
def main():
    print("In main")
    temp = myclass();
    temp.swap_values();
    #temp.print_private()
#call isprime to see if the number is prime or not. 
    isprime(3)
    cal_factorial(4)
#call main
main()