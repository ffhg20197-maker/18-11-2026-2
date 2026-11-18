#!/usr/bin/env sh
set -eu
if [ ! -f wp-config.php ]; then
  echo "ERROR: wp-config.php not found in current directory" >&2
  exit 1
fi
chmod 400 wp-config.php
chmod 644 .htaccess robots.txt
ls -l wp-config.php .htaccess robots.txt
