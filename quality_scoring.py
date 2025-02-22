import pandas as pd


df = pd.read_csv("titanic.csv")
print(df.head())

# วิธีการเรียกดูค่าใน Column
# df["Survived"]
# df.Survived

df.info()

fare_not_null = df.Fare.notnull()
dq_fare= fare_not_null.sum() / len(df)
print(f"Data Quality of Fare: {dq_fare}")

ticket_not_null = df.Ticket.notnull()
dq_ticket= ticket_not_null.sum() / len(df)
print(f"Data Quality of Ticket: {dq_ticket}")

parch_not_null = df.Parch.notnull()
dq_parch= parch_not_null.sum() / len(df)
print(f"Data Quality of Parch: {dq_parch}")

sibsp_not_null = df.SibSp.notnull()
dq_sibsp= sibsp_not_null.sum() / len(df)
print(f"Data Quality of SibSp: {dq_sibsp}")

sex_not_null = df.Sex.notnull()
dq_sex= sex_not_null.sum() / len(df)
print(f"Data Quality of Sex: {dq_sex}")

name_not_null = df.Name.notnull()
dq_name= name_not_null.sum() / len(df)
print(f"Data Quality of Name: {dq_name}")

pclass_not_null = df.Pclass.notnull()
dq_pclass= pclass_not_null.sum() / len(df)
print(f"Data Quality of Pclass: {dq_pclass}")

survived_not_null = df.Survived.notnull()
dq_survived= survived_not_null.sum() / len(df)
print(f"Data Quality of Survived: {dq_survived}")

passenger_id_not_null = df.PassengerId.notnull()
dq_passenger_id= passenger_id_not_null.sum() / len(df)
print(f"Data Quality of PassengerId: {dq_passenger_id}")

age_not_null = df.Age.notnull()
dq_age = age_not_null.sum() / len(df)
print(f"Data Quality of Age: {dq_age}")

cabin_not_null = df.Cabin.notnull()
dq_cabin = cabin_not_null.sum() / len(df)
print(f"Data Quality of Cabin: {dq_cabin}")

embarked_not_null = df.Embarked.notnull()
dq_embarked = embarked_not_null.sum() / len(df)
print(f"Data Quality of Embarked: {dq_embarked}")

print(f"Completeness: {(dq_fare + dq_ticket + dq_parch + dq_sibsp + dq_sex + dq_name + dq_pclass + dq_survived + dq_passenger_id + dq_age + dq_cabin + dq_embarked) / 12}")
