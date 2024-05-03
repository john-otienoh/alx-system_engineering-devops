# create a manifest that kills a process named killmenow.
$process_name = 'killmenow'

exec { "kill ${process_name}":
  command => "pkill -f ${process_name}",
  path    => ['/usr/bin/bash'],
}
