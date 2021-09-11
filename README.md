# LoginRFID

Authentication using RFID (Radio-frequency identification) tags. Runs at boot, and/or can be configured to run at terminal sessions on Raspberry Pi.

## Working

Master tag is used to generate a MD5 hash which then can be cloned to non master tags. The hash is generated using the **master tag's UID, MAC address of the device, and timestamp**. The hash is stored onto a file which contains the hash with a signature. While reading, the reading script checks for valid hash before reading tags. To avoid keyboard interrupts, when exceptions are raised, it loops the script. Upon verifying, script is exited. 

Using hardware as an authentication factor is likely to be more realiable verus software in today's world. (Ofcourse, until they aren't lose!)

## Future Improvements

1. Implement database connectivity to send and retrieve hashes.
2. Better exception handling.

## Demo

[![demo](https://asciinema.org/a/fya448W8HEdupamxscgRSYzSi.svg)](https://asciinema.org/a/fya448W8HEdupamxscgRSYzSi?autoplay=1)

NOTE: I have mapped the script to run at every SSH session. Kills sessions if authentication fails (I'm aware this kills the whole point of remote connection, but I only intented to use it as a test environment).

## Built Using

* [Python](https://www.python.org/)
* [Bash](https://www.gnu.org/software/bash/)

## Connections

On your RFID RC522 you will notice that there are 8 possible connections on it, these being SDA (Serial Data Signal), SCK (Serial Clock), MOSI (Master Out Slave In), MISO (Master In Slave Out), IRQ (Interrupt Request), GND (Ground Power), RST (Reset-Circuit) and 3.3v (3.3v Power In). We will need to wire all of these but the IRQ to our Raspberry Pi’s GPIO pins.

| Module Pin Name | Module Physical Pin |    RPi Pin Name   | RPi Physical Pin |
|       ---       |         ---         |      ---          |        ---       |
| **SDA**         | 1                   | GPOI 8(SPI_CE0)   | **24**           |
| **SCK**         | 2                   | GPOI 11(SPI_SCLK) | **23**           |
| **MOSI**        | 3                   | GPOI 10(SPI_MOSI) | **19**           |
| **MISO**        | 4                   | GPOI 9(SPI_MISO   | **21**           |
| **IRQ**         | 5                   | ---               | **---**          |
| **GND**         | 6                   | GND               | **6**            |
| **RST**         | 7                   | GPOI 25           | **22**           |
| **3.3V**        | 8                   | 3.3v              | **1**            |

## Usage

*To generate **hash** and write it to RFID tag*
```
python3 <path-to-write.py-file>
```
###### hash.dat file will be created in the folder containing write.py

*To **test** authentication script*
```
python3 <path-to-read.py-file>
```
###### NOTE: keyboardInterrupts are excepted and main function is called forming a loop

*To **copy/clone** RFID tag*
```
python3 <path-to-clone.py-file>
```
###### Function will prompt for source and destination tags

**Edit the rc(run commands):**

*To run the script at **boot**, edit **/etc/rc.local***
```
echo "python3 <path-to-read.py-file>">>/etc/rc.local
```
###### Appends the command to the end of the [rc.local](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md) file

*To run the script at **terminal sessions**, edit **$HOME/.bashrc***
```
echo "python3 <path-to-read.py-file>">>/etc/rc.local
```
###### Appends the command to the end of the [.bashrc](https://www.raspberrypi.org/documentation/linux/usage/bashrc.md) file
###### **NOTE: Ensure write.py file is run before read.py and all files (hash.dat, write.py, read.py, clone.py) are in the same folder.**

## Author

* **Dhivakar Chelladurai** - <img src="https://dhivakar.xyz/images/logo.png" width=12px height=12px > <a href="https://dhivakar.xyz">dhivakar.xyz</a>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
