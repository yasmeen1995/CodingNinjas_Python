def pair_sum(arr, target):
    freq = dict()
    ans = 0

    for num in arr:
        expect = target - num
        ans += freq.get(expect, 0)
        if freq.get(num, 0):
            freq[num] += 1
        else:
            freq[num] = 1

    return ans


if __name__ == "__main__":
    print(pair_sum([2,3,1,2,2,3,1,1], 4))

# 2+2: 3
# 3+1: 6