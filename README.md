---

## Lab 2: Automated EC2 Web Server Provisioning (CPGA2025)

**Deliverables:**
* **Automation:** Deployment managed via `lab2_user_data.sh`.
* **Infrastructure:** Custom VPC, 1 Public Subnet, 1 IGW, Security Group allowing HTTP/SSH.

### Evidence of Infrastructure

**EC2 Instance Running & Security Group Inbound Rules:**
![EC2 Instance and Security Group](Screenshot%202026-05-08%20161223.png)

**Live Web Server Rendering Custom User Data Script:**
![Live Web Server](Screenshot%202026-05-08%20160859.png)

### Script Logic Explanation
This phase of the project fully automates the provisioning of an Apache web server upon EC2 boot. 
* It utilizes `yum` package manager commands to update the OS, install the `httpd` daemon, and configure the service to start automatically. 
* It leverages a Linux "Here-Doc" (`cat <<EOF >`) to dynamically construct the webpage. This allows the script to inject raw HTML, inline CSS, and absolute image URLs directly into the server's default document root (`/var/www/html/index.html`) in a single execution, entirely eliminating the need for manual file transfers or secondary style sheets.
