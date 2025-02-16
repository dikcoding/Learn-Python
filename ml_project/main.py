from data.load_data import get_data
from utils.preprocessing import preprocess_data
from models.knn_model import train_knn
from utils.evaluation import evaluate_model

def main():
    # Load Data
    X, y = get_data()

    # Preprocess Data
    X_train, X_test, y_train, y_test = preprocess_data(X, y)

    # Train Model
    model = train_knn(X_train, y_train)

    # Predict and Evaluate 
    y_pred = model.predict(X_test)  
    accuracy, report = evaluate_model(y_test, y_pred)

    # Print results
    print(f"Model Accuracy: {accuracy}")
    print(f"Classification Report:\n {report}")

if __name__ == "__main__":
    main()