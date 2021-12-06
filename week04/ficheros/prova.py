from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import pickle

# Cargamos los datos
data = datasets.load_iris()
iris_df = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Creamos los conjuntos de test y aprendizaje
x_train, x_test, y_train, y_test = train_test_split(iris_df, y, test_size=0.1)

# Entrenamos un árbol de decisión
dec_tree = DecisionTreeClassifier(splitter="random", criterion="entropy")
dec_tree.fit(x_train, y_train)

# Probamos el clasificador con los datos de test
y_test_predicted = dec_tree.predict(x_test)
print("Predicted classes: \t" + str(y_test_predicted))
print("Accuracy: \t\t" + str(dec_tree.score(x_test, y_test)))

# Guardamos el modelo aprendido serializado en un fichero
p = "files_folder/dec_tree_model.pickle"
with open(p, "wb") as f:
    pickle.dump(dec_tree, f)