from sklearn.datasets import load_iris
dataset = load_iris()

print("Data: ",dataset.data)
print("Target: ",dataset.target)
print("Feature_names", dataset.feature_names)
print("Target names: ",dataset.target_names)

X = dataset.data
y = dataset.target

from sklearn.model_selection import train_test_split
x1,x2,y1,y2 = train_test_split(X,y,test_size=0.2,random_state=1)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(x1,y1)
print('Accuracy:\n', classifier.score(x2,y2))

prediction = classifier.predict(x2)
print("Predicted Data:\n", prediction)

Err = prediction - y2
print("Resulting error is", Err)
print('Total no of samples misclassified =', sum(abs(Err)))