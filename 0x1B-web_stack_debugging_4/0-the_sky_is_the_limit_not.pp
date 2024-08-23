# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
command => 'sed -i "s/ULIMIT=\"-n 4096\"/ULIMIT=\"-n 10000\"/" /etc/default/nginx && sudo service nginx restart',
path    => '/usr/local/bin/:/bin/'
}
