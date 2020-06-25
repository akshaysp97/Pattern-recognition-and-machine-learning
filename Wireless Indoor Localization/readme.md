# Wireless Indoor Localization
The Wireless Indoor Localization problem comprises of using WiFi signal strengths to determine the indoor location of a user. The dataset consists of measured signal strength in dB at seven Wifi Routers (WS1-WS7) and four user locations. We employ the Wireless Indoor Localization data set to predict the location of a user who is in one of four rooms based on the WiFi signal strength received from seven routers. The dataset was divided into two sets as training data and validation data with 80% of the data kept as training data and 20% as validation data. The data is first cleaned and pre-processed by standardizing the samples. The pre-processed data is trained on different classification models to classify the samples. There were two approaches to the problem. In the first approach, we employ the given data consisting of seven input features corresponding to the seven WiFi routers on different classification algorithms to classify the data. In the second approach, we first introduce new features generated as nonlinear functions of the given seven features (nonlinear mapping). A total of 452 features are generated with regard to physical meaning of the features like mean and standard deviation of the signal power, minimum and maximum values of signal power and z-scaling. The best 40 features are then selected through feature ranking with recursive feature elimination(RFE). A total of seven classification techniques were employed in both the approaches. The Naïve Bayes Classifier is used as the baseline system in each approach. Logistic Regression, Support Vector Machine(SVM), XGBoost, K-Nearest Neighbors, Random Forest and Multi-Layer Perceptron(MLP) classifier models are implemented in each approach. For each of these models, different hyper parameters are applied using GridSearchCV and the best hyper parameters are selected. The performance of these classifiers are compared by analyzing metrics such as training accuracy, validation accuracy and mean cross validation accuracy. Results were visualized using the confusion matrix for each classifier result. The model with the highest mean cross validation accuracy in each approach was chosen as the final system to classify the test-set samples. In the first approach, the K-Nearest Neighbors classifier gave the best mean cross validation accuracy and achieved a test accuracy of 0.9825. Similarly, in the second approach, the Multi-Layer Perceptron classifier gave the best mean cross validation accuracy and achieved a test accuracy of 0.9575. In conclusion, the first approach produced the best result on the test data with the K-Nearest Neighbors classifier. K-Nearest Neighbors classifier was the best suited model to predict the location of the user. Intuitively we can attribute this to the fact that a router can be considered as a point where the signal range of the router constitutes a circle. As the K-Nearest Neighbors classifier plots the decision boundary in the form of a circle, it is the best predictor for the location of a user.