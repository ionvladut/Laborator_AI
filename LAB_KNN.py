#EX 1
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
iris= load_iris()
X= iris.data
Y= iris.target


print("Forma setului de date:", X.shape)
print("\nDenumirile atributelor:")
print(iris.feature_names)
print("\nClasele:")
print(iris.target_names) 

#EX 2
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
print(X)
print(Y)

#EX 3
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
print(x_train_scaled[:5])
print(x_test_scaled[:5])

#EX 4
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(x_train_scaled, y_train)
acuratete = knn.score(x_test_scaled, y_test)
print(acuratete)

#EX 5
for k in range(1,16):
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(x_train_scaled,y_train)
    acuratete = knn.score(x_test_scaled, y_test)
    print(acuratete)

k_values = []
accuracies = []

for k in range(1, 16):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train_scaled, y_train)

    accuracy = knn.score(x_test_scaled, y_test)

    k_values.append(k)
    accuracies.append(accuracy)

    print(f"k = {k}, accuracy = {accuracy}")

plt.plot(k_values, accuracies, marker='o')
plt.xlabel("Number of Neighbors (k)")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy for Different k Values")
plt.xticks(range(1, 16))
plt.grid(True)

plt.show()

#EX 6
# a)
y_pred = knn.predict(x_test_scaled)
matrice_confuzie = confusion_matrix(y_test, y_pred)
print(matrice_confuzie)

# b)
report = classification_report(y_test, y_pred, target_names = iris.target_names)
print(report)