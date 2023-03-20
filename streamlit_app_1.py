# #STREAMLIT APP 1 !!!!!!!!!!!!!!!!
import numpy as np
import pandas as pd
import pickle
import pickle
import streamlit as st 

import json
import requests
  
from streamlit_lottie import st_lottie
  
url = requests.get(
    "https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json")
# Creating a blank dictionary to store JSON file,
# as their structure is similar to Python Dictionary
url_json = dict()
  
if url.status_code == 200:
    url_json = url.json()
else:
    print("Error in the URL")
  
  
st.title("Auto Insurence Claim Fraud Detection")
  
st_lottie(url_json)

# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)


def predict_note_authentication(CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,\
SeverityOfIncident,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddress,IncidentTime,NumberOfVehicles,\
PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfTotalClaim,AmountOfInjuryClaim,AmountOfPropertyClaim,\
AmountOfVehicleDamage,InsuredAge, InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,InsuredHobbies,\
CapitalGains,CapitalLoss,Country,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,\
Policy_CombinedSingleLimit,Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,ReportedFraud,VehicleID,\
VehicleModel,VehicleMake,VehicleYOM):
    prediction=classifier.predict([[CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,\
SeverityOfIncident,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddress,IncidentTime,NumberOfVehicles,\
PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfTotalClaim,AmountOfInjuryClaim,AmountOfPropertyClaim,\
AmountOfVehicleDamage,InsuredAge, InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,InsuredHobbies,\
CapitalGains,CapitalLoss,Country,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,\
Policy_CombinedSingleLimit,Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,ReportedFraud,VehicleID,\
VehicleModel,VehicleMake,VehicleYOM]])
    print(prediction)
    return prediction
def main():
    st.title("Insurer Details")
    with st.form(key='columns_in_form1'):
      d1, d2, d3, d4 = st.columns(4)
      with d1:
          CustomerID = st.text_input("CustomerID")
      with d2:
          DateOfIncident = st.text_input("DateOfIncident")
      with d3:
          TypeOfIncident = st.text_input("TypeOfIncident")
      with d4:
          TypeOfCollission = st.text_input("TypeOfCollission")
      submitButton = st.form_submit_button(label = 'Submit1')


    with st.form(key='columns_in_form2'):
      c1, c2, c3, c4, c5 = st.columns(5)
      with c1:
          SeverityOfIncident = st.text_input("SeverityOfIncident")
      with c2:
          AuthoritiesContacted = st.text_input("AuthoritiesContacted")
      with c3:
          IncidentState = st.text_input("IncidentState")
      with c4:
          IncidentCity = st.text_input("IncidentCity")
      with c5:
          IncidentAddress = st.text_input("IncidentAddress")
      submitButton = st.form_submit_button(label = 'Submit2')

    with st.form(key='columns_in_form3'):
      b1, b2, b3, b4 = st.columns(4)
      with b1:
          IncidentTime = st.text_input("IncidentTime")
      with b2:
          NumberOfVehicles = st.text_input("NumberOfVehicles")
      with b3:
          PropertyDamage = st.text_input("PropertyDamage")
      with b4:
          BodilyInjuries = st.text_input("BodilyInjuries")
      submitButton = st.form_submit_button(label = 'Submit3')

    with st.form(key='columns_in_form4'):
      a1, a2, a3, a4, a5, a6 = st.columns(6)
      with a1:
          Witnesses = st.text_input("Witnesses")
      with a2:
          PoliceReport = st.text_input("PoliceReport")
      with a3:
          AmountOfInjuryClaim = st.text_input("AmountOfInjuryClaim")
      with a4:
          AmountOfPropertyClaim = st.text_input("AmountOfPropertyClaim")
      with a5:
