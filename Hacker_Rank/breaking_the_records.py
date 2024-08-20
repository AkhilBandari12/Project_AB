"""


Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.

Sample Input 0
9
10 5 20 20 4 5 2 25 1

Sample Output 0
2 4

Explanation 0
The diagram below depicts the number of times Maria broke her best and worst records throughout the season:
She broke her best record twice (after games  and ) and her worst record four times (after games , , , and ), 
so we print 2 4 as our answer. Note that she did not break her record for best score during game ,
 as her score during that game was not strictly greater than her best record at the time.

 

Sample Input 1
10
3 4 21 36 10 28 35 5 24 42

Sample Output 1
4 0

Explanation 1
The diagram below depicts the number of times Maria broke her best and worst records throughout the season:
She broke her best record four times (after games , , , and ) 
and her worst record zero times (no score during the season was lower than the one she earned during her first game), so we print 4 0 as our answer.




"""

# st = "3 4 21 36 10 28 35 5 24 42"
# scores = st.split(" ")
# print(scores)
# l = []
# for i in scores:
#     l.append(int(i))

# print(l)

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

best = scores[0]
worst = scores[0]

best_broken = 0
worst_broken = 0

for i in range(len(scores)):

    if scores[i]>best:
        best = scores[i]
        best_broken+=1
    if scores[i]<worst:
        worst = scores[i]
        worst_broken+=1
print(f"Best was broken : {best_broken} times & worst was broken : {worst_broken} times")



