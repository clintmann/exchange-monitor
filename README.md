# Outlook Monitor

## Introduction

This microservice consists of several program files, or scripts, written in Python that interact 
with Microsoft Azure Active Directory and Office 365 Outlook/Exchange mailboxes.

## Requirements
* Azure Active Directory
* Office 365 Outlook/Exchange mailbox(es)

**Note:** This application will leverage the Microsoft Graph APIs.

## Getting Started
In order to interact with Microsoft Graph your application must have an access token. 
To get an access token, the application must be able to successfully authenticate to the 
Azure Active Directory.  

The first thing we must do is register our application so that it can authenticate and 
receive a token from our Azure Active Directory Tenant.

## Application Registration

In your Azure portal

Choose **Azure Active Directory > App registrations > New application registration**

<img src= "https://github.com/clintmann/exchange-monitor/blob/master/images/App_registration.gif" width="500" height="500" />

![APP REGISTRATION][logo1]

[logo1]: (https://github.com/clintmann/exchange-monitor/blob/master/images/App_registration.gif =100x)"App Registration"
 
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
 
Our application with be interacting with Microsoft Graph via REST APIs. We will want to assign the appropriate level of permissions to grant acces only to the APIs we need and nothing more. 
Do this by checking the box next to the access you would like to assign. 


![REQUIRED PERMISSION][logo6]

[logo6]: https://github.com/clintmann/exchange-monitor/blob/master/images/Required_permission.gif "Required Permission"

For this application we are going to enable 1 permission for Azure AD and three permissions for Microsoft Graph.

**Windows Azure Active Directory API Permissions**
1. Read directory data


![AD Access][logo7]

[logo7]: https://github.com/clintmann/exchange-monitor/blob/master/images/Enable_Access_AzureAD.gif "AD Access"
 

**Microsoft Graph API Permissions**
1. Read all users' full profiles
2. Read all user mailbox settings
3. Read directory data


![Graph Access][logo8]

[logo8]: https://github.com/clintmann/exchange-monitor/blob/master/images/Enable_Access_Graph.gif "Graph Access"
 
 
Finally you must click Grant permissions in order for your choices to take affect.


![Grant Permissions][logo9]

[logo9]: https://github.com/clintmann/exchange-monitor/blob/master/images/Grant_permissions.gif "Grant Permissions"
 


For more information take a look at this [tutorial](https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-register-applications#register-a-web-app)

## How it works

