def max_audience_performances(audiences):
    highest = max(audiences)
    total = 0
    for i in audiences:
        if i == highest:
            total += highest
    return total

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
