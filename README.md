## Lab 2: Automated EC2 Web Server Provisioning
**Deliverables & Script Logic:**
This phase of the project fully automates the provisioning of an Apache web server upon EC2 boot. 
* It utilizes `yum` package manager commands to update the OS, install the `httpd` daemon, and configure the service to start automatically. 
* It leverages a Linux "Here-Doc" (`cat <<EOF >`) to dynamically construct the webpage. This allows a simple approach to script inject raw HTML, inline CSS, and absolute image URLs directly into the server's default document root (`/var/www/html/index.html`) in a single execution, eliminating the need for manual file transfers or dealing with imagines, resizing etc.
