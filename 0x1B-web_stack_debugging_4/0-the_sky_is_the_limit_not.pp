# 0. Sky is the limit, let's bring that limit higher

exec { 'change ulimit':
  path    => '/bin',
  command => "sed -i 's/15/2000/g' /etc/default/nginx"
}

service { 'restart-nginx':
  name       => 'nginx',
  hasrestart => true
}
