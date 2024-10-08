def last_date_test(model_c,model_r, comex_sprs_dumm_t, target_cols):
    csdt=comex_sprs_dumm_t
    train_s_d_t=csdt[csdt.date<csdt.date.max()]
    test_s_d_t =csdt[csdt.date==csdt.date.max()]
    X_pred_s_d_t=test_s_d_t.drop(columns=target_cols+['oc'])
    y_test_c_r=test_s_d_t[['oc']+target_cols]    
    pred_c_r=pred_c_r(model_c,model_r,train_s_d_t,X_pred_s_d_t,target_cols)
    test_pred_c_r=pd.concat([pred_c_r,y_test_c_r])