# Scripts

This folder contains Python scripts for generating interactive dashboards using **Plotly** and **Dash**. These scripts analyze Medicare inpatient hospital data, visualize trends, and provide insights into hospital utilization, financial aspects, and disparities.

## 📂 Files Overview

- **`dashboard1.py`** – Utilization & Access Analysis  
  - Visualizes hospital admissions trends over time.  
  - Analyzes inpatient hospital utilization by **geographic region** and **demographics** (age, race, gender).  
  - Identifies which hospital types are most frequently used.  

- **`dashboard2.py`** – Finance & Equity Analysis  
  - Tracks Medicare program payments and their trends.  
  - Compares cost-sharing amounts across **demographic groups** and **hospital types**.  
  - Examines geographic variations in **Medicare spending** and **equity in healthcare access**.  

- **`dashboard3.py`** – Hospital Performance & Policy Impact  
  - Evaluates hospital performance based on **program payments and utilization**.  
  - Investigates the influence of **hospital size and affiliation** (e.g., teaching, rural).  
  - Assesses the **impact of policy changes** on hospital efficiency and patient costs.

- **`cor.py`** – Correlation Analysis  
  - Generates a correlation graph between **Medicare program payments** and **cost-sharing** (deductible + coinsurance).  
  - Uses **Plotly** to create a scatter plot with a trend line.  
  - Helps identify how strongly cost-sharing relates to total program spending.  

## 🚀 Running the Dashboards Locally  

To run a dashboard on your local machine:  

```bash
python dashboard1.py
```

or  

```bash
python dashboard2.py
```

or  

```bash
python dashboard3.py
```

## ⚡ Dependencies  

Ensure you have the required libraries installed:  

```bash
pip install plotly dash pandas numpy gunicorn
```

## 🌐 Deploying on AWS  

### 1️⃣ **Launch an EC2 Instance**  
- Use **Amazon Linux 2** or **Ubuntu**.  
- Select a security group allowing inbound traffic on **port 8050** (or 80 if using a web server).  
- Connect via SSH:  

  ```bash
  ssh -i your-key.pem ec2-user@your-instance-ip
  ```

### 2️⃣ **Set Up Python & Install Dependencies**  
Update and install required packages:  

```bash
sudo yum update -y
sudo yum install python3-pip -y
pip3 install plotly dash pandas numpy gunicorn
```

### 3️⃣ **Transfer Your Scripts to the Server**  
Use SCP to upload your dashboard scripts:  

```bash
scp -i your-key.pem dashboard1.py ec2-user@your-instance-ip:/home/ec2-user/
```

### 4️⃣ **Run Dashboards on EC2**  
Navigate to the script's directory and run:  

```bash
python3 dashboard1.py
```

Or deploy using **Gunicorn** for better performance:  

```bash
gunicorn -w 4 -b 0.0.0.0:8050 dashboard1:server
```

### 5️⃣ **Access Your Dashboard**  
- Open your browser and go to:  
  ```
  http://your-instance-ip:8050
  ```

### 6️⃣ **(Optional) Deploy with Nginx for Production**  
For production, set up **Nginx** as a reverse proxy and configure a systemd service to keep the app running.

These steps allow you to deploy, run, and access the dashboards on AWS. Let me know if you need additional configurations! 🚀
