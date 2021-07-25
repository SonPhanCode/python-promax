from sklearn import tree
my_tree = tree.DecisionTreeClassifier()
diem = [[10,10,10],
[8,8,8],
[7,7,7],
[9,9,9],
[10,8,7],
[8,7,9],
[6,5,4],
[1,2,3],
[6,7,8],
[7,8,9],
[6,8,10],
[5,9,10],
[10,10,5],
[5,10,10],
[10,5,10],
[8,7,6],
[7,9,10],
[9,5,8],
[6,9,10],
[8,8,10],
[8,6,9],
[9,6,10],
[9,10,6]
]
ketqua = [1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,1,1,0,1,1]
training = my_tree.fit(diem,ketqua)
xeploai2 = training.predict([[10,10,6]])
print(xeploai2)