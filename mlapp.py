#MLAPP 1 !!!!!!!!!!!!!!!!

import streamlit as st
import pandas as pd
import numpy as np


#______________________________________________________________________
def info_shape(data):
  """
  Parameters  :   Dataframe
  Return      :   info(), shape()
  """
  print(f"shape:{data.shape}")
  return [data.info()]

#______________________________________________________________________
def stats(data):
  """
  Parameters  :   Dataframe
  Return      :   head(), tail(), dtype,  describe()
  in a single dataframe for convinient and compact representation
  """
  col_dtype=pd.DataFrame(data.dtypes,columns=['dtype'])
  col_desc=data.describe()
  return pd.concat([data.head(),data.tail(),col_dtype.T,col_desc])
  
#_____________________________________________________________________
def null_unique(data):
  """
  Parameters  :   Dataframe
  Return      :   nunique(),  isna()
  in a single dataframe for convinient and compact representation
  """
  uni=pd.DataFrame(data.nunique(),columns=['unique values'])
  uni['unique values %'] = (uni['unique values']/data.shape[0])*100
  nul=pd.DataFrame(data.isna().sum(),columns=['null values'])
  nul['null values %'] = (nul['null values']/data.shape[0])*100
  return pd.concat([uni,nul],axis=1)

#____________________________________________________________________
def dmy_hms(data,columns):
  """
  Parameters: datetime [ns] column
  Return    : day month year    hour minute second
  and appends these columns to the given dataframe
  """
  for column in columns:
    data[column+'_day'] = data[column].dt.date.apply(lambda x: x.strftime("%a"))
    data[column+'_month'] = data[column].dt.date.apply(lambda x: x.strftime("%b"))
    data[column+'_year'] = data[column].dt.year
    data[column+'_hour'] = data[column].dt.hour
    data[column+'_minute'] = data[column].dt.minute
    data[column+'_second'] = data[column].dt.second
    for i in [column+'_day',column+'_month',column+'_year',column+'_hour',column+'_minute',column+'_second']:
      if(data[i].nunique()==1):
        data.drop(i,inplace=True,axis=1)
    data.drop(column,axis=1,inplace=True)

#__________________________________________________________________
def type_cast(data,cat=None,num=None,da_ti=None):
  """
  Parameters: Dataframe, list of column name in dataframe to be converted to category , list of column name in dataframe to be converted to int64, list of column name in dataframe to be converted to datetime64[ns]
  Return    : Modified dataframe of given datatypes of corresponding columns list
  """
  for i in cat:
    data[i] = data[i].astype('category')
  for j in num:
    data[j] = pd.to_numeric(data[j])
  for k in da_ti:
    data[k] = pd.to_datetime(data[k])






st.set_page_config(page_title="MLAPP",page_icon="🧑‍💻", layout="centered")
st.text("ML APP1")
train = pd.DataFrame({'col1':list(range(10)),
                      'col2':list(range(10)),
                      'col3':list(range(10)),
                      'col5':[chr(x) for x in range(65,75)],
                      'col6':[chr(x) for x in range(97,97+10)]})
st.dataframe(info_shape(train), use_container_width=True)
st.dataframe(stats(train), use_container_width=True)
st.dataframe(null_unique(train), use_container_width=True)

a = train.columns
num_opt = st.multiselect('What are your numerical columns',a)
cat_opt = st.multiselect('What are your categorical columns',[x for x in a if x not in num_opt])
date_opt = st.multiselect('What are your datetime columns',[x for x in a if x not in num_opt+cat_opt])
st.write('Numerical columns:',num_opt,'Categorical columns:',cat_opt,'date columns:',date_opt)
if submit:
    st.success('The output is this x')
