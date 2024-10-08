import pandas as pd

def predict_sklearn(model,X_train,y_train,X_pred):
    model.fit(X_train,y_train)
    pred=model.predict(X_pred)
    return pred

def s_d_ensemble_pred(model_c,model_r,train,X_pred):
    
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


def Back_from_dummies(comex_dumm):
    o=comex_dumm[comex_dumm.columns[~comex_dumm.columns.str.contains('~')]]    
    prdt=pd.from_dummies(comex_dumm[comex_dumm.columns[comex_dumm.columns.str.contains('Product')]],sep='~')    
    month=pd.from_dummies(comex_dumm[comex_dumm.columns[comex_dumm.columns.str.contains('month')]],sep='~')    
    uf=pd.from_dummies(comex_dumm[comex_dumm.columns[comex_dumm.columns.str.contains('UF')]],sep='~')    
    comex=pd.concat([o,prdt,month,uf],axis=1)
    return comex

def last_date_test(model_c,model_r, comex_s_d):
    csd=comex_s_d
    train=csd[csd.date<csd.date.max()]
    test_ld =csd[csd.date==csd.date.max()]
    X_pred_ld=test_ld.drop(columns=['kg','fob']+['oc'])
    y_test_ld=test_ld[['oc']+['kg','fob']]    
    ensemble_pred_ld=s_d_ensemble_pred(model_c,model_r,train,X_pred_ld)
    ensemble_test_pred_ld=pd.concat([ensemble_pred_ld,y_test_ld.reset_index(drop=True)],axis=1)
    ensemble_test_pred_ld=Back_from_dummies(ensemble_test_pred_ld)
    return ensemble_test_pred_ld

print('ensemble_test_pred_ld = last_date_test(model_c,model_r, comex_sprs_dumm)')