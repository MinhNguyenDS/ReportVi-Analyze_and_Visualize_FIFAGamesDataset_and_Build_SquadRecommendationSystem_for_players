import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
import joblib

warnings.filterwarnings("ignore")
sns.set_style()
plt.style.use('seaborn')

df_ST = pd.read_csv('dataset_predict/df_ST.csv')
df_CM = pd.read_csv('dataset_predict/df_CM.csv')
df_CB = pd.read_csv('dataset_predict/df_CB.csv')
df_GK = pd.read_csv('dataset_predict/df_GK.csv')

# Predict function
# model_name, kargs thuộc tính ứng với từng nhóm vị trí
def recommend_ST (model_name, **kargs):
  # load model
  if model_name == 'kmeans':
    model = joblib.load('model/model_ST_K-means-4.sav')
  elif model_name == 'hierarchical': 
    model = joblib.load('model/model_ST_Hierarchical-5.sav')
    model_svm = joblib.load('model/model_SVM_ST.sav')

  # Khởi tạo (Nếu không có tham số thì recommend cầu thủ xịn nhất)
  StandingTackle = 72.0
  ShotPower = 94.0
  Jumping = 95.0
  Stamina = 92.0
  Strength = 97.0
  SprintSpeed = 97.0
  Agility = 96.0
  Reactions = 81.0
  Balance = 95.0 
  Dribbling = 86.0
  Curve = 94.0
  FKAccuracy = 94.0
  LongPassing = 91.0
  Crossing = 88.0
  Volleys = 90.0

  # Lấy giá trị 
  for id in kargs:
    if id == 'StandingTackle': 
        StandingTackle = kargs.get('StandingTackle')
    if id == 'ShotPower': 
        ShotPower = kargs.get('ShotPower')
    if id == 'Jumping': 
        Jumping = kargs.get('Jumping')
    if id == 'Stamina': 
        Stamina = kargs.get('Stamina')
    if id == 'Strength': 
        Strength = kargs.get('Strength')
    if id == 'SprintSpeed': 
        SprintSpeed = kargs.get('SprintSpeed')
    if id == 'Agility': 
        Agility = kargs.get('Agility')
    if id == 'Reactions': 
        Reactions = kargs.get('Reactions')
    if id == 'Balance': 
        Balance = kargs.get('Balance')
    if id == 'Dribbling': 
        Dribbling = kargs.get('Dribbling')
    if id == 'Curve': 
        Curve = kargs.get('Curve')
    if id == 'FKAccuracy': 
        FKAccuracy = kargs.get('FKAccuracy')
    if id == 'LongPassing': 
        LongPassing = kargs.get('LongPassing')
    if id == 'Crossing': 
        Crossing = kargs.get('Crossing')
    if id == 'Volleys': 
        Volleys = kargs.get('Volleys')

  # Chuyển các giá trị về dạng array phù hợp với input đầu vào
  array_value = np.array([[ StandingTackle, ShotPower, Jumping, Stamina, Strength, 
                            SprintSpeed, Agility, Reactions, Balance, Dribbling, 
                            Curve, FKAccuracy, LongPassing, Crossing, Volleys]])
  if model_name == 'kmeans': 
    pred = model.predict(array_value)
    return df_ST[df_ST['cluster_KMeans']==pred[0]].sample(10)
  elif model_name == 'hierarchical': 
    pred = model_svm.predict(array_value)
    return df_ST[df_ST['cluster_Hierarchical']==pred[0]].sample(10) 

