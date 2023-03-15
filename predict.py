import pandas as pd
from joblib import load
from sklearn.preprocessing import StandardScaler

dataset_test = pd.read_csv('internship_hidden_test.csv')
random_forest_regressor_model = load('random_forest_regressor_model.joblib')

scaler = StandardScaler()
X_data_test = dataset_test.loc[:, "0":"52"]
X_scaled_test = pd.DataFrame(scaler.fit_transform(X_data_test))

val_predictions_test = random_forest_regressor_model.predict(X_scaled_test)
df_val_predictions_test = pd.DataFrame({'target_predictions': val_predictions_test})
df_val_predictions_test.to_csv('predictions.csv', index=False)
