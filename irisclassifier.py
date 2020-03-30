from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

def classify(demolst):
     X_demo = np.array([demolst])
     
     iris = load_iris()
     #print(iris["data"])
     
     X_train,X_test,y_train,y_test = train_test_split(iris["data"],iris["target"],random_state=0)
     
     knn = KNeighborsClassifier(n_neighbors=4)
     knn.fit(X_train,y_train)
     #print(knn.score(X_test,y_test))
     
     target_index = knn.predict(X_demo)[0]
     
     return [iris.target_names[target_index],target_index]

if __name__ == "__main__":
     demolst = [7.4,2.8,6.0,1.4]     
     print(classify(demolst))