# rpizw-nifi-mqtt-gps
GPS Sensor Reading from Raspberry Pi Zero Wireless Sending via MQTT to Apache NiFi 1.x

sudo apt-get install gpsd gpsd-clients python-gps
sudo apt-get install ntp
pip install paho-mqtt

See:   http://www.danmandle.com/blog/getting-gpsd-to-work-with-python/

Build HDFS Directories

	[root@princeton10 centos]# su hdfs
	[hdfs@princeton10 centos]$ hdfs dfs -mkdir -p /rpwz/gps
	[hdfs@princeton10 centos]$ hdfs dfs -chmod -R 777 /rpwz/gps
  
Hardware

Raspberry Pi Zero Wireless
BU353-S4 USB GPS  (http://usglobalsat.com/p-688-bu-353-s4.aspx)

