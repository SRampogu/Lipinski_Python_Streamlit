import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski
import streamlit as st
import pandas as pd

#Lipinski for Single Molecule
st.header('Lipinski Prediction-SMILES input')

smiles=st.text_input(("Enter the valid SMILES"))

df=Chem.MolFromSmiles(smiles)
#df=Chem.MolFromSmiles(smiles)
b=Descriptors.ExactMolWt(df)
c=Descriptors.NumHAcceptors(df)
d=Descriptors.NumHDonors(df)
e=Descriptors.MolLogP(df)
#st.write(b,c,d,e)
df3=pd.Series({"MW":b, "nHA":c, "nHD":d,"LogP":e})
df4=pd.Series.to_frame(df3).T #(.T= transpose)
df5=pd.Series.to_frame(df3)

st.write('WITH TRANSPOSE')
st.write(df4)

st.write('WITHOUT TRANSPOSE')
st.write(df5)
      

    




