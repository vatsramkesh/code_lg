

def print_binary(n: int):

    if n == 0:
        return
    print_binary(n//2)
    print(n%2, end="")


if __name__ == "__main__":
    print_binary(21) # 10101