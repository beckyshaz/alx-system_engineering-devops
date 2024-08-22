# Enable holberton user to open files without error

exec {'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/^holberton hard/s/5/70000/g" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

exec {'increase-soft-file-limit-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/70000/g" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
