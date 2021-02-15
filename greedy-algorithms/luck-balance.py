# Complete the luckBalance function below.
def luckBalance(k, contests):
    zero_nums = []
    one_nums = []
    for val, index in contests:
        if index == 1:
            one_nums.append(val)
        else:
            zero_nums.append(val)
    one_nums.sort(reverse=True)
    return sum(one_nums[:k]) + sum(zero_nums) - sum(one_nums[k:])
