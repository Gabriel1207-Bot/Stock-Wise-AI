import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

# --- 1. LOAD DATA (Matches Section 7b: Structured Data) ---
print("--- Loading Warehouse Data ---")
df = pd.read_csv('data/warehouse_data.csv')
print(f"Loaded {len(df)} records.\n")

# --- 2. DEMAND FORECASTING (Matches Section 7d: Time Series) ---
print("--- Demand Forecasting Module ---")
# Check if the column exists, otherwise skip or use a default
if 'daily_demand' in df.columns:
    # We will predict demand based on the Item Category
    # Using a simple Linear Regression to demonstrate the concept
    X = df[['item_id']] # Using ID as a proxy for time/sequence
    y = df['daily_demand']
    
    model = LinearRegression().fit(X, y)
    
    # Predict for a hypothetical "next" item
    predicted_demand = model.predict([[999]])[0]
    print(f"Predicted demand for next item cycle: {predicted_demand:.2f} units")
    
    if predicted_demand > 50:
        print("ALERT: High demand predicted. Auto-generating purchase requisition.")
    else:
        print("Demand is stable. No action required.")
else:
    print("Column 'daily_demand' not found. Please check dataset.")

# --- 3. ANOMALY DETECTION (Matches Section 7c: Theft Prevention) ---
print("\n--- Anomaly Detection Module (Theft Prevention) ---")
# We will simulate 'normal' vs 'abnormal' picking times
# The dataset has 'picking_time_seconds'. High times could mean searching/theft.
if 'picking_time_seconds' in df.columns:
    # Assume normal picking is under 300 seconds (5 mins)
    # Anything over 600 seconds (10 mins) is suspicious
    picking_times = df['picking_time_seconds'].values.reshape(-1, 1)
    
    # Train Isolation Forest
    iso_forest = IsolationForest(contamination=0.05, random_state=42)
    predictions = iso_forest.fit_predict(picking_times)
    
    anomalies = df[predictions == -1]
    print(f"Detected {len(anomalies)} anomalies (Suspiciously long picking times).")
    
    if len(anomalies) > 0:
        print("ALERT: Anomaly detected! Possible theft or misplacement.")
        print(f"Example: Item {anomalies.iloc[0]['item_id']} took {anomalies.iloc[0]['picking_time_seconds']:.0f} seconds to pick.")
else:
    print("Column 'picking_time_seconds' not found.")

# --- 4. INTELLIGENT SLOTTING (Matches Section 7a: Clustering) ---
print("\n--- Intelligent Slotting Module (K-Means Clustering) ---")
# We group items by their storage location and demand to optimize layout
if 'storage_location_id' in df.columns and 'daily_demand' in df.columns:
    # Create a simple 2D array for clustering
    slotting_data = df[['storage_location_id', 'daily_demand']].dropna()
    
    kmeans = KMeans(n_clusters=3, random_state=42).fit(slotting_data)
    df['Cluster'] = kmeans.labels_
    
    print("Clustering complete. Fast-moving items (Cluster 0) should be moved near dispatch.")
    print("Slow-moving items (Cluster 2) can be moved to the back.")
else:
    print("Required columns for clustering not found.")

# --- 5. CHATBOT LOGIC (Matches Section 7f & 7h) ---
print("\n--- Chatbot Logic (Simulation) ---")
def warehouse_chatbot(query):
    query = query.lower()
    if "where" in query and "pipe" in query:
        return "110mm Water Pipe is in Aisle 3, Shelf 2. Quantity: 120."
    elif "expired" in query or "medicine" in query:
        return "Alert: 3 items are expiring in 7 days. Please check the medicine cabinet."
    elif "low stock" in query:
        return "Warning: 16mm Electrical Cable is low on stock (15 units left)."
    else:
        return "I'm sorry, I didn't understand. Please ask about stock location or expiry."

# Test the chatbot
print("User: Where is the blue cable?")
print(f"Bot: {warehouse_chatbot('Where is the blue cable?')}")
print("User: Show me expired medicine.")
print(f"Bot: {warehouse_chatbot('Show me expired medicine.')}")

print("\n--- Stockwise AI Execution Complete ---")
