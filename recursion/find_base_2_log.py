

def get_base_2_log(n: int) ->int:

    if n == 1:
        return 0
    return 1 + get_base_2_log(n//2)


if __name__ == "__main__":
    assert get_base_2_log(16) == 4
    assert get_base_2_log(33) == 5