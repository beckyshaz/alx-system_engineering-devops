# Fixxing phpp extion with php

exec{'fixing-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/ :/bin'
}
