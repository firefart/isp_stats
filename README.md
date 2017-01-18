# ISP STATS

![Grafana](/images/grafana.png?raw=true "Grafana")

## Description
The following package is meant to provide an easy way to regularly measure your internet connection speed and create some stats.
You can easily set up this script on a raspberry pi with raspbian and keep it running in the background.

The data can be used to confront your ISP if your speed is way below the promised speed.

For setting up the machine you need a linux machine because ansible does not run on windows.

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
