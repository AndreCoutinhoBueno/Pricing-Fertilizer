def s_d_ensemble_pred(model_c,model_r,train,X_pred):
    
    import pandas as pd
    
    def predict_sklearn(model,X_train,y_train,X_pred):
        model.fit(X_train,y_train)
        pred=model.predict(X_pred)
        return pred
        
    # Class
    train=train.assign(oc=1)
    train.loc[train.kg==0,'oc']=0
    X_train=train[X_pred.columns]
    y_train=train.oc
    pred_c=X_pred.assign(oc_pred=predict_sklearn(model_c,X_train,y_train,X_pred))
    
    # Regress
    train=train[train.oc==1]
    X_train=train[X_pred.columns]
    y_train=train[[x for x in train.columns if x not in X_pred.columns]]
    X_pred_r=pred_c[pred_c.oc_pred==1].drop(columns='oc_pred')
    pred_r=predict_sklearn(model_r,X_train,y_train,X_pred_r)
    pred_r=pd.DataFrame({'kg_pred':[pred_r[0][0]],'fob_pred':[pred_r[0][1]]})
    pred_r=pd.concat([X_pred_r.reset_index(drop=True),pred_r],axis=1)
    # Ensembled predictions
    ensemble_pred=pred_c.merge(pred_r,how='outer')
    return ensemble_pred

print('ensemble_pred = s_d_ensemble_pred(model_c,model_r,train,X_pred)')