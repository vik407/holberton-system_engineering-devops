# 0. Sky is the limit, let's bring that limit higher

exec { 'raise-limits':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
  command => 'sed -i "s/-n 15/ -n 30000/g" /etc/default/nginx'
}

service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
}
