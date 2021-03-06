# PlanIt

[![LICENSE](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/Arhaan/PlanIt/blob/master/LICENSE)

## CLI-based Day Planner

The project website is [Plan It](https://arhaan.github.io/PlanIt/)

## Why should I use it?

Are you a student? A professor? An entrepreneur? None of these? Then this app is for you.

I have come across various day planners. But none of them has been able meet my needs. So I am trying to build this customizable daily planner. This is still a work in progress

## Features

* Set events along with their start and end times.
* Customise the commands as per your wish.
* Quickly find what event is scheduled next.

## Details

`v1.0.1`

`timetable.txt` stores the timetable for each day.

`commands.txt` stores the commands and their shortcuts.

Feel free to mail me about the things you liked and disliked in the app. Any features you would like to see in future releases. Have a look at `CONTRIBUTING.md` for further details.

## Commands

* _setEvent_ : To set a new Event : `setEvent Name startTime EndTime`
* _quitCommand_ : To quit the program : `quit`
* _deleteEvent_ : Delete an event : `deleteCommand eventStartTime`
* _displayCommand_ : display an event :  `displayCommand`
* _helpCommand_ : To get help. This command cannot be changed : `help`
* _changeCommandShortcut_: To change shortcut to a command : `changeCommand commandName shortcutName`
* _nowCommand_ : To display the current Event and the next Event scheduled : `now`

## Installation

You will need to have python installed. If you dont have python installed have a look at [Python](https://www.python.org/downloads/). To install this app you will have to:

* Download [PlanIt](https://github.com/Arhaan/PlanIt/archive/v1.0.1.tar.gz) (for Linux and Mac) or [PlanIt](https://github.com/Arhaan/PlanIt/archive/v1.0.1.zip) (for Windows)
* Extract the above `tar.gz` (Linux and Mac) or `.zip`(Windows) file.
* Navigate to this repository in the terminal or command prompt
* run `python planIt.py`

Do comment about any new features you would like to see!
