# create a custom HTTP header response

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get update']
}

file_line { 'redirect':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'server_name _;',
    line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    require => Package['nginx'],
}

file_line { 'header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'server_name _;',
    line    => 'add_header X-Served-By "$HOSTNAME";',
    require => Package['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
