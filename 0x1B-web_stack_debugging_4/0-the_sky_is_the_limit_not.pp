# 0. Sky is the limit, let's bring that limit higher

exec { 'raise-limits':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
  command => 'sed -ri "s/(ULIMIT=\"-n) [0-9]+/\1 10000/" /etc/default/nginx'
}

service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
}
