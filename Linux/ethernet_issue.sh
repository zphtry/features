# Problems with ethernet connection can be caused by kernel and driver issues.
# In case your network controller is Realtek RTl8111 / 8168 / 8411 you can try follow theese steps:

# Update your kernel (I choosed last version 4.18.5-041805-generic) with ukuu
sudo apt-add-repository -y ppa:teejee2008/ppa 
sudo apt-get update
sudo apt-get install ukuu

# Download appropiate headers and install.
http://kernel.ubuntu.com/~kernel-ppa/mainline/

# Follow this guide
https://medium.com/@lgobinath/no-ethernet-connection-in-ubuntu-16-04-linux-mint-18-with-realtek-rtl8111-8168-8411-7ae2779dc9b8