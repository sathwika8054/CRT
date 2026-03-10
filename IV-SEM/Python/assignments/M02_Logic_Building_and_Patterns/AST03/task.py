def sum_of_digits(n: int) -> int:
        a=[]
        for i in range(len(str(abs(n)))):
            a.append(int(str(abs(n))[i]))
        return sum(a)

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))
