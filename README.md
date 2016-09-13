Workspace Kludge
================

A quick and dirty script for showing a notification upon workspace switch. To use: either run as

~~~
./workspace-kludge.py
~~~

Or add it to the list of startup applications on your desktop.

This project is based on:

http://askubuntu.com/questions/15971/getting-visual-feedback-of-workspace-switch-in-xfce

You have to configure it by inputting the number of workspace rows and columns in the script (defaults to 3x4). Afterwards it shows you the name of the current workspace + an ASCII grid showing the current workspace.

ASCII art will only work if your notification daemon uses monospace text.

TODO: switch the current desktop launchers depending on current desktop.
