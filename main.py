import pandas as pd
from pymongo import MongoClient

df = pd.read_csv("Annual_change_forest_area.csv")

client = MongoClient("mongodb://localhost:27017/")
db = client["forestChangingArea"]

data = df.to_dict("records")

collection = db["data"]
collection.insert_many(data)

print(collection.count_documents({}))






