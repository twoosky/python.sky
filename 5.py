#5

score = []
score_sum=0
aver=0
count = 0 
for i in range(5):
    score.append(int(input('점수를 입력 : ')))
    score_sum = score_sum + score[i]
aver = score_sum/len(score)
print(aver)
for i in range(5):
    if score[i] > aver:
        count += 1

print("평균 이상의 학생 수 : %d"%count)
