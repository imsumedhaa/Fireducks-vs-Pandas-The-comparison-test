
🔥 FireDucks vs Pandas: Speed Benchmark on Large Sales Dataset

This project benchmarks the performance of FireDucks vs Pandas for handling large-scale data operations using a synthetic sales dataset with 1 million rows.

We measure the speed of each library across common data engineering tasks such as reading, filtering, grouping, and sorting.
📂 What's Inside
🔧 Operations Benchmarked

  1.Generate a Large Dataset
    Create a synthetic sales dataset with product names, regions, prices, and units sold.

  2.  Read CSV File
    Compare read times for loading a large CSV using Pandas and FireDucks.

  3. Filter Data
    Select rows where price > 100.

  4. Group By
    Calculate the average price of products sold, grouped by region.
 
  5. Sort Values
    Sort the grouped results by average price in descending order.

Each operation's execution time is logged for both Pandas and FireDucks to highlight performance differences.
🧪 How to Run

  Clone the repo:

git clone https://github.com/Srabany/FireDucks_vs._Pandas_Comparisons.git
cd FireDucks_vs._Pandas_Comparisons

Install Dependencies:

pip install pandas fireducks numpy

Run the Script:

  1.python fireducks_vs_pandas_sales_benchmark.py

The script will:

  Generate a CSV with 1M rows

  Run timed operations using both libraries

  Print performance results to the console

📦 Dataset

The dataset is created automatically by the script and saved as:

sales_data.csv

You don’t need to download anything manually.
📊 Sample Output

✅ Created 'sales_data.csv'
📄 Pandas Read Time: 1.2423 sec
🔥 FireDucks Read Time: 0.3391 sec
📉 Pandas Filter Time: 0.0874 sec
🔥 FireDucks Filter Time: 0.0256 sec
📊 Pandas GroupBy Time: 0.0934 sec
🔥 FireDucks GroupBy Time: 0.0312 sec
🔽 Pandas Sort Time: 0.0047 sec
🔥 FireDucks Sort Time: 0.0021 sec
✅ Sales Benchmark Completed!

🚀 Purpose

This mini-project serves as a simple yet powerful demonstration of how FireDucks can provide speed advantages over Pandas in real-world data workflows. Ideal for:

  Data Engineers 👷‍♂️

  Analysts 📊

  Performance geeks ⚡

   Anyone working with big data in Python

🐍 Built With
    Pandas 🐼
    FireDucks 🔥🦆
    NumPy
    Python 3.7+
