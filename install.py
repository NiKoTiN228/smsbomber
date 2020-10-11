import os
os.system("pkg install dos2unix")
os.system("pip install requests")
os.system("cp ~/smsbomber/smsbomber.py /data/data/com.termux/files/usr/bin/smsbomber")
os.system("dos2unix /data/data/com.termux/files/usr/bin/smsbomberr")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/smsbomber")
os.system("smsbomber")
