<div>
   <h1 align="center">
     <img height="32" width="32" src="https://cdn.simpleicons.org/faceit/FF5500"/>
     AutoFaceIT
  </h1>
</div>

![GitHub all releases](https://img.shields.io/github/downloads/McDoom51/AutoFaceIT/total?style=for-the-badge)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/mcdoom51/autofaceit/main?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/mcdoom51/autofaceit?style=for-the-badge)

---

AutoFaceIT provides an automated solution to streamline the process of launching CSGO with FaceIT Anti-Cheat, enhancing the convenience and user experience for players.

The script designed to automate the launching of CSGO with FaceIT Anti-Cheat. It ensures that CSGO is closed, launches FaceIT Anti-Cheat if it is not already running, and then launches CSGO again. The script is continuously monitors the CSGO and FaceIT Anti-Cheat processes to maintain the desired state.

The script will run as a system service. This is to ensure that the script will automatically launch when the computer is turned on, so you don't need to worry about it.

The script have been repackaged into an executable, after the script can't be run as a system service otherwise.
There is a released package that contains the script file, so you can build the executable yourself.

## Features:
- Automatic restart of CSGO when FaceIT Anti-Cheat is launched.
   - Launching of FaceIT Anti-Cheat if it is not already running.
   - Launching of CSGO when FaceIT Anti-Cheat is running.
- Continuous monitoring of CSGO and FaceIT Anti-Cheat.

## Prerequisites

- Python 3.x installed (The included bat file will check if Python is installed, and will install it if it's missing)

## Installation

- Easy Installation
   1. [Download the package]()
   2. Unzip the downloaded folder onto a location of your choicing.
   3. Run Install.bat
 
 - Build the program yourself
   1. [Download the package]()
   2. Unzip the downloaded folder onto a location of your choicing.
   3. [Download py2exe]()
   4. Build the package accordingly to the provided documentation in the downloaded folder.
   5. Run Install.bat

When this is done, the program is now actively on your computer and working.

## Uninstallation

1. Run the Uninstall.bat file.
> The file is located in the same folder as the program
2. The script is now uninstalled, and all traces of the script are removed.

## Logging

The script logs events and errors to a `script.log` file. You can check this log file for information on the script's execution, including any errors that may occur.

If you need help with the error, please open a [ticket](https://github.com/McDoom51/AutoFaceIT/issues/new) with the log file

## Contributing

Contributions to AutoFaceIT are welcome! If you have any improvements, bug fixes, or new features to propose, please submit a pull request.

## Disclaimer

This script is provided as-is and without any warranties. Use it at your own risk. The authors and contributors of this project are not responsible for any damages or legal implications that may arise from its use.

## Authors

- [@McDoom51](https://www.github.com/McDoom51)
