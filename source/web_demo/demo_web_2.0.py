import streamlit as st
import pandas as pd
import numpy as np
import base64

# import local file
from predict_function import recommend_ST, recommend_CM, recommend_CB, recommend_GK

# Khởi tạo các biến
name_Position = ['ST', 'CM', 'CB', 'GK']
name_model = ['kmeans','hierarchical']
feature_ST = ['StandingTackle (10 , 72)', 'ShotPower(38, 94)', 'Jumping(33, 95)', 
            'Stamina(30, 92)', 'Strength(34, 97)', 'SprintSpeed (32, 97)', 'Agility(30, 96)',
            'Reactions(45, 81)', 'Balance(32, 95)', 'Dribbling(40, 86)', 'Curve(21, 94)', 
            'FKAccuracy(21, 94)', 'LongPassing(19, 91)', 'Crossing(20, 88)', 'Volleys(30, 90)']
feature_CM = ['SlidingTackle (10, 87)', 'Aggression (20, 95)', 'Penalties (20, 92)',
            'SprintSpeed (32, 96)', 'Agility (30, 95)', 'Reactions (45, 81)', 'Balance (32, 96)',
            'Dribbling (35, 86)', 'FKAccuracy (20, 92)', 'LongPassing (26, 93)', 'Crossing (22, 94)',
            'Finishing (21, 88)', 'Volleys (17, 90)']
feature_CB = ['StandingTackle (43, 92)', 'Aggression (28, 95)', 'Positioning (12, 86)', 
            'Vision (25, 87)', 'Penalties (13, 92)', 'Composure (35, 84)']
feature_GK = ['GKReflexes (16, 90)', 'ShotPower (29, 70)', 'Jumping (22, 84)',
            'Stamina (13, 45)', 'Strength (24, 85)', 'LongShots (4, 45)']

# Hàm thay đổi background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')

st.write("""# Recommend building squads of players in FIFA 22 games""")

postition_pre = st.selectbox('Position', name_Position)
model_pre = st.selectbox('Model', name_model)

if postition_pre == 'ST':  
    arr = np.zeros(len(feature_ST))
    df = pd.DataFrame(feature_ST, arr).transpose()
    df.columns = feature_ST

    col_1, col_2, col_3 = st.columns((5,5,5))
    with col_1: n1= st.text_area("'StandingTackle (10, 72)': ")
    with col_2: n2 = st.text_area("'ShotPower(38, 94)': ")
    with col_3: n3 = st.text_area("'Jumping(33, 95)': ")
    with col_1: n4 = st.text_area("'Stamina(30, 92)': ")
    with col_2: n5= st.text_area("'Strength(34, 97)': ")
    with col_3: n6= st.text_area("'Agility(30, 96)': ")
    with col_1: n7= st.text_area("'SprintSpeed (32, 97)': ")
    with col_2: n8= st.text_area("'Reactions(45, 81)': ")
    with col_3: n9= st.text_area("'Balance(32, 95)': ")
    with col_1: n10 = st.text_area("'Dribbling(40, 86)': ")
    with col_2: n11 = st.text_area("'Curve(21, 94)': ")
    with col_3: n12 = st.text_area("'FKAccuracy(21, 94)': ")
    with col_1: n13= st.text_area("'LongPassing(19, 91)': ")
    with col_2: n14= st.text_area("'Crossing(20, 88)': ")
    with col_3: n15= st.text_area("'Volleys(30, 90)': ")

    if n1 == '': n1 = 72
    if n2 == '': n2 = 94
    if n3 == '': n3 = 95
    if n4 == '': n4 = 92
    if n5 == '': n5 = 97
    if n6 == '': n6 = 96
    if n7 == '': n7 = 97
    if n8 == '': n8 = 81
    if n9 == '': n9 = 95
    if n10 == '': n10 = 86
    if n11 == '': n11 = 94
    if n12 == '': n12 = 94
    if n13 == '': n13 = 91
    if n14 == '': n14 = 88
    if n15 == '': n15 = 90

    if st.button("Tiến hành đề xuất"):
        result = recommend_ST(model_pre, StandingTackle = n1,
                                        ShotPower = n2,
                                        Jumping = n3,
                                        Stamina = n4,
                                        Strength = n5,
                                        Agility = n6,
                                        SprintSpeed =n7 ,
                                        Reactions = n8,
                                        Balance = n9,
                                        Dribbling = n10,
                                        Curve = n11,
                                        FKAccuracy = n12,
                                        LongPassing = n13,
                                        Crossing = n14,
                                        Volleys = n15)
        st.write(result)

