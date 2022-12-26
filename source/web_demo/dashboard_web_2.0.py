import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import base64

name_Position = ['ST', 'CM', 'CB', 'GK']
name_GePoint = ['Attacking', 'Skill', 'Movement', 'Power', 'Mentality', 'Defending', 'Goalkeeping']

attacking = ['Crossing', 'Finishing', 'ShortPassing', 'Volleys']
skill = ['Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl']
movement = ['Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance']
power = ['ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots']
mentality = ['Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure']
defending = ['StandingTackle', 'SlidingTackle']
goalkeeping = ['GKDiving', 'GKKicking', 'GKPositioning', 'GKReflexes']
name_GePoint = ['attacking', 'skill', 'movement', 'power', 'mentality', 'defending', 'goalkeeping']


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

#Đọc data
df = pd.read_csv('dataset\FIFA22.csv')
st.write("""# Analyze and visualize data to suggest building squads of players in FIFA 22 games""")

st.header('Visualization of personal information data')

col1, col2 = st.columns((10,10))

with col1:
    # Age distribution of players
    st.subheader('Age distribution of players')

    x = df['Age'].value_counts().index
    y = df['Age'].value_counts()
    plt.figure(figsize=(18,10))
    plt.bar(x, y)
    plt.xlabel('Age of the Players', fontsize = 16)
    plt.ylabel('Quantity', fontsize =16)
    plt.title('Distribution of Age of the Players', fontsize = 20)

    st.pyplot(plt)

with col2:
    # Overall Score of Players
    st.subheader('Overall Score of Players')

    x = df['Overall'].value_counts().index
    y = df['Overall'].value_counts()
    plt.figure(figsize=(18,10))
    plt.bar(x, y)
    plt.xlabel(xlabel = "Player's Overall Scores", fontsize = 16)
    plt.ylabel(ylabel = 'Number of Players', fontsize = 16)
    plt.title(label = 'Distribution of Players Overall Scores', fontsize = 20)

    st.pyplot(plt)

with col1:
    # Skill Moves and Prefered Legs of the players
    st.subheader('Skill Moves and Prefered Legs of the players')

    fig, ax = plt.subplots(figsize=(12,8))
    graph = sns.countplot(ax=ax,x=df['Skill Moves'], data=df, hue='Preferred Foot', palette = 'PuBuGn_d')
    plt.title('Skill Moves of Players segregated by Preferred Foot'  , fontsize = 20)
    plt.xlabel('Skill Moves')
    plt.ylabel('Number')
    for p in graph.patches:
        height = p.get_height()
        graph.text(p.get_x()+p.get_width()/2., height + 0.1,height ,ha="center");

    st.pyplot(plt)

with col2:
    # Top 10 countries with most number of player
    st.subheader('Top 10 countries with most number of players')

    top_countries = df['Nationality'].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(12,8))
    x = top_countries.values
    y = top_countries.index
    plt.barh(y, x, align='center')
    plt.gca().invert_yaxis()
    plt.xlabel('Number of Players')
    plt.ylabel('Name of Countries', rotation=0)
    plt.title('Top 10 Countries with most number of players')

    st.pyplot(plt)

# Distribution of Best Position of players
st.subheader('Distribution of Best Position of players')
plt.figure(figsize=(18,15))
labels = df['Best Position'].value_counts().index
size = df['Best Position'].value_counts()
plt.pie(size,labels = labels, shadow =True, autopct='%1.1f%%', colors = colors.TABLEAU_COLORS ,startangle = 40)
plt.title('Distribution of Best Position of players', fontsize = 20)
plt.legend(labels, title = 'Position',loc='upper right',fontsize = 10)
st.pyplot(plt)
st.header('Visualize metric information data')

# Using for Visualize metric information data
#==========================================================================================
#Compare objects
st.subheader('Compare objects')
st.sidebar.header('Using for Visualize metric information data')
st.sidebar.subheader('Compare between Positions')
# Sidebar - Position selection
recommend_position = name_Position
selected_position = st.sidebar.multiselect('Position', name_Position, recommend_position)

# Sidebar - Target selection
recommend_target = name_GePoint[:-1]
selected_target = st.sidebar.multiselect('Target', name_GePoint, recommend_target)