#           AmountOfPropertyClaim = st.text_input("AmountOfPropertyClaim")
#       with a6:
#           AmountOfVehicleDamage = st.text_input("AmountOfVehicleDamage")
      submitButton = st.form_submit_button(label = 'Submit4')

    with st.form(key='columns_in_form5'):
      z1, z2, z3, z4 = st.columns(4)
      with z1:
          InsuredAge = st.text_input("InsuredAge")
      with z2:
          InsuredZipCode = st.text_input("InsuredZipCode")
      with z3:
          InsuredGender = st.text_input("InsuredGender")
      with z4:
          InsuredEducationLevel = st.text_input("InsuredEducationLevel")
      submitButton = st.form_submit_button(label = 'Submit5')

    with st.form(key='columns_in_form6'):
      z1, z2, z3, z4 = st.columns(4)
      with z1:
          InsuredOccupation = st.text_input("InsuredOccupation")
      with z2:
          InsuredHobbies = st.text_input("InsuredHobbies")
      with z3:
          CapitalGains = st.text_input("CapitalGains")
      with z4:
          CapitalLoss = st.text_input("CapitalLoss")
      submitButton = st.form_submit_button(label = 'Submit6')

    with st.form(key='columns_in_form7'):
      z1, z2, z3, z4 = st.columns(4)
      with z1:
          InsurancePolicyNumber = st.text_input("InsurancePolicyNumber")
      with z2:
          CustomerLoyaltyPeriod = st.text_input("CustomerLoyaltyPeriod")
      with z3:
          DateOfPolicyCoverage = st.text_input("DateOfPolicyCoverage")
      with z4:
          InsurancePolicyState = st.text_input("InsurancePolicyState")
      submitButton = st.form_submit_button(label = 'Submit7')

    with st.form(key='columns_in_form8'):
      z1, z2, z3, z4, z5 = st.columns(5)
      with z1:
          Policy_CombinedSingleLimit = st.text_input("Policy_CombinedSingleLimit")
      with z2:
          Policy_Deductible = st.text_input("Policy_Deductible")
      with z3:
          PolicyAnnualPremium = st.text_input("PolicyAnnualPremium")
      with z4:
          UmbrellaLimit = st.text_input("UmbrellaLimit")
      with z5:
          InsuredRelationship = st.text_input("InsuredRelationship")
      submitButton = st.form_submit_button(label = 'Submit8')

    with st.form(key='columns_in_form9'):
      z1, z2, z3, z4 = st.columns(4)
      with z1:
          VehicleID = st.text_input("VehicleID")
      with z2:
          VehicleModel = st.text_input("VehicleModel")
      with z3:
          VehicleMake = st.text_input("VehicleMake")
      with z4:
          VehicleYOM = st.text_input("VehicleYOM")
      submitButton = st.form_submit_button(label = 'Submit9')

# def main():
#     st.title("Insurer Details")
#     with st.form(key='columns_in_form1'):
#         d1, d2, d3, d4 = st.columns(4)
#         with d1:
#             CustomerID = st.text_input("CustomerID")
#         with d2:
#             DateOfIncident = st.text_input("DateOfIncident")
#         with d3:
#             TypeOfIncident = st.text_input("TypeOfIncident")
#         with d4:
#             TypeOfCollission = st.text_input("TypeOfCollission")
#         submitButton = st.form_submit_button(label = 'Submit1')


#     with st.form(key='columns_in_form2'):
#         c1, c2, c3, c4 = st.columns(4)
#         with c1:
#             AuthoritiesContacted = st.text_input("AuthoritiesContacted")
#         with c2:
#             IncidentState = st.text_input("IncidentState")
#         with c3:
#             IncidentCity = st.text_input("IncidentCity")
#         with c4:
#             IncidentAddress = st.text_input("IncidentAddress")
#         submitButton = st.form_submit_button(label = 'Submit2')

#     with st.form(key='columns_in_form3'):
#         b1, b2, b3, b4 = st.columns(4)
#         with b1:
#             IncidentTime = st.text_input("IncidentTime")
#         with b2:
#             NumberOfVehicles = st.text_input("NumberOfVehicles")
#         with b3:
#             PropertyDamage = st.text_input("PropertyDamage")
#         with b4:
#             BodilyInjuries = st.text_input("BodilyInjuries")
#         submitButton = st.form_submit_button(label = 'Submit3')

#     with st.form(key='columns_in_form4'):
#         a1, a2, a3, a4 = st.columns(4)
#         with a1:
#             Witnesses = st.text_input("Witnesses")
#         with a2:
#             PoliceReport = st.text_input("PoliceReport")
#         with a3:
#             AmountOfTotalClaim = st.text_input("AmountOfTotalClaim")
#         with a4:
#             AmountOfInjuryClaim = st.text_input("AmountOfInjuryClaim")
#         submitButton = st.form_submit_button(label = 'Submit4')

#     with st.form(key='columns_in_form5'):
#         z1, z2, z3, z4 = st.columns(4)
#         with z1:
#             InsuredAge = st.text_input("InsuredAge")
#         with z2:
#             InsuredZipCode = st.text_input("InsuredZipCode")
#         with z3:
#             InsuredGender = st.text_input("InsuredGender")
#         with z4:
#             InsuredEducationLevel = st.text_input("InsuredEducationLevel")
#         submitButton = st.form_submit_button(label = 'Submit5')

