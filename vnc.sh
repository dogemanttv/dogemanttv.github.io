sudo apt update
sudo apt install xfce4 xfce4-goodies
sudo apt install tightvncserver
export USER="codespace"
vncserver
vncserver -kill :1
mv ~/.vnc/xstartup ~/.vnc/xstartup.bak
curl https://raw.githubusercontent.com/dogemanttv/dogemanttv.github.io/main/xstartup --output ~/.vnc/xstartup
sudo chmod +x ~/.vnc/xstartup
vncserver
~/noVNC/utils/novnc_proxy --vnc localhost:5901
