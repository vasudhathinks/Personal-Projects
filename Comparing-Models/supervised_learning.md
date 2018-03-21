#### Supervised Learning Algorithms:
1. Decision Trees
1. Neural Networks
1. Boosting
1. Support Vector Machines (SVM)
1. K-Nearest Neighbors (KNN)

#### Data Pre-processing:
1. The original Titanic dataset has 10 features and 1 response variable. Of the 10, I removed 3:
name, ticket number, and cabin number because they were string variables with many distinct values.
While a name or cabin (related to class) could inform the response variable, I prioritized faster run time and easy
of understanding, which would both suffer if the model accounted for the various string inputs.
All factor variables were converted to numerical values for consistency.
1. The original HR Attrition dataset has 9 features and 1 response variable. All variables were kept though
factor variables where converted to numerical values.
1. Each dataset was split into a training and test set with 80% and 20% of the original data, respectively.

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


#### Discussion:
1. Decision Trees. It is clear that the decision trees algorithm was much better at mapping the 
HR Attrition dataset as compared to Titanic: looking at test set accuracies, we are comparing 78.7%
accuracy for Titanic and 97.0% accuracy for HR Attrition! Additionally, though the details have not been shared,
another interesting point was that the tree for Titanic only used 4 of its 7 features for mapping, while
HR Attrition used 6 of its 9 features. Finally, pruning Titanic's tree led to the same accuracy, while
additional nodes for HR continued to improve accuracy. 

1. Neural Networks. On these relatively small datasets, the neural network models did not perform very well, nor did
they have an easy time training the model when run (which is why they were only run with 2 layers or even just 2 nodes). 
It was surprising that this algorithm could not map HR Attrition well because my general sense
about that data was that it is clear and follows a known distribution (since it's simulated), 
however, it performed very poorly in comparison to the other models (85.1% test accuracy compared to others' in the 90s).
In contrast, the Titanic data performed relatively well. This speaks volumes about the algorithm, which is able to pick 
information through the noise (Titanic), but not necessarily translate clarity well (HR).

1. Boosting. This ensemble method did not perform particularly well on these datasets as compared to the others. 
This weak learner, however, does not lag far behind. With more iterations, it improved its performance and I expect
with further experimentation, it could improve.

1. SVM. Both datasets resulted in high accuracies using SVM with a Gaussian kernel (leave it to gauss to understand
data distributions). Performance on the Titanic data is more surprising and satisfying, with its relatively high accuracies 
of 85.6% on the training and 82.3% on the test set, because it was difficult to find a model or tweak parameters that
would increase accuracy above the high 70s-low 80s.

1. KNN. My favorite algorithm (and a lazy one at that). While the detail is not shared, the Titanic dataset showed that 
the more neighbors (k) used, the more accurate prediction of the response variable. On the other hand, the HR dataset 
showed that the accuracy on the test set decreased after a certain value of k (k=5). This suggests that the data points 
in HR dataset are placed close to each other for predicting to the same response variable and when additional (and further) 
points are included to make an assessment, it throws off accuracy. For the Titanic dataset, I wonder if capturing more
neighbors allows the model to incorporate more noise, which results in a more accurate reading.