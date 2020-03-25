# 6. Install Nginx web server (w/ Puppet)

package { 'nginx':
  ensure => installed,
  require => Package['nginx'],
}

file { '/usr/share/nginx/html/index.html':
  content => 'Holberton School',
  path    => '/usr/share/nginx/html/index.html'
}

file_line { 'redirect':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}
