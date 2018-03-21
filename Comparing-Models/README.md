#### Premise:
Various classification machine learning algorithms were used on two datasets to compare model performance and understand different models' strengths and weaknesses.

#### Description of the two datasets:
1. [The Titanic Dataset from Kaggle.](https://www.kaggle.com/c/titanic/data)
This dataset is composed of 891 data points of passengers from the Titanic shipwreck.
The response variable is whether passengers survived and the features range from age to fare paid for the trip.
I expect this dataset to be challenging because it likely contains a lot of noise.
A disastrous situation such a shipwreck likely could not allow for clear-cut classification, for example,
one cannot say that by being wealthy or being a child guaranteed survival.
1. HR Attrition Data from Kaggle.
This dataset has 14,999 data points about employees at a fictitious company (data is simulated).
The response variable is whether an employee left the company and the features range from years of service to satisfaction level.
Most of the features numerically continuous, ordinal, and easy to understand.

The difference between these two datasets in how they appear to be complicated or simple, and whether
they will be difficult to model or not. It's not wise to judge a book by its cover
and it's probably not wise to assume data will be easier to model because it's easy to understand.

#### Data Pre-processing:
1. The original Titanic dataset has 10 features and 1 response variable. Of the 10, I removed 3:
name, ticket number, and cabin number because they were string variables with many distinct values.
While a name or cabin (related to class) could inform the response variable, I prioritized faster run time and easy
of understanding, which would both suffer if the model accounted for the various string inputs.
All factor variables were converted to numerical values for consistency.
1. The original HR Attrition dataset has 9 features and 1 response variable. All variables were kept though
factor variables where converted to numerical values.

#### Supervised Learning Algorithms used in R:
1. Decision Trees
1. Neural Networks
1. Boosting
1. Support Vector Machines (SVM)
1. K-Nearest Neighbors (KNN)

#### Results:
The primary metric for comparing model performance is with accuracy rates.

1. Titanic's Accuracy Rates:

| Model                     | Training Set | Test Set  |
| ------------------------- |:------------:| ---------:|
| Decision Tree - Pruned    | 83.0%        | 78.7%     |
| Neural Network - 2 Layers | 84.7%        | 81.5%     |
| Boosting - Pruned         | 81.1%        | 79.2%     |
| SVM - Gaussian Kernel     | 85.6%        | 82.3%     |
| KNN - k=12                | 81.7%        | 82.0%     |

1. HR Attritions's Accuracy Rates:

| Model                      | Training Set | Test Set  |
| -------------------------- |:------------:| ---------:|
| Decision Tree - Not Pruned | 97.2%        | 97.0%     |
| Neural Network - 2 Nodes   | 85.3%        | 85.1%     |
| Boosting - Pruned          | 90.3%        | 90.1%     |
| SVM - Gaussian Kernel      | 96.4%        | 96.0%     |
| KNN - k=5                  | 96.7%        | 96.3%     |




	
	
	
	
	







