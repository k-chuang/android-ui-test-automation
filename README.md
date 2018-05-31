# Appium Mobile UI Test Automation
This project is just a basic outline on how to set up [appium](http://appium.io/), an open source test automation framework for native, mobile web, and hybrid applications, and use it to run automated UI tests for Android apps.

Appium is cross-platform, and supports a lot of mobile platforms (iOS mobile, Android mobile) as well as mobile web applications (Safari on iOS, Chrome on Android).

## Setup
1. Install [Java JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
  - Using the SDK Manager, you can:
    - Install all the necessary packages, Android versions, etc.
    - (Optional) Install adb in the 'Extras' tab
      - Only do this if you want to test a physical device, otherwise, you do not need to do this step, since you can run emulators to emulate Android or iOS devices.
2. Set JAVA_HOME in environment variables, and reference it in PATH environment variable.
  - For Windows:
    - from control panel, edit environment variables window and add the following
    ```console
    JAVA_HOME=C:\Program Files\Java\jdk1.8.0_45
    ```
    
    ```console
    PATH = C:\Program Files\Java\jdk1.8.0_45\bin;
    ```
  - For MacOS:
    - in your ~/.bash_profile
    ```bash
    export JAVA_HOME= '/usr/libexec/java_home'
    ```
    ```bash
    export PATH = $PATH:$JAVA_HOME/bin
    ```
3. Install [Android SDK](https://developer.android.com/studio/index.html)
  - Use SDK Manager to install necessary packages, such as Android SDK Build Tool, Android versions and their APIs, etc.
4. Set ANDROID_HOME in environment variables, and reference it in PATH environment variable.
  - See step 2 for a similar reference.
5. Install appium via 2 ways:
  - via NPM (Node.js Package Manager)
    - Assuming you have already installed [Node.js](https://nodejs.org/en/)
    ```bash
    npm install -g appium
    ```
  - via [Desktop App Download](https://github.com/appium/appium-desktop/releases/tag/v1.6.1)
    - [Windows 64 bit Desktop Download](https://github.com/appium/appium-desktop/releases/download/v1.6.1/appium-desktop-setup-1.6.1.exe)
    - [MacOS Desktop Download](https://github.com/appium/appium-desktop/releases/download/v1.6.1/Appium-1.6.1.dmg)

## Procedure
I will give just a high level summary of the procedure of how to use Appium for UI test automation with a physical Android device.

1. I opened the Appium Desktop application, and set the appropriate host IP address, and port number.
2. I enable the 'Developer Options' and turn it on
  - This step is necessary to do for programmatic interaction via adb
3. I connect the Android device via USB to my laptop
  - Run 'adb devices' in the shell to double check that it is properly connected
4. Install the Appium Client Python library via:
  ```bash
  pip install Appium-Python-Client
  ```
5. Start coding in Python!
  - Used unittest to write test cases and test suite
  - Used pytest as the test runner to execute the test suite
  - See [code])()
6. Used [UI Automator Viewer](https://developer.android.com/training/testing/ui-automator#ui-automator-viewer) to view elements of the Android app and incorporate within code.
