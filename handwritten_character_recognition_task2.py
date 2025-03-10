# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('/content/A_Z Handwritten Data.csv')
df

# Data Preprocessing
df.head()

df.tail()

df.describe()

df.info()

df['0'].value_counts()

df.isnull().sum()

import matplotlib.pyplot as plt
import plotly.express as px
fig=px.histogram(df,x='0')
fig.show()

# Handwritten Alphabets
for i in range(26):
    filtered_df = df[df['0'] == i]
    if len(filtered_df) > 0:
        dd = filtered_df.iloc[0]
        x = dd[1:].values
        x = x.reshape((28, 28))
        plt.imshow(x, cmap='binary')
        plt.show()

x=df.drop(['0'],axis=1)
y=df['0']
print(x.head())
print(y.head())

# Split into train and test sets
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.33,random_state=42)

print(train_x.head())
print(train_y.head())

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# predict the accuracy
model = RandomForestClassifier()
model.fit(train_x, train_y)

# Make predictions on the test set
pred_y = model.predict(test_x)

# Evaluate the model's accuracy
accuracy = accuracy_score(test_y, pred_y)
print(f"Accuracy of the Random Forest Classifier: {accuracy}")

# classification report

from sklearn.metrics import classification_report

# Generate the classification report
print(classification_report(test_y, pred_y))