if postition_pre == 'CM':
    arr = np.zeros(len(feature_CM))
    df = pd.DataFrame(feature_CM, arr).transpose()
    df.columns = feature_CM 
    
    col_1, col_2, col_3 = st.columns((5,5,5))
    with col_1: n1 = st.text_area("'StandingTackle (10, 72)': ")
    with col_2: n2 = st.text_area("'Aggression (20, 95)': ")
    with col_3: n3 = st.text_area("'Penalties (20, 92)': ")
    with col_1: n4= st.text_area("'SprintSpeed (32, 96)': ")
    with col_2: n5= st.text_area("'Agility (30, 95)': ")
    with col_3: n6 = st.text_area("'Reactions (45, 81)': ")
    with col_1: n7= st.text_area("'Balance (32, 96)': ")
    with col_2: n8= st.text_area("'Dribbling (35, 86)': ")
    with col_3: n9 = st.text_area("'FKAccuracy (20, 92)': ")
    with col_1: n10 = st.text_area("'LongPassing (26, 93)': ")
    with col_2: n11 = st.text_area("'Crossing (22, 94)': ")
    with col_3: n12 = st.text_area("'Finishing (21, 88)': ")
    n13 = st.text_area("'Volleys (17, 90)': ")

    if n1 == '': n1 = 72
    if n2 == '': n2 = 95
    if n3 == '': n3 = 92
    if n4 == '': n4 = 96
    if n5 == '': n5 = 95
    if n6 == '': n6 = 81
    if n7 == '': n7 = 96
    if n8 == '': n8 = 86
    if n9 == '': n9 = 92
    if n10 == '': n10 = 93
    if n11 == '': n11 = 94
    if n12 == '': n12 = 88
    if n13 == '': n13 = 90
    
    if st.button("Tiến hành đề xuất"):
        result = recommend_CM(model_pre, SlidingTackle = n1,
                                        Aggression = n2,
                                        Penalties = n3,
                                        SprintSpeed = n4 ,
                                        Agility = n5,
                                        Reactions = n6,
                                        Balance =n7,
                                        Dribbling =n8 ,
                                        FKAccuracy =n9 ,
                                        LongPassing =n10 ,
                                        Crossing = n11,
                                        Finishing = n12,
                                        Volleys = n13)
        st.write(result)

if postition_pre == 'CB':
    col_1, col_2, col_3 = st.columns((5,5,5))
    with col_1: n1 = st.text_area("'StandingTackle (43, 92)': ")
    with col_2: n2= st.text_area("'Aggression (28, 95)': ")
    with col_3: n3= st.text_area("'Positioning (12, 86)': ")
    with col_1: n4= st.text_area("'Vision (25, 87)': ")
    with col_2: n5= st.text_area("'Penalties (13, 92)': ")
    with col_3: n6= st.text_area("'Composure (35, 84)': ")

    if n1 == '': n1 = 92
    if n2 == '': n2 = 95
    if n3 == '': n3 = 86
    if n4 == '': n4 = 87
    if n5 == '': n5 = 92
    if n6 == '': n6 = 84
    
    if st.button("Tiến hành đề xuất"):
        result = recommend_CB(model_pre, StandingTackle = n1,
                                        Aggression = n2,
                                        Positioning = n3,
                                        Vision = n4,
                                        Penalties = n5,
                                        Composure = n6,
                                )
        st.write(result)

if postition_pre == 'GK':
    col_1, col_2, col_3 = st.columns((5,5,5))
    with col_1: n1 = st.text_area("'GKReflexes (16, 90)':")
    with col_2: n2 = st.text_area("'ShotPower (29, 70)': ")
    with col_3: n3= st.text_area("'Jumping (22, 84)': ")
    with col_1: n4= st.text_area("'Stamina (13, 45)': ")
    with col_2: n5 = st.text_area("'Strength (24, 85)': ")
    with col_3: n6 = st.text_area("'LongShots (4, 45)': ")

    if n1 == '': n1 = 90
    if n2 == '': n2 = 70
    if n3 == '': n3 = 84
    if n4 == '': n4 = 45
    if n5 == '': n5 = 85
    if n6 == '': n6 = 45
    
    if st.button("Tiến hành đề xuất"):
        result = recommend_GK(model_pre, GKReflexes = n1,
                                         ShotPower = n2,
                                         Jumping = n3,
                                         Stamina = n4,
                                         Strength = n5,
                                         LongShots = n6)               
        st.write(result)

