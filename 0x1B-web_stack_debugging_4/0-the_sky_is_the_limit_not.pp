# 0. Sky is the limit, let's bring that limit higher

exec { 'raise-limits':
  path    => '/usr/bin:/bin:/usr/sbin',
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf;"
}

service { 'restart-nginx':
  name       => 'nginx',
  hasrestart => true
}
