class Main:
    def f1(self, inputString):
        def Takedata(inputdata):
            number = []
            for i in inputdata:
                if i.isdecimal():
                    number.append(int(i))
            return number
        
        def sum_prime_numbers(n):
            prime_numbers = []
            for num in range(2, n):
                is_prime = True
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_numbers.append(num)
            return sum(prime_numbers)

        data = inputString.split()
        numbers = []
        for inputdata in data:
            numbers += Takedata(inputdata)
        min_number = min(numbers)
        print(f"The sum of prime numbers less than {min_number} is: {sum_prime_numbers(min_number)}")

    def f2(self, inputString):
        pass

    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        inputString = input("Enter the input string: ")
        print("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        else:
            print("Wrong select")
        print("FINISH")

main = Main()
main.main()


