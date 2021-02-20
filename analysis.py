# This file contains analysis on the training and unlabeled data in order to
# predit whether a patient is diagnosed with diabetes.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

train_data = "Desktop/Project/WiDS-Datathon-2021/TrainingWiDS2021.csv"
test_data = "Desktop/Project/WiDS-Datathon-2021/UnlabeledWiDS2021.csv"

train_df = pd.read_csv(train_data)
test_df = pd.read_csv(test_data)



