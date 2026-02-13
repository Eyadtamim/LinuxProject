# LinuxProject

# Note-Taking Web App with EBS Backup Strategy

## Project Overview
[cite_start]This project involves deploying a simple note-taking web application on an AWS EC2 instance using RHEL 10[cite: 3, 5, 11]. [cite_start]The application allows users to write and submit notes, which are stored in a MariaDB database with a timestamp and displayed on the webpage[cite: 5, 25, 27]. [cite_start]Additionally, a backup strategy is implemented using a dedicated 100 GiB EBS volume[cite: 36, 37].

---

## 1. Prerequisites
* [cite_start]**AWS Free Tier Account**[cite: 9].
* [cite_start]**EC2 Instance:** Red Hat Enterprise Linux (RHEL) 10 (t2.micro/t3.micro)[cite: 11, 18, 19].
* [cite_start]**Security Group:** Inbound rules for Port 22 (SSH) and Port 80 (HTTP)[cite: 21].
* [cite_start]**Storage:** One additional 100 GiB EBS volume[cite: 36].

---

## 2. Execution Steps

### Step 1: Install MariaDB & Dependencies
[cite_start]Update the system and install the MariaDB server and Python environment[cite: 30].
```bash
sudo dnf update -y
sudo dnf install mariadb-server python3-pip -y
sudo systemctl enable --now mariadb

Step 2: Configure MariaDB Schema
Connect to MariaDB and create the necessary database and table structure to store user notes.

SQL
-- Access MariaDB
sudo mysql -u root

-- Create and configure the database
CREATE DATABASE notes_app;
USE notes_app;

-- Create table to store notes with timestamps
CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    note_content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- (Optional) Create a dedicated app user
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON notes_app.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

Step 3: Deploy the Web Application
Develop the app using Python/Flask or Go.


Functionality: Users submit notes via a web form.


Display: Notes must appear at the top of the list with the date and time of creation.

Note: Ensure index.html is located in a folder named templates/ to avoid TemplateNotFound errors.

Step 4: Mount the Backup Volume
Attach and mount the additional EBS volume under /backup. Note that modern Nitro instances map EBS volumes to NVMe device paths.

Identify the 100G volume: lsblk

Format and mount:

Bash
# Format the volume as XFS
sudo mkfs.xfs /dev/nvme1n1 

# Create the backup directory and mount it
sudo mkdir /backup
sudo mount /dev/nvme1n1 /backup
Step 5: Implement Backup Strategy
Implement a process to back up MariaDB data to the mounted volume.

Bash
# Manual backup command to /backup directory
sudo mysqldump -u root notes_app > /backup/notes_db_backup_$(date +%F).sql
3. Deliverables

Source Code: Python or Go application files.


Screenshots: The running application on EC2.


Database: Evidence of MariaDB schema and tables.


Backup: Evidence of database backups stored in /backup
