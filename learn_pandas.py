import pandas as pd;

# marks = pd.Series([23, 34, 64], index=[1, 2, 3]);

# print(marks);

data = {
    "name": ["john", "Rohit", "Riya"],
    "age": [23, 20, 23],
    "marks": [23, 34, 64]
};

datframe = pd.DataFrame(data);
# print(datframe);

# print(datframe.head(1));
# print(datframe.tail(1));

# print(datframe.sample(2));

print(datframe.size);
print(datframe.shape);