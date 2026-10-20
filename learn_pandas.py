import pandas as pd;

marks = pd.Series([23, 34, 64], index=[1, 2, 3]);

# print(marks);

data = {
    "name": ["john", "Rohit", "Riya"],
    "age": [23, 34, 23],
    "marks": [23, 34, 64]
};

datframe = pd.DataFrame(data);
# print(datframe);

# print(datframe.head(1));
# print(datframe.tail(1));

# print(datframe.sample(2));

# print(datframe.size);
# print(datframe.shape);
# print(marks.size);
# print(marks.shape);

# print(datframe.describe());
# print(datframe.info());
# print(marks.info());
# print(marks.describe());

# print(datframe.columns);
# print(datframe[["name","age"]]);

data1 = pd.read_csv("./student_data_150.csv");
data2 = pd.read_json("./student_data_150.json");
data3 = pd.read_excel("./student_data_150.xlsx");
# print(data1);
# print(data2);


# print(data1.loc[1,"name"]);
# print(data1.iloc[1,1])

# print(data1[5:10]);
# print(data1.isnull());
# print(data1.isnull().sum());
# print(data1.dtypes);
# print(data1['city'].unique());
# print(data1.dropna());
# data1['age'] =  data1['age'].fillna(data1['age'].mode());
# print(data1);
# print(data1.duplicated());
# print(data1.duplicated().sum());
# print(data1.drop_duplicates(inplace=True));
# print(data1.duplicated().sum());
# print(data1.dtypes);
# print(data1["age"]< 13);
data1["name"] = data1['name'].str.lower();
print(data1);
