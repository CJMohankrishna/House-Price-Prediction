import joblib
import pandas as pd
model = joblib.load("models/house_price_model.pkl")
scaler = joblib.load("models/scaler.pkl")
features = joblib.load("models/features.pkl")
new_house = pd.DataFrame(
    [[0] * len(features)],
    columns=features
)
print(type(model))
print(type(scaler))
overall_qual = int(input("Enter Overall Quality (1-10): "))
lot_area = float(input("Enter Lot Area: "))
garage_cars = int(input("Enter Garage Cars: "))
year_built = int(input("Enter Year Built: "))
new_house["OverallQual"] = overall_qual
new_house["LotArea"] = lot_area
new_house["GarageCars"] = garage_cars
new_house["YearBuilt"] = year_built
new_house_scaled = scaler.transform(new_house)
prediction = model.predict(new_house_scaled)
print(f"Predicted House Price: ${prediction[0]:,.2f}")