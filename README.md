# nickRestore
Hexchat addon that restore your registered main nickname when it is still in use (GHOST) after a reconnection.

## Use
1. Install python plugin for HexChat:

        sudo apt install hexchat-python3

2. Download the file to the Hexchat addons directory:

        wget -N https://raw.githubusercontent.com/Wibol/nickRestore/main/nickRestore.py -P ~/.config/hexchat/addons/

3. Add your registered nickname password for NickServ to the file:

        nano ~/.config/hexchat/addons/nickRestore.py

4. Run "/LOAD nickRestore.py" in Hexchat or restart it.
