include Makefile_help.mak

install:$(call print-help,install           		,Installs all needed dependancies.)
	echo "Install needed support systems"
	sudo apt-get -y install sqlite3 gpsd gpsd-clients python-gps
	python makedb.py
	sed -i '/DEVICES/c\DEVICES="/dev/ttyUSB1"' /etc/default/gpsd
	service gpsd restart
	cp gps_sensor_service.conf /etc/supervisor/conf.d/
	/usr/bin/supervisorctl update
	/usr/bin/supervisorctl restart gps_sensor_service
	sed -i '/exit 0/d' /etc/rc.local 
	grep -qxF 'sudo python "/home/pi/gps_sensor_app/webapp.py" &' /etc/rc.local || echo 'sudo python "/home/pi/gps_sensor_app/webapp.py" &' >> /etc/rc.local
	echo "exit 0" >> /etc/rc.local
	kill $(netstat -ntpln | grep 80 | awk {'print $7'} | tr -dc '0-9') || true
	source /etc/rc.local
	echo "Installation completed successfully"

default: help
