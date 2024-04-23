def check_strict_superset(n, numbers):
    for _ in range(n):
        counter = 0
        set_1 = set(map(int, input().split()))
        for x in set_1:
            if x in numbers:
                counter += 1
        if counter != len(set_1):
            return False
    return True

numbers = set(map(int, input().split()))
n = int(input())
print(check_strict_superset(n, numbers))
