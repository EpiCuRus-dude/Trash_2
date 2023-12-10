from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import shap





vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)




rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)


y_pred = rf_model.predict(X_test)
print(classification_report(y_test, y_pred))

# SHAP Values
explainer = shap.TreeExplainer(rf_model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test, feature_names=vectorizer.get_feature_names())



xgb_model = xgb.XGBClassifier()
xgb_model.fit(X_train, y_train)

# SHAP Values
explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test, feature_names=vectorizer.get_feature_names())


#####

from sklearn.linear_model import LogisticRegression

# Logistic Regression
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)


y_pred = lr_model.predict(X_test)
print(classification_report(y_test, y_pred))


explainer = shap.LinearExplainer(lr_model, X_train, feature_dependence="independent")
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test, feature_names=vectorizer.get_feature_names())


#### 

from sklearn.svm import SVC


svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)


y_pred = svm_model.predict(X_test)
print(classification_report(y_test, y_pred))

# Note: SHAP with SVM might be computationally expensive



