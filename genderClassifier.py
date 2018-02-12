from sklearn import tree

#[height, weight, shoe size]
X=[[180,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,47], [175,64,39], [177,70,40], [159,59,38],
[177,75,42], [181,85,43], [157,57,39]]

Y=['male', 'female', 'female','female', 'male','male','male','female','male','female','male','female']

clf=tree.DecisionTreeClassifier()

clf=clf.fit(X,Y)

height=int(input("What is the height(in cms): \n"))
weight=int(input("What is the weight(kgs): \n"))
shoeSize=int(input("What is the shoe size(european): \n"))

new=[height,weight,shoeSize]
prediction=clf.predict([new])

print(prediction)
