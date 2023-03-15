# Project Description
This project aims to build a model that predicts a target variable based on a set of 53 anonymized features. The dataset used in this project is provided in the `internship_train.csv` file. The performance of the model will be evaluated using the Root Mean Squared Error (RMSE) metric. The final model will be used to make predictions on a test set provided in the `internship_hidden_test.csv` file.

# Requirements
To run the code in this project, you will need the following packages:

* joblib==1.2.0
* numpy==1.24.2
* pandas==1.5.3
* scikit-learn==1.1.1

You can install all packages by running `pip install -r requirements.txt`.

# Installation

* Clone the repository: `git clone https://github.com/VladShevchenko3/Test_task3.git`
* Install the required packages: `pip install -r requirements.txt`

To reproduce the analysis of this project, follow these steps:

* Run the Jupyter notebook: `jupyter notebook`
* Open the `analysis.ipynb` notebook and follow the instructions.

Note: If you don't have Jupyter Notebook installed, you can install it using the command `pip install jupyter`.

To reproduce the results of this project, follow these steps:

* Run `predict.py`
* Open the `predictions.csv` and check results.
# Usage
To train the model and make predictions on new data, follow the steps in the `analysis.ipynb` notebook. The notebook contains load the data, preprocess it, train the models, evaluate performanc and best model selection. Once the final model is trained, you can use it to make predictions on new data by running the `predict.py`. The predictions will be saved in a file named `predictions.csv`.

# References
* Scikit-learn documentation: https://scikit-learn.org/stable/documentation.html
* NumPy documentation: https://numpy.org/doc/stable/
* Pandas documentation: https://pandas.pydata.org/docs/

