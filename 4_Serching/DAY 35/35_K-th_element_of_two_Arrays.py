
def kthElement(a, b, k):
    n = len(a)
    m = len(b)
    if n > m:
        return kthElement(b, a, k)

    lo = max(0, k - m)
    hi = min(k, n)

    while lo <= hi:
        mid1 = (lo + hi) // 2
        mid2 = k - mid1

        l1 = (mid1 == 0 and float('-inf') or a[mid1 - 1])
        r1 = (mid1 == n and float('inf') or a[mid1])

        l2 = (mid2 == 0 and float('-inf') or b[mid2 - 1])
        r2 = (mid2 == m and float('inf') or b[mid2])

        if l1 <= r2 and l2 <= r1:
          
            return max(l1, l2)

        if l1 > r2:
            hi = mid1 - 1

        else:
            lo = mid1 + 1

    return 0

if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5

    print(kthElement(a, b, k))