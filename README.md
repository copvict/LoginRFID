# LoginRFID

Authentication using RFID (Radio-frequency identification) tags. Runs at boot, and/or can be configured to run at terminal sessions.

## Scope

Using hardware as an authentication factor is likely to be more realiable verus software in today's world. (Ofcourse, until you don't lose it!)

## Future Improvements

1. Implement functionality for basic commands such as "help", "ls", and "cd" to emulate the CLI experience.
2. User input to navigate through a website. 
3. HackerMode: Random user keystrokes will dump program from a input file.

## Demo

<img src="https://dhivakar.xyz/HTerMinaL.gif">
NOTE: I have mapped the script to run at every SSH session. (I'm aware this kills the whole point of remote connection, but I only intented to use it as a test environment.)

## Built Using

* [Python](https://www.python.org/)
* [Bash](https://www.gnu.org/software/bash/)

## Usage

**script/script.js**

- *Line 2:*
```
var com="blah blah blah<n woo foo boo<nwoof woof woof.";
```
###### use "<n" in the string to break the line as in line 3 

- *Line 25:*
```
domcli.innerHTML+="<p style=\"color:#00ff00; display:inline;\">user@devicename:~$ </p>"+stringArr[i][j++];
```
###### change "user@devicename:~$ " to customize your own [PS1](https://www.gnu.org/software/bash/manual/bashref.html#index-PS1)

## Author

* **Dhivakar Chelladurai** - <img src="https://dhivakar.xyz/images/logo.png" width=12px height=12px > <a href="https://dhivakar.xyz">dhivakar.xyz</a>

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
