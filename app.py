import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot  as plt 

st.set_page_config(page_title="Bike rentals Dashboard", layout="wide")

st.title("Bike Rental Data Analysis Dashboard")
st.markdown("""This interactive dashboard summarizes key insights from the bike rental dataset,
including temporal patterns, seasonal trends, and user behavior""")

@st.cache_data
def  load_data():
    df = pd.read_csv('./notebooks/updated_data_frame.csv')
    return df

df = load_data()

st.success(f"Dataset loaded successfully with {df.shape[0]} rows")

st.sidebar.header("Filters")

year_selector = st.sidebar.selectbox(
    "Select Year",
    options=['ALL', 2011, 2012],
    index=2
)

day_type_selector = st.sidebar.radio(
    "Day Type",
    options=["All", "Working Day", "Non-working Day"], 
    index=0
)

season_option = st.sidebar.multiselect(
    "Select Season(s)",
    options=df['season'].unique(),
    default=df['season'].unique()

)

filtered_df = df.copy()

if year_selector != 'All':
    filtered_df = filtered_df[filtered_df['year'] == year_selector]

if day_type_selector == "Working Day":
    filtered_df = filtered_df[filtered_df['workingday'] == 1]
elif day_type_selector == "Non-working Day":
    filtered_df = filtered_df[filtered_df['workingday'] == 0]

filtered_df = filtered_df[filtered_df['season'].isin(season_option)]

st.subheader("Mean Hourly Rentals vs Hour of the Day")

hourly_mean = (
    filtered_df.groupby('hour of the day')['count'].mean().reset_index()
)

fig,ax = plt.subplots()
sns.lineplot(data=hourly_mean, x='hour of the day', y = 'count', marker='o', ax=ax)
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Mean Rentals")
ax.set_xticks(range(0,24))

st.pyplot(fig)


st.subheader("mean Hourly rentals by Day of the Week")

hourly_day_mean = (
    filtered_df
    .groupby(['day of the week', 'hour of the day'])['count']
    .mean()
    .reset_index()
)

fig = sns.relplot(
    data=hourly_day_mean,
    x='hour of the day',
    y='count',
    col='day of the week',
    col_wrap=4,
    kind='line',
    height=3,
    aspect=1.2
)

fig.set_axis_labels("Hour of the Day", "Mean Hourly Rentals")
fig.set_titles("{col_name}")
fig.set(xticks=range(0, 24))
st.pyplot(fig.figure)


st.subheader("Mean Hourly Rentals by Season")

hourly_season_mean = (
    filtered_df
    .groupby(['season', 'hour of the day'])['count']
    .mean()
    .reset_index()
)

season_fig = sns.relplot(
    data=hourly_season_mean,
    x='hour of the day',
    y='count',
    col='season',
    kind='line',
    marker='o',
    col_wrap=2,
    height=4,
    aspect=1.3
)

season_fig.set_axis_labels("Hour of the Day", "Mean Hourly Rentals")
season_fig.set_titles("Season: {col_name}")
season_fig.set(xticks=range(0, 24))

st.pyplot(season_fig.figure)


st.subheader("Mean Rentals by Period of the Day (95% CI)")

fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    data=filtered_df,
    x='day_period',
    y='count',
    estimator='mean',
    errorbar=('ci', 95),
    ax=ax
)

ax.set_xlabel("Period of the Day")
ax.set_ylabel("Mean Hourly Rentals")
ax.set_title("Mean Hourly Bike Rentals by Day Period")

st.pyplot(fig)



st.subheader("Correlation Heatmap")

numeric_df = filtered_df.select_dtypes(include=['int64', 'float64'])
corr_matrix = numeric_df.corr()

fig, ax = plt.subplots(figsize=(10, 6))

sns.heatmap(
    corr_matrix,
    cmap="coolwarm",
    linewidths=0.5,
    ax=ax
)

ax.set_title("Correlation Heatmap of Numerical Variables")

st.pyplot(fig)





