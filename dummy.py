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

y_pred = classifier.predict(x2)
print('Test_data   Predicted_data')
prediction = [[ y2[i],y_pred[i]] for i in range(len(y_pred))]
for i in prediction:
    print(i)
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y2, y_pred)
print("Confusion Matrix: \n",cm)
accuracy = 100 * accuracy_score(y2, y_pred)
print("Accuracy is: \n%2.2f" % accuracy,"%")

Err = y_pred - y2
print("Resulting error is", Err)
print('Total no of samples misclassified =', sum(abs(Err)))