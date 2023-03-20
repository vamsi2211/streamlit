# #STREAMLIT APP 1 !!!!!!!!!!!!!!!!
import numpy as np
import pandas as pd
import pickle
import streamlit as st

# import json
# import requests
  
# from streamlit_lottie import st_lottie
  
# url = requests.get(
#     "https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json")
# # Creating a blank dictionary to store JSON file,
# # as their structure is similar to Python Dictionary
# url_json = dict()
  
# if url.status_code == 200:
#     url_json = url.json()
# else:
#     print("Error in the URL")
  
  
# st.title("Auto Insurence Claim Fraud Detection")
  
# st_lottie(url_json)

# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)


# def predict_note_authentication(CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,\
# SeverityOfIncident,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddresse,IncidentTime,NumberOfVehicles,\
# PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfTotalClaim,AmountOfInjuryClaim,AmountOfPropertyClaim,\
# AmountOfVehicleDamage,InsuredAge, InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,InsuredHobbies,\
# CapitalGains,CapitalLoss,Country,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,\
# Policy_CombinedSingleLimit,Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,ReportedFraud,VehicleID,\
# VehicleModel,VehicleMake,VehicleYOM):
#     prediction=classifier.predict([[CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,\
# SeverityOfIncident,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddress,IncidentTime,NumberOfVehicles,\
# PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfTotalClaim,AmountOfInjuryClaim,AmountOfPropertyClaim,\
# AmountOfVehicleDamage,InsuredAge, InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,InsuredHobbies,\
# CapitalGains,CapitalLoss,Country,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,\
# Policy_CombinedSingleLimit,Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,ReportedFraud,VehicleID,\
# VehicleModel,VehicleMake,VehicleYOM]])
#     print(prediction)
#     return prediction


