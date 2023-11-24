def find_most_popular(votes):
    count_dict = {}

    for num in votes:
        count_dict[num] = count_dict.get(num, 0) + 1

    max_count = max(count_dict.values())

    max_nums = [num for num, count in count_dict.items() if count == max_count]

    result = min(max_nums)

    return result


num_tests = int(input())

for _ in range(num_tests):
    num_votes = int(input())
    votes = [int(input()) for _ in range(num_votes)]

    result = find_most_popular(votes)
    print(result)