if st.button('Compare between Positions'):
    import plotly.express as px
    import plotly.graph_objects as go
    point = []
    position = []
    target = []
    df_GePoint = pd.read_csv('dataset/FiFA22_General_Position.csv')

    for i in range(df_GePoint.shape[0]):
        for j in range(df_GePoint.shape[1]):
            if (df_GePoint.GeneralPosition[i] in selected_position) & (df_GePoint.columns[j] in selected_target):
                point.append(df_GePoint.iloc[i,j])
                position.append(df_GePoint.GeneralPosition[i])
                target.append(df_GePoint.columns[j])

    dict_columns = {'target':target, 'position':position, 'point':point}
    df_new = pd.DataFrame(dict_columns)

    fig = px.line_polar(df_new, r=point, theta=target, color=position, line_close=True,
                        color_discrete_sequence=px.colors.qualitative.Light24)

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                            visible=True,
                            range=[0, 100]
                        )
                ),
        title="Mạng lưới chỉ số nhóm cầu thủ"
    )

    fig.update_traces(fill='toself')
    fig.show()

st.sidebar.subheader('Compare between players')
recommend_player = ['K. De Bruyne', 'E. Haaland']
selected_player = st.sidebar.multiselect('Target', df.Name, recommend_player)

if st.button('Compare between players'):
    import plotly.express as px
    import plotly.graph_objects as go

    fig = go.Figure()

    for i in selected_player:
        fig.add_trace(
                    go.Scatterpolar(
                                    r=df[df.Name == i][df.columns[54:61]].values[0],
                                    theta=df.columns[54:61],
                                    fill='toself',
                                    name = i,
                                    showlegend=True,
                                    mode = 'markers',
                                    marker = {'color' : 'blue'}
                                    )
                    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                            visible=True,
                            range=[0, 100]
                        )
                ),
        title="Mạng lưới chỉ số các cầu thủ"
    )
    fig.show()

st.subheader('Correlation between attributes and positions')
st.write("""#### Correlation between attributes and positions""")

attacking_p = []
skill_p = []
movement_p = []
power_p = []
mentality_p = []
defending_p = []
goalkeeping_p = []

for i in name_Position:
  attacking_p.append(np.float64(df[df['GeneralPosition'] == i][attacking].mode().mean(axis = 1).max()))
  skill_p.append(np.float64(df[df['GeneralPosition'] == i][skill].mode().mean(axis = 1).max()))
  movement_p.append(np.float64(df[df['GeneralPosition'] == i][movement].mode().mean(axis = 1).max()))
  power_p.append(np.float64(df[df['GeneralPosition'] == i][power].mode().mean(axis = 1).max()))
  mentality_p.append(np.float64(df[df['GeneralPosition'] == i][mentality].mode().mean(axis = 1).max()))
  defending_p.append(np.float64(df[df['GeneralPosition'] == i][defending].mode().mean(axis = 1).max()))
  goalkeeping_p.append(np.float64(df[df['GeneralPosition'] == i][goalkeeping].mode().mean(axis = 1).max()))

data = {'attacking': attacking_p, 'skill': skill_p, 'movement': movement_p, 
        'power': power_p, 'mentality': mentality_p, 'defending': defending_p,
        'goalkeeping': goalkeeping_p}

df_ModePos = pd.DataFrame(data)
df_ModePos.index = name_Position
df_ModePos.index.name = "GeneralPosition"

st.write(df_ModePos)

st.write("""#### Highly correlated attribute group for each positions""")

arr = []
for i in name_GePoint:
  arr.append(df_ModePos[i].sort_values(ascending=False).head(2).to_frame().index.values)

df_PosPlayer = pd.DataFrame(arr).transpose()
df_PosPlayer.columns = name_GePoint

st.write(df_PosPlayer)

# Heat map between attributes in each position
st.subheader('Heat map between attributes in each position')

df_ST = df[df['GeneralPosition'] == 'ST']
df_CM = df[df['GeneralPosition'] == 'CM']
df_CB = df[df['GeneralPosition'] == 'CB']
df_GK = df[df['GeneralPosition'] == 'GK']

