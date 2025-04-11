# Load Libraries
import pandas as pd
import fireducks.pandas as fd
import time
import numpy as np



# -----------------------------------
# STEP 1: Create Dummy Sales Dataset
df = pd.DataFrame({
    "product": np.random.choice(["apple", "banana", "orange", "kiwi"], size=1_000_000),
    "region": np.random.choice(["north", "south", "east", "west"], size=1_000_000),
    "price": np.random.uniform(10, 200, size=1_000_000),
    "units_sold": np.random.randint(1, 50, size=1_000_000)
})


df.to_csv("sales_data.csv", index=False)
print("✅ Created 'sales_data.csv'")


# -----------------------------------
# STEP 2: Read CSV
start = time.time()
pandas_df = pd.read_csv("sales_data.csv")
print("📄 Pandas Read Time:", round(time.time() - start, 4), "sec")

start = time.time()
fd_df = fd.read_csv("sales_data.csv")
print("🔥 FireDucks Read Time:", round(time.time() - start, 4), "sec")


# -----------------------------------
# STEP 3: Filter → price > 100
start = time.time()
filtered_pandas = pandas_df[pandas_df['price'] > 100]
print("📉 Pandas Filter Time:", round(time.time() - start, 4), "sec")

start = time.time()
filtered_fd = fd_df[fd_df['price'] > 100]
print("🔥 FireDucks Filter Time:", round(time.time() - start, 4), "sec")


# -----------------------------------
# STEP 4: Group by region, average price
start = time.time()
group_pandas = filtered_pandas.groupby('region')['price'].mean().reset_index()
print("📊 Pandas GroupBy Time:", round(time.time() - start, 4), "sec")

start = time.time()
group_fd = filtered_fd.groupby('region')['price'].mean().reset_index()
print("🔥 FireDucks GroupBy Time:", round(time.time() - start, 4), "sec")


# -----------------------------------
# STEP 5: Sort by average price descending
start = time.time()
sorted_pandas = group_pandas.sort_values(by='price', ascending=False)
print("🔽 Pandas Sort Time:", round(time.time() - start, 4), "sec")

start = time.time()
sorted_fd = group_fd.sort_values(by='price', ascending=False)
print("🔥 FireDucks Sort Time:", round(time.time() - start, 4), "sec")

# -----------------------------------
print("✅ Sales Benchmark Completed!")
