# Outlook Monitor

## Introduction

This microservice consists of several program files, or scripts, written in Python that interact 
with Microsoft Azure Active Directory and Office 365 Outlook/Exchange mailboxes.

## Requirements
Azure Active Directory
Office 365 Outlook/Exchange mailbox(es)

**Note:** This application will leverage the Microsoft Graph APIs.
## Getting Started
The first thing we must do, is register our application, so that it can interact with 
our Azure Active Directory Tenant.

## Application Registration
![APP REGISTRATION][logo1]

[logo1]: https://github.com/clintmann/exchange-monitor/blob/master/images/App_registration.gif "App Registration"
 
In your Azure portal

Choose **Azure Active Directory > App registrations > New application registration**

![CREATE APP][logo2]

[logo2]: https://github.com/clintmann/exchange-monitor/blob/master/images/Create_app.gif "Create App"
 

![GENERATE KEY][logo3]

[logo3]: https://github.com/clintmann/exchange-monitor/blob/master/images/Settings_generate_key.gif "Generate Key"
 
![KEYS][logo4]

[logo4]: https://github.com/clintmann/exchange-monitor/blob/master/images/Keys.gif "Key"
 
Click Save to Generate the key
 
For more information take a look at this [tutorial](https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-register-applications#register-a-web-app)
## How it works

