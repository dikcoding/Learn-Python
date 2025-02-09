from abc import ABC, abstractmethod
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

# Abstract Class (Abstraction)
class MLModel(ABC):
    def __init__(self, model_name):
        self._model_name = model_name  # Encapsulation
        self._model = None  # Encapsulation
    
    @abstractmethod
    def train(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass
    
    def evaluate(self, X, y):
        y_pred = self.predict(X)
        accuracy = np.mean(y_pred == y)
        print(f"Accuracy of {self._model_name}: {accuracy:.2f}")
        return accuracy
    
    @classmethod
    def model_class_method(cls):
        print(f"This is a class method of {cls.__name__}")
    
    @staticmethod
    def model_static_method():
        print("This is a static method of MLModel class")
    
# Subclass for Linear Regression (Inheritance)
class LinearRegressionModel(MLModel):
    def __init__(self):
        super().__init__("Linear Regression")
        self._model = LinearRegression()  # Encapsulation
    
    def train(self, X, y):
        self._model.fit(X, y)
        print(f"{self._model_name} model trained")
    
    def predict(self, X):
        return self._model.predict(X)

# Subclass for Decision Tree Classifier (Inheritance)
class DecisionTreeModel(MLModel):
    def __init__(self):
        super().__init__("Decision Tree")
        self._model = DecisionTreeClassifier()  # Encapsulation

    def train(self, X, y):
        self._model.fit(X, y)
        print(f"{self._model_name} model trained")
    
    def predict(self, X):
        return self._model.predict(X)

# Function to demonstrate polymorphism
def make_prediction(model: MLModel, X):
    return model.predict(X)

# Example usage
if __name__ == "__main__":
    # Sample Data
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([1, 2, 2, 3])

    # Linear Regression Model
    lr_model = LinearRegressionModel()
    lr_model.train(X_train, y_train)
    lr_predictions = lr_model.predict(X_train)
    lr_model.evaluate(X_train, y_train)

    # Decision Tree Model
    dt_model = DecisionTreeModel()
    dt_model.train(X_train, y_train)
    dt_predictions = dt_model.predict(X_train)
    dt_model.evaluate(X_train, y_train)

    # Demonstrating Polymorphism
    print("Using polymorphism to make predictions:")
    print("Linear Regression predictions:", make_prediction(lr_model, X_train))
    print("Decision Tree predictions:", make_prediction(dt_model, X_train))

    # Calling class method
    MLModel.model_class_method()  # Outputs: This is a class method of MLModel

    # Calling static method
    MLModel.model_static_method()  # Outputs: This is a static method of MLModel class