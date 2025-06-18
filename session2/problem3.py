def remove_dupes(items):
    p1 = 0  
    p2 = 1 

    while p2 < len(items):
        if items[p2] != items[p1]:
            p1 += 1
            items[p1] = items[p2]
        p2 += 1
    
    return p1 + 1 