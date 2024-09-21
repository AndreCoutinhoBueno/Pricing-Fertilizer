def prev_score(ano_mes_ncm_uf):

    imp_fert=imp_fert[imp_fert.KG_LIQUIDO>0]
    
    imp_fert[['CO_ANO','CO_MES','CO_NCM','SG_UF_NCM']]=imp_fert[['CO_ANO','CO_MES','CO_NCM','SG_UF_NCM']].astype('category')
    
    imp_fert=imp_fert.groupby(observed=False,by=['CO_ANO','CO_MES','CO_NCM','SG_UF_NCM'])[['KG_LIQUIDO']].sum().reset_index()
    
    
    imp_fert=imp_fert.assign(date=pd.to_datetime(imp_fert.CO_ANO.astype(str)+'/'+imp_fert.CO_MES.astype(str)+'/1').astype(int))\
    .drop(columns='CO_ANO')

    max_depth=5
    from sklearn.ensemble import RandomForestClassifier as RFC
    RFC=RFC(max_depth=max_depth)
    from sklearn.ensemble import RandomForestRegressor as RFR
    RFR=RFR(max_depth=max_depth)



    result=pd.DataFrame()
    a=0
    for date in imp_fert.date.unique():
        
        imp_fert_t1=imp_fert[imp_fert.date<=date]
    
        imp_fert_t1=imp_fert_t1.assign(oc=0)
        imp_fert_t1.loc[imp_fert_t1.KG_LIQUIDO!=0,'oc']=1
        
        imp_fert_dumm=pd.get_dummies(imp_fert_t1)
        
        train=imp_fert_dumm[imp_fert_dumm.date<imp_fert_dumm.date.max()]
        test=imp_fert_dumm[imp_fert_dumm.date==imp_fert_dumm.date.max()]
        test_pred=imp_fert_t1[imp_fert_t1.date==imp_fert_t1.date.max()]
    
        if len(train)>=6*12:
        
        
            X_train=train.drop(columns=['KG_LIQUIDO','oc'])
            y_train_c=train.oc
            y_train_r=train.KG_LIQUIDO
            X_test=test.drop(columns=['KG_LIQUIDO','oc'])
            y_test_c=test.oc
            y_test_r=test.KG_LIQUIDO
            
            
            RFC.fit(X_train,y_train_c)
            test_pred=test_pred.assign(oc_pred=RFC.predict(X_test))
            
            if (test_pred.oc.values[0]==1)&(test_pred.oc_pred.values[0]==1):
                RFR.fit(X_train,y_train_r)
                test_pred=test_pred.assign(kg_pred=RFR.predict(X_test))
            else:
                test_pred=test_pred.assign(kg_pred=0)
            
            result=pd.concat([result,test_pred])


    from sklearn import metrics
    
    q=pd.DataFrame()
    for ncm in result.CO_NCM.unique():
        for uf in result.SG_UF_NCM.unique():
            
            result_t=result[(result.CO_NCM==ncm)&(result.SG_UF_NCM==uf)]
    
            result_t=result_t\
            .assign(accuracy =metrics.accuracy_score (result_t.oc,result_t.oc_pred))\
            .assign(precision=metrics.precision_score(result_t.oc,result_t.oc_pred))\
            .assign(recall   =metrics.recall_score   (result_t.oc,result_t.oc_pred))
            
            result_t2=result_t[(result_t.oc==1)&(result_t.oc_pred==1)]
            
            result_t=result_t.assign(r2=metrics.r2_score(result_t2.KG_LIQUIDO,result_t2.kg_pred))
    
            result_t=result_t[['CO_NCM','SG_UF_NCM','accuracy','precision','recall','r2']].drop_duplicates()
            
            q=pd.concat([q,result_t])
    
    q.accuracy.mean()
    
    q.precision.mean()
    
    q.recall.mean()
    
    q.r2.mean()
    
    return q

    print('Disponível função prev_score(ano_mes_ncm_uf)')