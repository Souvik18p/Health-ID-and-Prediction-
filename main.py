from sklearn.linear_model import LinearRegression
import numpy as np
import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.index) + self.timestamp + str(self.data) + self.previous_hash).encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), str(datetime.datetime.now()), data, previous_block.hash)
        self.chain.append(new_block)

# Step 1: Collect input from the user
hospital_name = input("Enter hospital name: ")
patient_name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
doctor_name = input("Enter doctor name: ")
height = float(input("Enter patient height (in meters): "))
weight = float(input("Enter patient weight (in kg): "))
cholesterol_level = float(input("Enter patient cholesterol level: "))
bp_level = input("Enter patient blood pressure level: ")
heart_rate = int(input("Enter patient heart rate: "))
sugar_level = float(input("Enter patient sugar level: "))

# Step 2: Store the input securely in a blockchain
blockchain = Blockchain()
health_id_data = {
    "Hospital Name": hospital_name,
    "Patient Name": patient_name,
    "Age": age,
    "Doctor Name": doctor_name,
    "Height": height,
    "Weight": weight,
    "Cholesterol Level": cholesterol_level,
    "Blood Pressure Level": bp_level,
    "Heart Rate": heart_rate,
    "Sugar Level": sugar_level
}
blockchain.add_block(health_id_data)

# Step 3: Prepare the data for training

X = np.array([[age, cholesterol_level, heart_rate]])
y_cholesterol = np.array([cholesterol_level * 1.05])  # Future cholesterol level (increased by 5%)
y_heart_rate = np.array([heart_rate * 1.05])  # Future heart rate (increased by 5%)

# Step 4: Train regression models
cholesterol_model = LinearRegression()
cholesterol_model.fit(X, y_cholesterol)

heart_rate_model = LinearRegression()
heart_rate_model.fit(X, y_heart_rate)

# Step 5: Make predictions
future_cholesterol_prediction = cholesterol_model.predict(X)[0]
future_heart_rate_prediction = heart_rate_model.predict(X)[0]

# Step 6: Provide output
# You can also implement more sophisticated health metrics based on your requirements
overall_health = "Good" if future_cholesterol_prediction < 200 and future_heart_rate_prediction < 100 and age < 60 else "Needs attention"

# Print the output
print("\n--- Patient Health ID ---")
print("Hospital Name:", hospital_name)
print("Patient Name:", patient_name)
print("Age:", age)
print("Doctor Name:", doctor_name)
print("Height:", height, "m")
print("Weight:", weight, "kg")
print("Cholesterol Level:", cholesterol_level)
print("Blood Pressure Level:", bp_level)
print("Heart Rate:", heart_rate)
print("Sugar Level:", sugar_level)
print("\n--- Future Health Predictions ---")
print("Future Cholesterol Level:", future_cholesterol_prediction)
print("Future Heart Rate:", future_heart_rate_prediction)
print("Overall Health:", overall_health)

# Display the blockchain
print("\n--- Health ID Blockchain ---")
for block in blockchain.chain:
    print("Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print()
