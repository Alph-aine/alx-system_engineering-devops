# Fix 500 error when requesting from an Apache web server
exec {'replace':
  command => 'sed -i "s/\.phpp/\.php/g" /var/www/html/wp-settings.php'
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  }
