def right_triangle(n: int) -> str:
    result = ""
    for i in range(1, n + 1):
        result += "*" * i
        if i != n:   # avoid newline in last line
            result += "\n"
    return result

if __name__ == "__main__":
    n = int(input())
    print(right_triangle(n))
