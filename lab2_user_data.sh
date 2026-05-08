#!/bin/bash

Update the OS packages
yum update -y

Install the Apache Web Server
yum install -y httpd

Start the web server service
systemctl start httpd

Enable the service to automatically start on system reboots
systemctl enable httpd

Generate the static website content
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Samael's Armageddon Lab 2</title>
    <style>
        /* Requirement: Background Color */
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background-color: #1e272e; 
            color: #d2dae2; 
            margin: 0; 
            padding: 40px; 
        }
        .container { 
            max-width: 800px; 
            margin: auto; 
            background-color: #2c3e50; 
            padding: 30px; 
            border-radius: 10px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        }
        section { 
            margin-bottom: 30px; 
            padding-bottom: 20px; 
            border-bottom: 1px solid #485460; 
        }
        .footer { 
            text-align: center; 
            font-size: 0.9em; 
            color: #808e9b; 
            border-bottom: none; 
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Samael King - Lab 2 Web Server</h1>

        <section>
            <h2>About Me</h2>
            <p>Greetings! I'm Samael. I'm currently drilling AWS infrastructure setups to build muscle memory for the GCP-PCA and the SAA-C03 exam.</p>
        </section>

        <section>
            <h2>Project Description: CPG Armageddon</h2>
            <p>This web page is hosted on an Amazon EC2 instance deployed within a custom VPC. The web server (Apache) and this HTML file were dynamically generated using an automated Bash User Data script upon boot.</p>
            
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" alt="AWS Logo" style="width:200px; background-color:white; padding:10px; border-radius:5px; margin-top:10px;">
        </section>

        <section class="footer">
            <h2>Contact</h2>
            <p>If the server is down, I'm probably out moto-vlogging.</p>
            <p>&copy; 2026 Samael King | Cloud Proving Ground</p>
        </section>
    </div>
</body>
</html>