#     with st.form(key='columns_in_form6'):
#         z1, z2, z3, z4 = st.columns(4)
#         with z1:
#             InsuredOccupation = st.text_input("InsuredOccupation")
#         with z2:
#             InsuredHobbies = st.text_input("InsuredHobbies")
#         with z3:
#             CapitalGains = st.text_input("CapitalGains")
#         with z4:
#             CapitalLoss = st.text_input("CapitalLoss")
#         submitButton = st.form_submit_button(label = 'Submit6')

#     with st.form(key='columns_in_form7'):
#         z1, z2, z3, z4, z5 = st.columns(5)
#         with z1:
#             Country = st.text_input("Country")
#         with z2:
#             InsurancePolicyNumber = st.text_input("InsurancePolicyNumber")
#         with z3:
#             CustomerLoyaltyPeriod = st.text_input("CustomerLoyaltyPeriod")
#         with z4:
#             DateOfPolicyCoverage = st.text_input("DateOfPolicyCoverage")
#         with z5:
#             InsurancePolicyState = st.text_input("InsurancePolicyState")
#         submitButton = st.form_submit_button(label = 'Submit7')

#     with st.form(key='columns_in_form8'):
#         z1, z2, z3, z4, z5 = st.columns(5)
#         with z1:
#             Policy_CombinedSingleLimit = st.text_input("Policy_CombinedSingleLimit")
#         with z2:
#             Policy_Deductible = st.text_input("Policy_Deductible")
#         with z3:
#             PolicyAnnualPremium = st.text_input("PolicyAnnualPremium")
#         with z4:
#             UmbrellaLimit = st.text_input("UmbrellaLimit")
#         with z5:
#             InsuredRelationship = st.text_input("InsuredRelationship")
#         submitButton = st.form_submit_button(label = 'Submit8')

#     with st.form(key='columns_in_form9'):
#         z1, z2, z3, z4, z5 = st.columns(5)
#         with z1:
#             ReportedFraud = st.text_input("ReportedFraud")
#         with z2:
#             VehicleID = st.text_input("VehicleID")
#         with z3:
#             VehicleModel = st.text_input("VehicleModel")
#         with z4:
#             VehicleMake = st.text_input("VehicleMake")
#         with z5:
#             VehicleYOM = st.text_input("VehicleYOM")
#         submitButton = st.form_submit_button(label = 'Submit9')

#     test = pd.DataFrame([CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddress,IncidentTime,NumberOfVehicles,PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfTotalClaim,AmountOfInjuryClaim,InsuredAge,InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,InsuredHobbies,CapitalGains,CapitalLoss,Country,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,Policy_CombinedSingleLimit,Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,ReportedFraud,VehicleID,VehicleModel,VehicleMake,VehicleYOM], columns=CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddress,IncidentTime,NumberOfVehicles,\
#     PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfTotalClaim,AmountOfInjuryClaim,InsuredAge,InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,\
#     InsuredHobbies,CapitalGains,CapitalLoss,Country,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,Policy_CombinedSingleLimit,Policy_Deductible,\
#     PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,ReportedFraud,VehicleID,VehicleModel,VehicleMake,VehicleYOM'.split(','))
#     st.dataframe(test, use_container_width=True)

    
 # assigning int and removing insured zip code from int float cols to num_cols

# int_cols = list(df_train_final.select_dtypes(include = "int").columns)
# int_cols.remove("InsuredZipCode")
# int_cols.remove("InsurancePolicyNumber")


# float_cols = list(df_train_final.select_dtypes(include = "float").columns)
# num_cols = int_cols+float_cols


    result=""
    if st.button("Predict"):
        result=predict_note_authentication(CustomerID,DateOfIncident,TypeOfIncident,TypeOfCollission,\
SeverityOfIncident,AuthoritiesContacted,IncidentState,IncidentCity,IncidentAddress,IncidentTime,NumberOfVehicles,\
PropertyDamage,BodilyInjuries,Witnesses,PoliceReport,AmountOfTotalClaim,AmountOfInjuryClaim,AmountOfPropertyClaim,\
AmountOfVehicleDamage,InsuredAge, InsuredZipCode,InsuredGender,InsuredEducationLevel,InsuredOccupation,InsuredHobbies,\
CapitalGains,CapitalLoss,Country,InsurancePolicyNumber,CustomerLoyaltyPeriod,DateOfPolicyCoverage,InsurancePolicyState,\
Policy_CombinedSingleLimit,Policy_Deductible,PolicyAnnualPremium,UmbrellaLimit,InsuredRelationship,ReportedFraud,VehicleID,\
VehicleModel,VehicleMake,VehicleYOM)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()
    
    
    