def recommend_CM (model_name, **kargs):
  # load model
  if model_name == 'kmeans':
    model = joblib.load('model/model_CM_K-means-4.sav')
  elif model_name == 'hierarchical': 
    model = joblib.load('model/model_CM_Hierarchical-6.sav')
    model_svm = joblib.load('model/model_SVM_CM.sav')

  # Khởi tạo (Nếu không có tham số thì recommend cầu thủ xịn nhất)
  SlidingTackle = 87.0
  Aggression = 95.0
  Penalties = 92.0
  SprintSpeed = 96.0
  Agility = 95.0
  Reactions = 81.0
  Balance = 96.0
  Dribbling = 86.0
  FKAccuracy = 92.0 
  LongPassing = 93.0
  Crossing = 94.0
  Finishing = 88.0
  Volleys = 90.0

  # Lấy giá trị 
  for id in kargs:
    if id == 'SlidingTackle': 
        SlidingTackle = kargs.get('SlidingTackle')
    if id == 'Aggression': 
        Aggression = kargs.get('Aggression')
    if id == 'Penalties': 
        Penalties = kargs.get('Penalties')
    if id == 'SprintSpeed': 
        SprintSpeed = kargs.get('SprintSpeed')
    if id == 'Agility': 
        Agility = kargs.get('Agility')
    if id == 'Reactions': 
        Reactions = kargs.get('Reactions')
    if id == 'Balance': 
        Balance = kargs.get('Balance')
    if id == 'Dribbling': 
        Dribbling = kargs.get('Dribbling')
    if id == 'FKAccuracy': 
        FKAccuracy = kargs.get('FKAccuracy')
    if id == 'LongPassing': 
        LongPassing = kargs.get('LongPassing')
    if id == 'Crossing': 
        Crossing = kargs.get('Crossing')
    if id == 'Finishing': 
        Finishing = kargs.get('Finishing')
    if id == 'Volleys': 
        Volleys = kargs.get('Volleys')

  # Chuyển các giá trị về dạng array phù hợp với input đầu vào
  array_value = np.array([[	SlidingTackle, Aggression, Penalties, SprintSpeed, Agility, 
                            Reactions, Balance, Dribbling, FKAccuracy, LongPassing, 
                            Crossing, Finishing ,Volleys]])
  
  if model_name == 'kmeans': 
    pred = model.predict(array_value)
    return df_CM[df_CM['cluster_KMeans']==pred[0]].sample(10)
  elif model_name == 'hierarchical': 
    pred = model_svm.predict(array_value)
    return df_CM[df_CM['cluster_Hierarchical']==pred[0]].sample(10) 

def recommend_CB (model_name, **kargs):
  # load model
  if model_name == 'kmeans':
    model = joblib.load('model/model_CB_K-means-3.sav')
  elif model_name == 'hierarchical': 
    model = joblib.load('model/model_CB_Hierarchical-4.sav')
    model_svm = joblib.load('model/model_SVM_CB.sav')

  # Khởi tạo (Nếu không có tham số thì recommend cầu thủ xịn nhất)
  StandingTackle = 92.0
  Aggression = 95.0
  Positioning = 86.0
  Vision = 87.0
  Penalties = 92.0
  Composure = 84.0

  # Lấy giá trị 
  for id in kargs:
    if id == 'StandingTackle': 
        StandingTackle = kargs.get('StandingTackle')
    if id == 'Aggression': 
        Aggression = kargs.get('Aggression')
    if id == 'Positioning': 
        Positioning = kargs.get('Positioning')
    if id == 'Vision': 
        Vision = kargs.get('Vision')
    if id == 'Penalties': 
        Penalties = kargs.get('Penalties')
    if id == 'Composure': 
        Composure = kargs.get('Composure')

  # Chuyển các giá trị về dạng array phù hợp với input đầu vào
  array_value = np.array([[StandingTackle,	Aggression,	Positioning,	Vision,	Penalties, Composure]])
  
  if model_name == 'kmeans': 
    pred = model.predict(array_value)
    return df_CB[df_CB['cluster_KMeans']==pred[0]].sample(10)
  elif model_name == 'hierarchical': 
    pred = model_svm.predict(array_value)
    return df_CB[df_CB['cluster_Hierarchical']==pred[0]].sample(10) 

def recommend_GK (model_name, **kargs):
  # load model
  if model_name == 'kmeans':
    model = joblib.load('model/model_GK_K-means-3.sav')
  elif model_name == 'hierarchical': 
    model = joblib.load('model/model_GK_Hierarchical-2.sav')
    model_svm = joblib.load('model/model_SVM_GK.sav')

  # Khởi tạo (Nếu không có tham số thì recommend cầu thủ xịn nhất)
  GKReflexes = 90.0
  ShotPower = 70.0
  Jumping = 84.0
  Stamina = 45.0
  Strength = 85.0
  LongShots = 45.0

  # Lấy giá trị 
  for id in kargs:
    if id == 'GKReflexes': 
        GKReflexes = kargs.get('GKReflexes')
    if id == 'ShotPower': 
        ShotPower = kargs.get('ShotPower')
    if id == 'Jumping': 
        Jumping = kargs.get('Jumping')
    if id == 'Stamina': 
        Stamina = kargs.get('Stamina')
    if id == 'Strength': 
        Strength = kargs.get('Strength')
    if id == 'LongShots': 
        LongShots = kargs.get('LongShots')

  # Chuyển các giá trị về dạng array phù hợp với input đầu vào
  array_value = np.array([[GKReflexes,	ShotPower,	Jumping,	Stamina,	Strength,	LongShots]])
  
  if model_name == 'kmeans': 
    pred = model.predict(array_value)
    return df_GK[df_GK['cluster_KMeans']==pred[0]].sample(10)
  elif model_name == 'hierarchical': 
    pred = model_svm.predict(array_value)
    return df_GK[df_GK['cluster_Hierarchical']==pred[0]].sample(10) 

if __name__ == "__main__":
    recommend_ST('kmeans')
    