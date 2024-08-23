# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix--requests-failure':
command  => 'sed -i "s/15/4096/" /etc/default/nginx; sudo service nginx restart',
provider => shell
}