heatmap_ST = df_ST[name_GePoint].corr()
heatmap_CM = df_CM[name_GePoint].corr()
heatmap_CB = df_CB[name_GePoint].corr()
heatmap_GK = df_GK[name_GePoint].corr()

cmap = sns.diverging_palette(0, 230, 90, 60, as_cmap=True)
col21, col22 = st.columns((5,5))

with col21:
    st.write("""#### Position ST""")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(heatmap_ST, annot=True, fmt=".2f", cmap = cmap, vmin=-1, vmax=1)
    st.pyplot(fig)

with col22:
    st.write("""#### Position CM""")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(heatmap_CM, annot=True, fmt=".2f", cmap = cmap, vmin=-1, vmax=1)
    st.pyplot(fig)

with col21:
    st.write("""#### Position CB""")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(heatmap_CB, annot=True, fmt=".2f", cmap = cmap, vmin=-1, vmax=1)
    st.pyplot(fig)

with col22:
    st.write("""#### Position GK""")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(heatmap_GK, annot=True, fmt=".2f", cmap = cmap, vmin=-1, vmax=1)
    st.pyplot(fig)

# Correlation between players
st.subheader('Correlation between positions')

df_p2p = df_ModePos.transpose()
heatmap_p2p = df_p2p[name_Position].corr()

fig, ax = plt.subplots(figsize=(7, 5))
ax = sns.heatmap(heatmap_p2p, annot=True, fmt=".2f", cmap = cmap, vmin=-1, vmax=1)
st.pyplot(fig)

# Correlation between detailed attributes of each position
st.subheader('Correlation between detailed attributes of each position')

df_ST_train = df_ST[defending + power + movement + skill + attacking]
df_CM_train = df_CM[defending + mentality + movement + skill + attacking]
df_CB_train = df_CB[defending + mentality]
df_GK_train = df_GK[goalkeeping + power]

st.write("""#### Position ST""")
fig, ax = plt.subplots(figsize=(15, 10))
ax = sns.heatmap(df_ST_train.corr(), annot=True, fmt=".2f", cmap = cmap, vmin=-1, vmax=1)
st.pyplot(fig)

st.write("""#### Position CM""")
fig, ax = plt.subplots(figsize=(15, 10))
ax = sns.heatmap(df_CM_train.corr(), annot=True, fmt=".2f", cmap = cmap, vmin=-1, vmax=1)
st.pyplot(fig)

col13, col23 = st.columns((5,5))

with col13:
    st.write("""#### Position CB""")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(df_CB_train.corr(), annot=True, fmt=".2f", cmap = cmap, vmin=-1, vmax=1)
    st.pyplot(fig)

with col23:
    st.write("""#### Position GK""")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(df_GK_train.corr(), annot=True, fmt=".2f", cmap = cmap, vmin=-1, vmax=1)
    st.pyplot(fig)

with col13:
    # Overall comparison of positions
    st.write("""#### Overall comparison of positions""")

    fig, ax = plt.subplots(figsize=(10, 7))
    textprops = {"fontsize": 20}

    df_ST.Overall.value_counts().sort_index().plot(kind = 'line', color = 'r')
    df_CM.Overall.value_counts().sort_index().plot(kind = 'line', color = 'b')
    df_CB.Overall.value_counts().sort_index().plot(kind = 'line', color = 'g')
    df_GK.Overall.value_counts().sort_index().plot(kind = 'line', color = 'y')

    plt.legend(title = "Country")
    plt.title('Overall comparison of positions')
    plt.ylabel('Value')
    plt.xlabel('Point')

    st.pyplot(fig)

with col23:
    # Distribution of positions
    st.write("""#### Distribution of positions""")

    plt.figure(figsize=(10,10))
    labels = df['GeneralPosition'].value_counts().index
    size = df['GeneralPosition'].value_counts()
    plt.pie(size,labels = labels, shadow =True, autopct='%1.1f%%', colors = colors.TABLEAU_COLORS ,startangle = 40)
    plt.title('Distribution of positions', fontsize = 20)
    plt.legend(labels, title = 'Position',loc='upper right',fontsize = 10)
    st.pyplot(plt)



