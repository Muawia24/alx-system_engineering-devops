# Using strace, will find out why Apache is returning a 500 error
exec{'debug_error':
command => 'sudo sed -i s/pphp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
path    => ['/bin', '/usr/bin', '/usr/sbin']
}
