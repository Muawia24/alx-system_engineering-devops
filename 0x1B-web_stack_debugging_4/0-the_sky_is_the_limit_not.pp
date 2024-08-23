# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
command => 'sed -i "s/worker_connections [0-9]\+/worker_connections 100/" /etc/nginx/nginx.conf && sudo service nginx restart',
path    => '/usr/local/bin/:/bin/'
}
