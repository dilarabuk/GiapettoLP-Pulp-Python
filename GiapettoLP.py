TOYS = ["soldiers","trains"] #i
MONEY = ["price","material","labor"] #k
HOURS = ["finishing","carpentry"] #j
a = {"finishing":100,"carpentry":80}
d = {"soldiers":40,"trains":50}
m = {"price":{"soldiers":27,"trains":21},"material":{"soldiers":-10,"trains":-9},"labor":{"soldiers":-14,"trains":-10}}
h = {"finishing":{"soldiers":2,"trains":1},"carpentry":{"soldiers":1, "trains":1}}

gpt = LpProblem("Giapetto_Profit_Maximization",LpMaximize)

X = LpVariable.dicts("number_of",TOYS, lowBound = 0, cat = "Integer")#Amount of soldiers and trains

gpt += lpSum(lpSum([[X[i]*m[k][i] for k in MONEY] for i in TOYS]))

gpt += lpSum([X[i]*h["finishing"][i] for i in TOYS]) <= a["finishing"]

gpt += lpSum([X[i]*h["carpentry"][i] for i in TOYS]) <= a["carpentry"]

gpt += [X[i] for i in TOYS] <= [d[i] for i in TOYS]

print(gpt)

status = gpt.solve()
status = LpStatus[status]

for i in TOYS:
    print(X[i],(X[i]).varValue)