def main():
    st.title("Insurer Details")
    with st.form(key='columns_in_form1'):
      d1, d2, d3, d4 = st.columns(4)
      with d1:
          CustomerID = st.text_input("CustomerID",value='Cust10000'	)
      with d2:
          DateOfIncident = st.text_input("DateOfIncident",value='2015-02-03')
      with d3:
          TypeOfIncident = st.text_input("TypeOfIncident",value='Multi-vehicle Collision')
      with d4:
          TypeOfCollission = st.text_input("TypeOfCollission",value='Side Collision')
      submitButton = st.form_submit_button(label = 'Submit1')


    with st.form(key='columns_in_form2'):
      c1, c2, c3, c4, c5 = st.columns(5)
      with c1:
          SeverityOfIncident = st.text_input("SeverityOfIncident",value='Total Loss'	)
      with c2:
          AuthoritiesContacted = st.text_input("AuthoritiesContacted",value='Police')
      with c3:
          IncidentState = st.text_input("IncidentState",value='State7')
      with c4:
          IncidentCity = st.text_input("IncidentCity",value='City1')
      with c5:
          IncidentAddress = st.text_input("IncidentAddress",value='Location 1311')
      submitButton = st.form_submit_button(label = 'Submit2')

    with st.form(key='columns_in_form3'):
      b1, b2, b3, b4 = st.columns(4)
      with b1:
          IncidentTime = st.number_input("IncidentTime",value=17)
      with b2:
          NumberOfVehicles = st.number_input("NumberOfVehicles",value=3)
      with b3:
          PropertyDamage = st.text_input("PropertyDamage",value='YES')
      with b4:
          BodilyInjuries = st.number_input("BodilyInjuries",value=1)
      submitButton = st.form_submit_button(label = 'Submit3')

    with st.form(key='columns_in_form4'):
      a1, a2, a3, a4, a5, a6 = st.columns(6)
      with a1:
          Witnesses = st.number_input("Witnesses",value=46013)
      with a2:
          PoliceReport = st.text_input("PoliceReport",value='YES')
      with a3:
          AmountOfInjuryClaim = st.number_input("AmountOfInjuryClaim",value=13417)
      with a4:
          AmountOfPropertyClaim = st.number_input("AmountOfPropertyClaim",value=6071)
      with a5:
          AmountOfVehicleDamage = st.number_input("AmountOfVehicleDamage",value=46013)
      submitButton = st.form_submit_button(label = 'Submit4')

    with st.form(key='columns_in_form5'):
      z1, z2, z3, z4 = st.columns(4)
      with z1:
          InsuredAge = st.number_input("InsuredAge",value=35)
      with z2:
          InsuredZipCode = st.number_input("InsuredZipCode",value=454776)
      with z3:
          InsuredGender = st.text_input("InsuredGender",value='MALE')
      with z4:
          InsuredEducationLevel = st.text_input("InsuredEducationLevel",value='JD')
      submitButton = st.form_submit_button(label = 'Submit5')

    with st.form(key='columns_in_form6'):
      z1, z2, z3, z4 = st.columns(4)
      with z1:
          InsuredOccupation = st.text_input("InsuredOccupation",value='armed-forces')
      with z2:
          InsuredHobbies = st.text_input("InsuredHobbies",value='movies')
      with z3:
          CapitalGains = st.number_input("CapitalGains",value=56700)
      with z4:
          CapitalLoss = st.number_input("CapitalLoss",value=-48500)
      submitButton = st.form_submit_button(label = 'Submit6')

    with st.form(key='columns_in_form7'):
      z1, z2, z3, z4 = st.columns(4)
      with z1:
          InsurancePolicyNumber = st.number_input("InsurancePolicyNumber",value=110122)
      with z2:
          CustomerLoyaltyPeriod = st.number_input("CustomerLoyaltyPeriod",value=328)
      with z3:
          DateOfPolicyCoverage = st.text_input("DateOfPolicyCoverage",'2014-10-17')
      with z4:
          InsurancePolicyState = st.text_input("InsurancePolicyState",value='State3')
      submitButton = st.form_submit_button(label = 'Submit7')

    with st.form(key='columns_in_form8'):
      z1, z2, z3, z4, z5 = st.columns(5)
      with z1:
          Policy_CombinedSingleLimit = st.text_input("Policy_CombinedSingleLimit",value='250/500')
      with z2:
          Policy_Deductible = st.number_input("Policy_Deductible",value=1000)
      with z3:
          PolicyAnnualPremium = st.number_input("PolicyAnnualPremium",value=1406.91)	
      with z4:
          UmbrellaLimit = st.number_input("UmbrellaLimit",value=0)
      with z5:
          InsuredRelationship = st.text_input("InsuredRelationship",value='husband')
      submitButton = st.form_submit_button(label = 'Submit8')

    with st.form(key='columns_in_form9'):
      z1, z2, z3, z4 = st.columns(4)
      with z1:
          VehicleID = st.text_input("VehicleID",value='Vehicle26917')
      with z2:
          VehicleModel = st.text_input("VehicleModel",value='Audi')
      with z3:
          VehicleMake = st.text_input("VehicleMake",value='A5')
      with z4:
          VehicleYOM = st.text_input("VehicleYOM",value=2008)
      submitButton = st.form_submit_button(label = 'Submit9')
    df_test_final = pd.DataFrame([[CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,SeverityOfIncident,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddress,IncidentTime,NumberOfVehicles,PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfInjuryClaim,AmountOfPropertyClaim,AmountOfVehicleDamage,InsuredAge,InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,InsuredHobbies,CapitalGains,CapitalLoss,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,Policy_CombinedSingleLimit,Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,VehicleID,VehicleModel,VehicleMake,VehicleYOM]],columns='CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,SeverityOfIncident,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddress,IncidentTime,NumberOfVehicles,PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfInjuryClaim,AmountOfPropertyClaim,AmountOfVehicleDamage,InsuredAge,InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,InsuredHobbies,CapitalGains,CapitalLoss,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,Policy_CombinedSingleLimit,Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,VehicleID,VehicleModel,VehicleMake,VehicleYOM'.split(','))
    # assigning int and removing insured zip code from int float cols to num_cols

    int_cols = list(df_test_final.select_dtypes(include = "int").columns)
    int_cols.remove("InsuredZipCode")
    int_cols.remove("InsurancePolicyNumber")
    float_cols = list(df_test_final.select_dtypes(include = "float").columns)
    num_cols = int_cols+float_cols
    
    
    cat_cols_test = ['SeverityOfIncident','IncidentAddress','InsuredRelationship','AuthoritiesContacted','InsuredOccupation','InsurancePolicyState','VehicleMake','TypeOfIncident','TypeOfCollission','CustomerID','InsuredHobbies','VehicleYOM','DateOfPolicyCoverage','InsuredGender','InsurancePolicyNumber','VehicleID','IncidentCity','PropertyDamage','PoliceReport','VehicleModel','IncidentState','Policy_CombinedSingleLimit','InsuredEducationLevel','DateOfIncident','InsuredZipCode']
    time_cols = ['DateOfIncident','DateOfPolicyCoverage']
    
    from datetime import datetime
    for i in cat_cols_test:
        df_test_final[i] = df_test_final[i].astype("category") 
    for i in num_cols:
        df_test_final[i] = df_test_final[i].astype("float")
    for i in time_cols:
        df_test_final[i] = pd.to_datetime(df_test_final[i])
        
    df_test_final["diff_between_incident_policy_taken"] = df_test_final["DateOfIncident"].dt.year - df_test_final["DateOfPolicyCoverage"].dt.year
    
    df_test_final["year_of_incident"] = df_test_final["DateOfIncident"].dt.year
    df_test_final["VehicleYOM"] = df_test_final["VehicleYOM"].astype("int")
    df_test_final["vehicle_age"] = df_test_final["year_of_incident"] - df_test_final["VehicleYOM"]
    df_test_final["VehicleYOM"] = df_test_final["VehicleYOM"].astype("category")
    
    test_drop_cols = ["CustomerID","InsurancePolicyNumber","VehicleID","DateOfIncident","DateOfPolicyCoverage","VehicleYOM","PoliceReport"]
    df_test_final.drop(test_drop_cols,axis=1,inplace=True)
    
    
    
    with open('imputer.pkl', 'rb')as f1:
        imputer = pickle.load(f1)
    real_test_df_vehiclemake_witness_gender = pd.DataFrame(imputer.transform(df_test_final[["VehicleMake","Witnesses","InsuredGender"]]),columns = ["VehicleMake","Witnesses","InsuredGender"])
    with open('imputer1.pkl', 'rb')as f2:
        imputer1 = pickle.load(f2)
    real_test_df_premium_time = pd.DataFrame(imputer1.transform(df_test_final[["PolicyAnnualPremium","IncidentTime"]]),columns = ["PolicyAnnualPremium","IncidentTime"])
    df_test_final.drop(["VehicleMake","Witnesses","InsuredGender","IncidentTime","PolicyAnnualPremium"],axis=1 ,inplace =True)
    
    df_test_final = pd.concat([df_test_final,real_test_df_vehiclemake_witness_gender, real_test_df_premium_time],axis=1)
    ord_cols = ["SeverityOfIncident","BodilyInjuries","NumberOfVehicles","Witnesses","InsuredEducationLevel"]
    nom_cols = ["TypeOfIncident","TypeOfCollission","AuthoritiesContacted","InsuredOccupation","InsuredHobbies","IncidentCity","IncidentState","InsurancePolicyState","InsuredGender","InsuredRelationship",'Policy_CombinedSingleLimit',"PropertyDamage",]
    num_cols = [ "AmountOfInjuryClaim","AmountOfPropertyClaim","InsuredAge","CustomerLoyaltyPeriod","Policy_Deductible","PolicyAnnualPremium","IncidentTime","AmountOfVehicleDamage" ,"CapitalGains","CapitalLoss","UmbrellaLimit"]
    st.dataframe(df_test_final, use_container_width=True)



    result=""
    if st.button("Predict"):
#     result=predict_note_authentication(CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,SeverityOfIncident,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddress,IncidentTime,NumberOfVehicles,PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfTotalClaim,AmountOfInjuryClaim,AmountOfPropertyClaim,AmountOfVehicleDamage,InsuredAge, InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,InsuredHobbies,CapitalGains,CapitalLoss,Country,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,Policy_CombinedSingleLimit,Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,ReportedFraud,VehicleID,VehicleModel,VehicleMake,VehicleYOM)
      st.success('The output is {}'.format(result))
       
    

if __name__=='__main__':
    main()
    
    
    


