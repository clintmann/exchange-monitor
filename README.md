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

<img src= "https://github.com/clintmann/exchange-monitor/blob/master/images/App_registration.gif" width="800" height="500" />


Give your application a name, Sign-on  URL and click Create


<img src= "https://github.com/clintmann/exchange-monitor/blob/master/images/Create_app.gif" width="300" height="300" />

 
Next you will need to generate a key for you application to use. 
Click **Settings > Keys**

<img src= "https://github.com/clintmann/exchange-monitor/blob/master/images/Settings_generate_key.gif" width="800" height="500" />


Give your Key a Description and Expiration time and click Save Click Save to Generate the key

<img src= "https://github.com/clintmann/exchange-monitor/blob/master/images/Keys.gif" width="400" height="200" />

 
Our application with be interacting with Microsoft Graph via REST APIs. We will want to assign the appropriate level of permissions to grant acces only to the APIs we need and nothing more. 
Do this by checking the box next to the access you would like to assign. 

<img src= "https://github.com/clintmann/exchange-monitor/blob/master/images/Required_permission.gif" width="800" height="400" />


For this application we are going to enable 1 permission for Azure AD and three permissions for Microsoft Graph.

**Windows Azure Active Directory API Permissions**
1. Read directory data

<img src= "https://github.com/clintmann/exchange-monitor/blob/master/images/Enable_Access_AzureAD.gif" width="800" height="400" />


**Microsoft Graph API Permissions**
1. Read all users' full profiles
2. Read all user mailbox settings
3. Read directory data

<img src= "https://github.com/clintmann/exchange-monitor/blob/master/images/Enable_Access_Graph.gif" width="800" height="900" />

 
Finally you must click Grant permissions in order for your choices to take affect.

<img src= "https://github.com/clintmann/exchange-monitor/blob/master/images/Grant_permissions.gif" width="500" height="300" />


For more information take a look at this [tutorial](https://docs.microsoft.com/en-us/azure/active-directory-b2c/tutorial-register-applications#register-a-web-app)

## How it works

