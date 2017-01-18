# ISP STATS

![Grafana](/images/grafana.png?raw=true "Grafana")

## Description
The following package is meant to provide an easy way to regularly measure your internet connection speed and create some stats.
You can easily set up this script on a raspberry pi with raspbian and keep it running in the background.

The data can be used to confront your ISP if your speed is way below the promised speed.

For setting up the machine you need a linux machine because ansible does not run on windows.

## Using Ansible
* Install Ansible: http://docs.ansible.com/ansible/intro_installation.html#installing-the-control-machine
* `cd ansible`
* edit `hosts` and change IP address
* Be sure `root` login via SSH key is enabled on the remote machine and your public key is installed
* `ansible-playbook -i hosts site.yml`
* Open `http://ÌP/dashboard/db/isp-stats` in your browser
* Change the password of the `admin` user in the GUI

## Using Vagrant
`vagrant up`
