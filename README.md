# Outlook Monitor

## Introduction

This microservice consists of several program files, or scripts, written in Python that interact 
with Microsoft Azure Active Directory and Office 365 Outlook/Exchange mailboxes.

## Requirements
Azure Active Directory
Office 365 Outlook/Exchange mailbox(es)

**Note:** This application will leverage the Microsoft Graph APIs.
## Getting Started
In order to interact with Microsoft Graph your application must have an access token. 
To get an access token, the application must be able to successfully authenticate to the 
Azure Active Directory.  

So the first thing we must do, is register our application, so that it can authenticate and 
receive a token from our Azure Active Directory Tenant.

## Application Registration

In your Azure portal

Choose **Azure Active Directory > App registrations > New application registration**

![APP REGISTRATION][logo1]

[logo1]: https://github.com/clintmann/exchange-monitor/blob/master/images/App_registration.gif "App Registration"
 
Give your application a name, Sign-on  URL and click Create
![CREATE APP][logo2]

[logo2]: https://github.com/clintmann/exchange-monitor/blob/master/images/Create_app.gif "Create App"
 
Next you will need to generate a key for you application to use. 
Click **Settings > Keys**

![GENERATE KEY][logo3]

[logo3]: https://github.com/clintmann/exchange-monitor/blob/master/images/Settings_generate_key.gif "Generate Key"

Give your Key a Description and Expiration time and click Save Click Save to Generate the key

![KEYS][logo4]

[logo4]: https://github.com/clintmann/exchange-monitor/blob/master/images/Keys.gif "Key"
 
For more information take a look at this [tutorial](https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-register-applications#register-a-web-app)

![REQUIRED PERMISSIONS][logo5]

[logo5]: https://github.com/clintmann/exchange-monitor/blob/master/images/Required_permissions.gif "Required Permissions"
 

## How it works

