<h1>🔥 FireDucks vs Pandas: Speed Benchmark on Large Sales Dataset</h1>

<p>This project benchmarks the performance of <strong>FireDucks</strong> vs <strong>Pandas</strong> for handling large-scale data operations using a synthetic sales dataset with <strong>1 million rows</strong>.</p>

<p>We measure the speed of each library across common data engineering tasks such as reading, filtering, grouping, and sorting.</p>

<hr>

<h2>📂 What's Inside</h2>

<h3>🔧 Operations Benchmarked</h3>
<ol>
  <li><strong>Generate a Large Dataset</strong><br>Create a synthetic sales dataset with product names, regions, prices, and units sold.</li>
  <li><strong>Read CSV File</strong><br>Compare read times for loading a large CSV using Pandas and FireDucks.</li>
  <li><strong>Filter Data</strong><br>Select rows where <code>price &gt; 100</code>.</li>
  <li><strong>Group By</strong><br>Calculate the average price of products sold, grouped by region.</li>
  <li><strong>Sort Values</strong><br>Sort the grouped results by average price in descending order.</li>
</ol>

<p>Each operation's execution time is logged for both Pandas and FireDucks to highlight performance differences.</p>

<hr>

<h2>🧪 How to Run</h2>

<ol>
  <li><strong>Clone the repo:</strong>
    <pre><code>git clone https://github.com/Srabany/FireDucks_vs._Pandas_Comparisons.git
cd FireDucks_vs._Pandas_Comparisons</code></pre>
  </li>

  <li><strong>Install Dependencies:</strong>
    <pre><code>pip install pandas fireducks numpy</code></pre>
  </li>

  <li><strong>Run the Script:</strong>
    <pre><code>python fireducks_vs_pandas_sales_benchmark.py</code></pre>

    The script will:
    
      Generate a CSV with 1M rows
      Run timed operations using both libraries
      Print performance results to the console
    
  </li>
</ol>

<hr>

<h2>📦 Dataset</h2>

<p>The dataset is created automatically by the script and saved as:</p>
<pre><code>sales_data.csv</code></pre>
<p>No need to download anything manually.</p>

<hr>

<h2>📊 Sample Output</h2>

<pre><code>✅ Created 'sales_data.csv'
📄 Pandas Read Time: 0.8643 sec
🔥 FireDucks Read Time: 0.0347 sec
📉 Pandas Filter Time: 0.0511 sec
🔥 FireDucks Filter Time: 0.0009 sec
📊 Pandas GroupBy Time: 0.0481 sec
🔥 FireDucks GroupBy Time: 0.0029 sec
🔽 Pandas Sort Time: 0.0007 sec
🔥 FireDucks Sort Time: 0.0004 sec
✅ Sales Benchmark Completed!</code></pre>

<hr>

<h2>🚀 Purpose</h2>

<p>This mini-project serves as a simple yet powerful demonstration of how <strong>FireDucks</strong> can provide speed advantages over <strong>Pandas</strong> in real-world data workflows. Ideal for:</p>
<ul>
  <li>Data Engineers 👷‍♂️</li>
  <li>Analysts 📊</li>
  <li>Performance geeks ⚡</li>
  <li>Anyone working with <strong>big data in Python</strong></li>
</ul>

<hr>

<h2>🐍 Built With</h2>

<ul>
  <li><a href="https://pandas.pydata.org/">Pandas 🐼</a></li>
  <li><a href="https://github.com/Erotemic/fireducks">FireDucks 🔥🦆</a></li>
  <li><a href="https://numpy.org/">NumPy</a></li>
  <li><a href="https://www.python.org/">Python 3.7+</a></li>
</ul>
