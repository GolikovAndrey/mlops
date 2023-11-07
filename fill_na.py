import pandas as pd

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

for col in test.columns:
    if test[col].dtypes == object:
        train[col] = train[col].fillna(train[col].mode())
        test[col] = test[col].fillna(test[col].mode())
        continue
    train[col] = train[col].fillna(train[col].median())
    test[col] = test[col].fillna(test[col].median())

train.to_csv("data/stage1/train.csv")
test.to_csv("data/stage1/test.csv")