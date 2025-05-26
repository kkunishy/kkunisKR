scores=[85,95,70,75,99,93,88]

print(scores)
print('최대값',max(scores))
print('최소값',min(scores))
print('합계',sum(scores))
print('평균',sum(scores)/len(scores))
scores.sort()
print(scores)