# LinuxProject

Project: Note-Taking Web App with EBS Backup

Title: Deploy a Note-Taking Website on AWS EC2 with Backup Strategy 


Objective: Set up and deploy a note-taking web application on an AWS EC2 instance using Python/Flask, connect it to a MariaDB database, and implement a backup solution using an additional EBS volume.

1. Prerequisites

EC2 Instance: Red Hat Enterprise Linux (RHEL) 10 (t2.micro/t3.micro).
+1


Security Groups: Allow inbound traffic on Port 22 (SSH) and Port 80 (HTTP).


EBS Volume: One additional 100 GiB EBS volume attached to the instance.

2. Execution Steps
Step 1: Install MariaDB & Dependencies
Update the system and install the database server.

Bash
sudo dnf update -y
sudo dnf install mariadb-server python3-pip -y
sudo systemctl enable --now mariadb
Step 2: Configure MariaDB Schema
Use the following commands to set up the database and the table required to store notes with timestamps.

SQL
-- Access MariaDB
sudo mysql -u root

-- Create and configure the database
CREATE DATABASE notes_app;
USE notes_app;

-- Create table to store notes
CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    note_content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a user for the application
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON notes_app.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
Step 3: Deploy the Web Application
The application allows users to submit notes which are then displayed with a timestamp. Ensure your project directory follows this structure to avoid TemplateNotFound errors:
+1

Plaintext
/home/ec2-user/notes-app/
├── app.py
└── templates/
    └── index.html  <-- Your HTML form must be here
Step 4: Mount the Backup Volume
Attach the 100 GiB EBS volume in the AWS Console. Note that on RHEL Nitro instances, the device appears as an NVMe drive (e.g., /dev/nvme1n1) rather than /dev/xvdf.

Find the device name: lsblk


Format and mount: 

Bash
# Format the 100G volume
sudo mkfs.xfs /dev/nvme1n1 

# Create mount point and mount
sudo mkdir /backup
sudo mount /dev/nvme1n1 /backup
Step 5: Implement Backup Process
Create a backup of the MariaDB data to the /backup volume.

Bash
sudo mysqldump -u root notes_app > /backup/notes_db_backup_$(date +%F).sql
3. Deliverables 

Source code for the web app (Python).

Screenshots of the running app on EC2.

MariaDB schema and tables.

Configuration of the mounted /backup volume.

Evidence of database backup stored in /backup.

Project documentation.
