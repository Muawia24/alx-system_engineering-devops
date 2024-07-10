#  Add a custom HTTP header with Puppet
exec {'update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell'
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line {'add http header':
  ensure => 'present'
  path   => '/etc/nginx/nginx.conf',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $HOSTNAME;'
}
-> service {'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => package['nginx']
}
