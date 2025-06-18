def best_set(votes):
    dict = {}
    for i in votes:
        if dict.get(votes.get(i)) == None:
            dict[votes.get(i)] = 1
        else:
            dict[votes.get(i)] += 1

    highest = max(dict.values())
    for i in dict:
        if dict.get(i) == highest:
            return i

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
