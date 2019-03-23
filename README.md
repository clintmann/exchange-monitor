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

[logo1]: https://github.com/clintmann/exchange-moitor/blob/master/images/App_registration.gif "Registration Image"

- **Register Application:** 

## How it works

The python script is started when the user enters global configuration mode. We will use an Embedded Event Manager (EEM) applet as the trigger. When the user exists out of global configuration mode a separate EEM script is used to terminate the python script process.
