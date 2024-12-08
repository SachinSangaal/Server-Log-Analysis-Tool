<h1><strong>Log Analysis Tool</strong></h1><br>
<h2>Overview</h2><br>
<p>
    The Log Analysis Tool is a Python-based application designed to parse, analyze, and extract meaningful insights from log files. 
    It identifies key patterns, such as request counts by IP addresses, the most frequently accessed endpoints, and suspicious activities 
    like repeated failed login attempts.
</p>

<h3>Features</h3>
<ul>
    <li><strong>Log Parsing:</strong> Reads and processes log files line-by-line.</li>
    <li><strong>Log Analysis:</strong>
        <ul>
            <li>Counts requests by IP addresses.</li>
            <li>Identifies the most frequently accessed endpoint.</li>
            <li>Detects suspicious IPs based on a configurable threshold for failed login attempts.</li>
        </ul>
    </li>
    <li><strong>Output Handling:</strong>
        <ul>
            <li>Saves analysis results to a structured CSV file.</li>
            <li>Organizes results into categories for easy interpretation.</li>
        </ul>
    </li>
</ul>

<h3>Project Structure</h3>
<pre>
project-root/
│
├── logs/                       # Contains input log files.
│   └── sample.log              # Example log file for testing.
│
├── output/                     # Directory for analysis results.
│   └── log_analysis_results.csv
│
├── source/                     # Source code files.
│   ├── main.py                 # Entry point of the application.
│   ├── log_parser.py           # Handles log file reading and parsing.
│   ├── log_analyzer.py         # Analyzes parsed logs for insights.
│   ├── log_utils.py            # Utility functions for log processing.
│   ├── output_handler.py       # Manages saving results to CSV.
│   └── config.py               # Configuration for file paths and thresholds.
│
└── README.md                   # Project documentation.
</pre>

<h3>Installation</h3>
<p>Clone the repository:</p>
<pre>
git clone https://github.com/your-repo/log-analysis-tool.git
cd log-analysis-tool
</pre>



<h3>Configuration</h3>
<p>Adjust the following parameters in <code>config.py</code> to fit your needs:</p>
<ul>
    <li><strong>LOG_FILE_PATH:</strong> Path to the input log file.</li>
    <li><strong>OUTPUT_FILE_PATH:</strong> Path to save the analysis results.</li>
    <li><strong>SUSPICIOUS_IP_THRESHOLD:</strong> Threshold for flagging suspicious IPs based on failed login attempts.</li>
</ul>

<h3>Usage</h3>
<p>Place the log file you want to analyze in the <code>logs/</code> directory.</p>
<p>Update the <code>LOG_FILE_PATH</code> in <code>config.py</code> to match your log file's name.</p>
<p>Run the tool:</p>
<pre>
python source/main.py
</pre>
<p>The results will be displayed in the console and saved to the file specified in <code>OUTPUT_FILE_PATH</code>.</p>

<h3>Output Format</h3>
<p>The analysis results are saved as a CSV file with the following sections:</p>
<ul>
    <li><strong>IP Address Request Counts</strong>
        <ul>
            <li>IP Address</li>
            <li>Request Count</li>
        </ul>
    </li>
    <li><strong>Most Accessed Endpoint</strong>
        <ul>
            <li>Endpoint</li>
            <li>Access Count</li>
        </ul>
    </li>
    <li><strong>Suspicious Activity</strong>
        <ul>
            <li>Suspicious IP</li>
            <li>Failed Attempts</li>
        </ul>
    </li>
</ul>


<h3>Future Enhancements</h3>
<ul>
    <li>Add support for analyzing IPV6 log formats.</li>
    <li>Integrate a web-based interface for uploading logs and viewing results.</li>
    <li>Extend functionality to support larger files real-time log analysis.</li>
</ul>
