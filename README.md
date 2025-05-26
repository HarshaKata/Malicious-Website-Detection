# CMPE255FinalProject

# Problem Statement
In today’s society, phishing has become one of the most popular cyberattacks. Many online users often press links and have sensitive user information stolen without their knowledge. Although phishing is inherently simple and can be avoided easily, the majority of victims fall for phishing due to carelessness. Phishing usually targets human mistakes and weaknesses compared to other cyberattacks that focus on vulnerabilities in the hardware or software. Our project aims to build a classifier that will predict whether a URL is phishing or legitimate.

# Group Members
Eric Pham, Student ID: 014900964

Sai Sujith Valluru, Student ID: 018174195

Venkata Sai Sri Harsha Kata, Student ID: 017604522

# Dataset Link
https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset

This dataset contains a total of 235,795 samples of website URLs, with a distribution of 134,850 legitimate URLs and 100,945 phishing URLs. The dataset has a total of 54 features that were extracted from both the source code of the website and the URL. The features consist of elements that are typically used to determine if a website URL is phishing, like URL length, suspicious characters in the URL, and the number of external links/redirects. For general data preprocessing, we dropped all the categorical features that we weren’t going to use, applied one-hot encoding to the categorical column we were using, and scaled the numerical features using StandardScaler.


# Instructions to run the Jupyter notebook
1. Clone the GitHub repo or make sure you have these files downloaded: PhiUSIIL_Phishing_URL_Dataset.csv, Updated_model(1).ipynb, and url_classifier_model.joblib.
2. After having the files downloaded, you can run and open the Jupyter notebook.
3. In the Jupyter notebook, run the first cell block to ensure you have all the necessary libraries installed. You can also run the following command to download all the necessary libraries:

`pip install pandas numpy joblib matplotlib seaborn scikit-learn xgboost tldextract beautifulsoup4 requests`
4. Once you have all the libraries installed, you can run everything on the Jupyter notebook, but every code block has an output.
5. To run the URL prediction, make sure you run the cell block with the function train_model_and_save to export the joblib model. Afterwards, you can run the function test_random_url and change the URL to test the model.

