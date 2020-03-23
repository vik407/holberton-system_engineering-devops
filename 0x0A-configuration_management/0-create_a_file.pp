# Using Puppet, create a holberton file in /tmp.

file { 'holberton':
  path    => '/tmp/holberton',
  ensure  => file,
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
