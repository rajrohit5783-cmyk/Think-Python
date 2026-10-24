import pandas as pd;

# marks = pd.Series([23, 34, 64], index=[1, 2, 3]);

# # print(marks);

# data = {
#     "name": ["john", "Rohit", "Riya"],
#     "age": [23, 34, 23],
#     "marks": [23, 34, 64]
# };

# datframe = pd.DataFrame(data);
# print(datframe);

# # print(datframe.head(1));
# # print(datframe.tail(1));

# # print(datframe.sample(2));

# # print(datframe.size);
# # print(datframe.shape);
# # print(marks.size);
# # print(marks.shape);

# # print(datframe.describe());
# # print(datframe.info());
# # print(marks.info());
# # print(marks.describe());

# # print(datframe.columns);
# # print(datframe[["name","age"]]);

# data1 = pd.read_csv("./student_data_150.csv");
# data2 = pd.read_json("./student_data_150.json");
# data3 = pd.read_excel("./student_data_150.xlsx");
# # print(data1);
# # print(data2);


# # print(data1.loc[1,"name"]);
# # print(data1.iloc[1,1])

# # print(data1[5:10]);
# # print(data1.isnull());
# # print(data1.isnull().sum());
# # print(data1.dtypes);
# # print(data1['city'].unique());
# # print(data1.dropna());
# # data1['age'] =  data1['age'].fillna(data1['age'].mode());
# # print(data1);
# # print(data1.duplicated());
# # print(data1.duplicated().sum());
# # print(data1.drop_duplicates(inplace=True));
# # print(data1.duplicated().sum());
# # print(data1.dtypes);
# # print(data1["age"]< 13);
# data1["name"] = data1['name'].str.lower();
# print(data1);

# data = pd.DataFrame({
#     "Grades": ['A', 'B', 'C', 'D', 'E','F']
# });

# data2 = data["Grades"].map({"A": "Excellent", "B": "Very Good", "C": "Good", "D": "Bad", "E": "Very Bad",'F': "Fail"});

# def Grade(n):
#     if n >= 90 :
#         return "Excellent"
#     elif n >=  80 and n < 90:
#         return "Very Good"
#     elif n >= 70 and n < 80:
#         return "Good"
#     elif n >= 60 and n < 70:
#         return "Bad" 
#     else: return "fail"

# qwe = lambda abc: abc + 123456;
# data = pd.DataFrame({
#     "Marks": [76,45, 33, 74, 96,33]
# });
# data2 = data["Marks"].map(lambda abc: abc + 123456)
# data = pd.DataFrame({
#     "Marks": [10,21, 23, 13, 12,25],
#     "age": [23, 34, 23,45,2,24],
# });
# rangeAge = [0, 20 , 30, 50];
# labelAge = ["Minor", "Child", "Adult"]
# data["Grade"] = pd.cut(data["Marks"], bins=rangeAge, labels=labelAge)

# range = [0,10, 20,30];
# label = ["C", "B", "A"];
# data["Grade"] = pd.cut(data["Marks"], bins=range, labels=label)
# print(data);




# data = pd.DataFrame({
#     "Marks": [10, 21, 23, 13, 12, 25],
#     "age": [23, 34, 23, 45, 2, 24]
# })

# rangeAge = [0, 20, 30, 50]
# labelAge = ["Minor", "Child", "Adult"]

# data["Grade"] = pd.cut(
#     data["age"],
#     bins=rangeAge,
#     labels=labelAge
# )

# print(data)

outlier = 30;
 
data = pd.DataFrame({
    "Marks": [10, 21, 23, 13, 12, 25]
})

# print(data["Marks"] > 20);

# data2 = data[data["Marks"] > 20]
# print(data2)

# data.rename(columns={"Marks": "Score"}, inplace=True
# data.replace({10:20}, inplace=True)
# print(data)

print(data["Marks"].sample(n=0));