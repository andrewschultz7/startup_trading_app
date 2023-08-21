# startup_trading_app

Automation app that opens needed desktop applications and logins in when appropriate.

## Table of Contents

[TOC]

## Libraries:

- pyautogui
- selenium
- dotenv
- pywinauto
- opencv-python
- webdriver-manager

## Global Problem

User wants to sit back with morning drink and watch these apps open and log in on their own.
Developer wants to use different approaches for each app if possible.

- Tradovate site
- Tradingview app
- TOS app

## Tradovate

**Tradovate site Problem**<br />
User wants to watch tradovate website open and username and password autofill.

**Tradovate site Solution**<br />
Utilize selenium to access chrome and insert username and password into respective fields.

**Issue**<br />
Struggling to keep webpage open.<br />
**Solution**<br />
Added newer ChromeDriverManger to handle drivers.

## Tradingview

**Tradingview app Problem**<br />
User wants to watch tradingview app open and login if necessary.

**Tradingview app Solution**<br />
Utilize pywinauto to open app and pyautogui to access elements. Use image recognition to find elements.

**Issue**<br />
This app is part of windows apps.<br />
**Solution**<br />

- Researched accessing windows apps.
- Decided on image recognition to find elements since element tags were not easily accessible

**Issue**<br />
Some elements could have more than one state.<br />
**Solution**<br />

- Inserted multiple state images into list
- coded conditional statement for multiple state images

**Issue**<br />

- locateCenterOnScreen method is long for conditional statement
- webpage could show "pick your login", "grant access", or "username/password fields"<br />

**Solution**<br />

- coded anonymous function to run conditional statement
- function also allows for any size list and any login potentials

## TOS

**TOS app problem**<br />
User want to watch TOS open and login<br />

**TOS app solution**<br />
Utilize pywinauto to open app and pyautogui to access elements.

**Issue**<br />
TOS password field not accessible.<br />
**Solution**<br />
User pyautogui to match password field image.<br />
