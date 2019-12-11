#! /bin/sh

if [ "$#" == 0 ]; then
	echo "Please enter an argument"
	echo "-restart to restart greengrass daemon"
	echo "-status to get status of daemon"
	echo "-tail to tail greengrass logs"
	echo "	tail will only work if tails have been enabled for lambda"	
exit
fi
if [ "$1" == "-start" ]; then
	cd /greengrass/ggc/core
	sudo ./greengrassd start
fi
if [ "$1" == "-stop" ]; then
	cd /greengrass/ggc/core
	sudo ./greengrassd stop
fi
if [ "$1" == "-restart" ]; then
	cd /greengrass/ggc/core
	sudo ./greengrassd restart
fi
if [ "$1" == "-status" ]; then
	ps aux |grep -E 'greengrass.*daemon'
fi
if [ "$1" == "-tail" ]; then
	# sudo chmod 777 /greengrass/ggc/var
	# You will have to change this log file to fit the path that your log files exist in
	# tail -f /greengrass/ggc/var/log/user/us-west-2/046241544403/GG_SensorData.log
fi
if [ "$1" == "-tail" ]; then
	# sudo chmod 777 /greengrass/ggc/var
	# You will have to change this log file to fit the path that your log files exist in
	# tail -f /greengrass/ggc/var/log/user/us-west-2/046241544403/GG_SensorData.log
fi




