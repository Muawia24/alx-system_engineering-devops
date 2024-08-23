# Puppet script to fix "too many files user login error" 
exec {'open-file-limit':
command  => 'sed -i "s/nofile [0-9]\+/nofile 5000/" /etc/security/limits.conf',
provider => shell
}
