# first in terminal write  "pip install speedtest-cli"
from speedtest import Speedtest
import socket

# It's my variation about get information from speedtest-cli
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
st = Speedtest()
ip = st.get_config().get('client')

print("User name: ", hostname)
print("Local IP Address: ", IPAddr)
print("Public IP Address: ", ip.get('ip'))
print("ISP: ", ip.get('isp'))
print("Download:", '{:.2f}'.format(st.download() /1024 /1024), "Mb/s")
print("Upload:", '{:.2f}'.format(st.upload() /1024 /1024), "Mb/s")
print("Ping:",'{:.0f}'.format(st.results.ping), "ms")
