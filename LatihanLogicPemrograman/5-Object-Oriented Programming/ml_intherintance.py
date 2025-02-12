from abc import ABC, abstractmethod
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier


# Abstract Superclass
class MLModel(ABC):
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = None
    
    @abstractmethod
    def train(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass
    
    def evaluate(self, X, y):
        y_pred = self.predict(X)
        accuracy = np.mean(y_pred == y)
        print(f"Accuracy of {self.model_name}: {accuracy:.2f}")
        return accuracy
    
    @classmethod
    def model_class_method(cls):
        print(f"This is a static method of MLModel class {cls.__name__}")
    
    @staticmethod
    def model_static_method():
        print(f"This is a static method of MLModel class")
    
# Subclass for linear regression
class LinearRegressionModel(MLModel):
    def __init__(self):
        super().__init__("Linear Regression")
        self.model = LinearRegression()
    
    def train(self, X, y):
        self.model.fit(X, y)
        print(f"{self.model_name} model trained")
    
    def predict(self, X):
        return self.model.predict(X)

# Subclass for decision tree classifier
class DecisionTreeModel(MLModel):
    def __init__(self):
        super().__init__("Decision Tree")
        self.model = DecisionTreeClassifier()

    def train(self, X, y):
        self.model.fit(X, y)
        print(f"{self.model_name} model trained")
    
    def predict(self, X):
        return self.model.predict(X)

# Example usage
if __name__ == "__main__":
    # Sample Data
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([1, 2, 2, 3])

    # Linear Regression Model
    lr_model = LinearRegressionModel()
    lr_model.train(X_train, y_train)
    lr_y_pred = lr_model.predict(X_train)
    lr_model.evaluate(X_train, y_train)

    # Decision Tree Model
    dt_model = DecisionTreeModel()
    dt_model.train(X_train, y_train)
    dt_y_pred = dt_model.predict(X_train)
    dt_model.evaluate(X_train, y_train)

    # Calling class method
    MLModel.model_class_method() 

    # Calling static method
    MLModel.model_static_method()
