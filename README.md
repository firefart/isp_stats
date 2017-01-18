# ISP STATS

![Grafana](/images/grafana.png?raw=true "Grafana")

## Using Vagrant
`vagrant up`

## Manual Ansible
* Install Ansible: http://docs.ansible.com/ansible/intro_installation.html#installing-the-control-machine
* `cd ansible`
* edit `hosts` and change IP address
* Be sure `root` login via SSH key is enabled on the remote machine and your public key is installed
* `ansible-playbook -i hosts site.yml`
* Open `http://ÌP/dashboard/db/isp-stats` in your browser
* Change the password of the `admin` user in the GUI
