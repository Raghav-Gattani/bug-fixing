# BEFORE: buggy program - calculates average bounty of a crew
def average_bounty(bounties):
    total = 0
    for i in range(1, len(bounties)):   # BUG 1: skips the first item
        total += bounties[i]
    return total / len(bounties)        # BUG 2: crashes on empty list

crew = [3000000000, 1500000000, 320000000]
print("Average bounty:", average_bounty(crew))
print("Empty crew:", average_bounty([]))
