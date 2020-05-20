# Get typos cleared
exec {'/var/www/html/wp-settings.php':
  command => '/bin/sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php'
}
