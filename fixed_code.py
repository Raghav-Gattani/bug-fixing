# AFTER: fixed with Cursor AI
def average_bounty(bounties):
    if not bounties:                    # FIX 2: handle empty list
        return 0
    total = 0
    for bounty in bounties:             # FIX 1: loop over every item
        total += bounty
    return total / len(bounties)

crew = [3000000000, 1500000000, 320000000]
print("Average bounty:", average_bounty(crew))
print("Empty crew:", average_bounty([]))
