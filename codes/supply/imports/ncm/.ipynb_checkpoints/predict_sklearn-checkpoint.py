def predict_sklearn(model,X_train,y_train,X_pred):
    model.fit(X_train,y_train)
    pred=model.predict(X_pred)
    return pred

print('pred=predict_sklearn(model,X_train,y_train,X_pred)')