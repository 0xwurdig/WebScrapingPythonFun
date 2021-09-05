from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://HK:hanugolu@cluster0.3uliq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
myhero= [1,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,19,20,21,22,23,25,31,26,27,28,29,30,32,33,35,36,39,40,41,42,43,44,45,47,48,49,50,54,56,59,60,62,63,67,69,68,71,72,73,75,76,81,83,84,85,86,87,88,89,90,93,94,95,96,97,98,99,100,101,102,104,109,114,120,121,129,135]
db = client['DOTA2']
matches = db['matches']
asd = []
dsa = {}
print("Enter winning team \n")
try:
    win = []  
    while True:
        win.append(int(input()))
except:
    pass
print("Enter loseing team \n")
try:
    lose = []  
    while True:
        lose.append(int(input()))
except:
    pass
for i in range(0, 5):
    ele = int(input())
  
    lst.append(ele)
for i in list(matches.find({"win": {'$all':win}, "lose" : {'$all': lose}})):
    a = ''
    for j in i['win']:
        if j not in win and j in myhero:
            a = a + '//' + str(j)
    if a == '':
        continue
    if a not in asd:
        asd.append(a)
        dsa[a] = []
        dsa[a].append(i['match_id'])
    else:
        dsa[a].append(i['match_id'])
sorted_list =  sorted(dsa, key=lambda k: len(dsa[k]), reverse=True)
for  i in range(10):
    print(sorted_list[i] +'-------------------'+ str(sorted_list[i]))
print(sorted_dict)
    