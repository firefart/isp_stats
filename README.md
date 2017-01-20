# ISP STATS

![Grafana](/images/grafana.png?raw=true "Grafana")

## Description
The following package is meant to provide an easy way to regularly measure your internet connection speed and create some stats.
You can easily set up this script on a raspberry pi with raspbian and keep it running in the background.

The data can be used to confront your ISP if your speed is way below the promised speed.

For setting up the machine you need a linux machine because ansible does not run on windows.

The setup runs [speedtest-cli](https://github.com/sivel/speedtest-cli) every hour and collects the stats from the nearest [speedtest.net](http://www.speedtest.net/) server.
The data is written into a time series database ([InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/)) and displayed in a preconfigured dashboard using [Grafana](http://grafana.org/). You can also export all data from the dashboard as CSV for further offline processing.

**Hint:** If you want to use a raspberry and have a fast internet connection (>100Mbps) you need an external USB to Gigabit Ethernet adapter as the ethernet interface on the raspberry is only 100Mbs.

## Using Ansible
* Install Ansible: http://docs.ansible.com/ansible/intro_installation.html#installing-the-control-machine
* edit `ansible/hosts` and change IP address
* Be sure `root` login via SSH key is enabled on the remote machine and your public key is installed
* `ansible-playbook -i ansible/hosts ansible/site.yml`
* Open `http://ÌP/dashboard/db/isp-stats` in your browser
* The admin User is `admin`, the password can be found in `ansible/grafana_password` (do not delete this file!)
* All passwords and keys are generated on the first run so there are no default passwords to change after installation

## Using Vagrant
`vagrant up`

## Install on a raspberry pi
* download raspbian-lite and write image to sdcard https://www.raspberrypi.org/documentation/installation/installing-images/
* Create empty file in the mounted `boot` partition with name `ssh` without an extension to enable the ssh deamon on start
* Login via SSH with user `pi` and password `raspberry`
* sudo raspi-config
  * Expand Filesystem
  * Change User Password
  * Change Locale
  * Change Timezone
  * Finish --> Reboot
* `mkdir /root/.ssh` and add your public key to `/root/.ssh/authorized_keys`
* Run ansible as described above
