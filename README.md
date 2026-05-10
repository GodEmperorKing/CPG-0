## Lab 1: Branching, Git, & Python Collaboration (CPGA2025)

**Deliverables:**
* **Version Control:** Managed branch creation, commits, and merge conflict resolution via Git and GitHub.
* **Code Artifacts:** Python scripting collaboration (`app.py`, `greetings.py`).

### Evidence of Execution

**Git Branching & Merge History:**
![Git Branching Evidence](assets/Screenshot%202026-04-28%20200617.png)

**Python Script Execution/Collaboration:**
![Python Script Evidence](assets/Screenshot%202026-04-28%20200737.png)

**Upstream Remote Configuration:**
![Upstream Connection Evidence](assets/Screenshot%202026-04-28%20200810.png)

### Lab Logic Explanation
This foundational lab established the core Git workflows required for modern cloud engineering and DevOps. It involved creating isolated feature branches to write basic Python functions, staging and committing changes, and successfully executing a merge back into the main production branch. This simulates a standard, collaborative infrastructure-as-code pipeline.
---
## Lab 2: Automated EC2 Web Server Provisioning (CPGA2025)

**Deliverables:**
* **Automation:** Deployment managed via `lab2_user_data.sh`.
* **Infrastructure:** Custom VPC, 1 Public Subnet, 1 IGW, Security Group allowing HTTP/SSH.

### Evidence of Infrastructure

**EC2 Instance Running & Security Group Inbound Rules:**
![EC2 Instance and Security Group](assets/Screenshot%202026-05-08%20161223.png)

**Live Web Server Rendering Custom User Data Script:**
![Live Web Server](assets/Screenshot%202026-05-08%20160859.png)

### Script Logic Explanation
This phase of the project fully automates the provisioning of an Apache web server upon EC2 boot.
* The utility `yum` package manager commands to update the OS, install Apache (`httpd`), deepen configuration via the `systemctl` daemon, and configure a custom HTML landing page.
* This mimics an immutable infrastructure approach where the server is fully configured without manual intervention.
