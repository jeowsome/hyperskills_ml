import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 8)


general = pd.read_csv("test/general.csv")
prenatal = pd.read_csv("test/prenatal.csv")
sports = pd.read_csv("test/sports.csv")

prenatal.columns = general.columns
sports.columns = general.columns

merged_df = pd.concat((general, prenatal, sports), ignore_index=True)
merged_df.drop(columns=["Unnamed: 0"], inplace=True)
merged_df.dropna(axis=0, how="all", inplace=True)
merged_df.replace({'gender': {'man': 'm', 'male': 'm', 'woman': 'f', 'female': 'f'}}, inplace=True)
merged_df.gender.fillna('f', inplace=True)
merged_df.fillna({'bmi': 0, 'diagnosis': 0, 'blood_test': 0, 'ecg': 0, 'ultrasound': 0, 'mri': 0,
                  'xray': 0, 'children': 0, 'months': 0}, inplace=True)
merged_df.sample(n=20, random_state=30)

# gen_stomach_count = merged_df[['hospital', 'diagnosis']].value_counts().loc['general', 'stomach']
# gen_stomach_count_max = merged_df.groupby(["hospital"]).agg({"diagnosis": "count"}).diagnosis[0]
# sp_dislocation_count = merged_df[['hospital', 'diagnosis']].value_counts().loc['sports', 'dislocation']
# sp_dislocation_count_max = merged_df.groupby(["hospital"]).agg({"diagnosis": "count"}).diagnosis[2]
# gen_age = merged_df.groupby(["hospital"]).agg({"age": "median"}).age[0]
# sp_age = merged_df.groupby(["hospital"]).agg({"age": "median"}).age[2]
# t_max = merged_df.hospital.loc[merged_df.blood_test == "t"].describe()
# print(f"The answer to the 1st question is {merged_df.describe(include='all').hospital.top}")
# print(f"The answer to the 2nd question is {gen_stomach_count / gen_stomach_count_max}")
# print(f"The answer to the 3rd question is {round(sp_dislocation_count /sp_dislocation_count_max, 3)}")
# print(f"The answer to the 4th question is {gen_age - sp_age}")
# print(f"The answer to the 5th question is {t_max.top}, {t_max.freq} blood tests")


def plot():
    merged_df.plot(y="age", kind="hist")
    plt.show()
    print("The answer to the 1st question: 15 - 35")

    merged_df['diagnosis'].value_counts().plot(kind='pie')
    plt.show()
    print('The answer to the 2nd question: pregnancy')

    sns.violinplot(x="hospital", y="height", data=merged_df)
    plt.show()
    print("The answer to the 3rd question: It's because values are too large")


plot()
