def minimal_supporter(K, voters):
    
    needed_supporters = [(voters[i] - K) for i in range(1, len(voters))]

    needed_supporters.sort()

    majority_group = (K // 2) + 1

    total_supporters = sum(needed_supporters[:majority_group])

    return total_supporters

K = int(input().strip())
voters = list(map(int, input().strip().split()))


print(minimal_supporter(K, voters))
