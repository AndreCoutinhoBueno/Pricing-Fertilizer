import pandas as pd

def predict_sklearn(model,X_train,y_train,X_pred):
    model.fit(X_train,y_train)
    pred=model.predict(X_pred)
    return pred

def s_d_ensembled_pred(model_c,model_r,train,pred):
    
    # Class
    train=train.assign(oc=1)
    train.loc[train.kg==0,'oc']=0
    X_train=train.drop(columns=['kg','fob','oc'])
    y_train=train.oc
    X_pred=pred.drop(columns=['kg','fob','oc'])
    pred_c=X_pred.assign(oc_pred=predict_sklearn(model_c,X_train,y_train,X_pred))
    
    # Regress
    X_train=train[train.oc==1].drop(columns=['kg','fob','oc'])
    y_train=train[train.oc==1][['kg','fob']]
    X_pred_r=pred_c[pred_c.oc_pred==1].drop(columns=['oc_pred'])
    pred_r=predict_sklearn(model_r,X_train,y_train,X_pred_r)
    pred_r=pd.DataFrame({'kg_pred':[pred_r[0][0]],'fob_pred':[pred_r[0][1]]})
    pred_r=pd.concat([X_pred_r.reset_index(drop=True),pred_r],axis=1)
    # Ensembled predictions
    #ensembled_pred=pred_c.merge(pred_r,how='outer')
    return pred_c, pred_r #ensembled_pred





def Back_from_dummies(comex_dumm):
    o=comex_dumm[comex_dumm.columns[~comex_dumm.columns.str.contains('~')]]    
    prdt=pd.from_dummies(comex_dumm[comex_dumm.columns[comex_dumm.columns.str.contains('Product')]],sep='~')    
    month=pd.from_dummies(comex_dumm[comex_dumm.columns[comex_dumm.columns.str.contains('month')]],sep='~')    
    uf=pd.from_dummies(comex_dumm[comex_dumm.columns[comex_dumm.columns.str.contains('UF')]],sep='~')    
    comex=pd.concat([o,prdt,month,uf],axis=1)
    return comex




def pred_next_month(model_c,model_r, comex_sprs_hip, prdt_foco, uf_foco):
    import pandas as pd
    from pandas.tseries.offsets import DateOffset
    csh=comex_sprs_hip
    train=csh.copy()
    
    
    pred_date = csh.date.astype('datetime64[ns]').max()+DateOffset(months=1)
    
    pred=pd.DataFrame({
        'date':[pred_date],
        'year':[pred_date.year],
        'month':[pred_date.month],
        'Product':[prdt_foco],
        'UF':[uf_foco]
        })

    
    train_pred=pd.concat([train,pred])
    
    train_pred[['month','Product','UF']]=train_pred[['month','Product','UF']].astype(str)
    
    train_pred_dumm=pd.get_dummies(train_pred, prefix_sep='~')

    train_pred_dumm.date=train_pred_dumm.date.astype(int)

    train=train_pred_dumm[train_pred_dumm.date!=train_pred_dumm.date.max()]
    pred=train_pred_dumm[train_pred_dumm.date==train_pred_dumm.date.max()]
    
    
    pred_c, pred_r=s_d_ensembled_pred(model_c,model_r,train,pred)

    pred_c_r=pred_c.merge(pred_r)

    pred_c_r=Back_from_dummies(pred_c_r)

    pred_c_r.date=pred_c_r.date.astype('datetime64[ns]')

    return pred_c_r

print('pred_next_month_df = pred_next_month(model_c,model_r, comex_s_d, prdt_foco, uf_foco, month_foco)')