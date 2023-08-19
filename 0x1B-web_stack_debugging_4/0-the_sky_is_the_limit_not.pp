# Fix Nginx  message when simulting user requests

exec {'modify max open files limit setting':
  provider => shell
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart'
}
