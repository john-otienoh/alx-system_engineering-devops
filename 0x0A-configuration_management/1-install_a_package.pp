# Using Puppet, install flask from pip3.

$flask_version = '2.1.0'
package { 'flask':
  ensure   => $flask_version,
  provider => 'pip3',
}
