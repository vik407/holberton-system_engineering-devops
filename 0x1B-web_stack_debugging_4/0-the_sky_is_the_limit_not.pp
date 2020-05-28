# 0. Sky is the limit, let's bring that limit higher

exec { 'raise-limits':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'sed -i "s/15/4096/g" /etc/default/nginx'
}

exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
