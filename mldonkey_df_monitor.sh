#!/bin/sh

CACHEDIR="/var/cache/mldonkey"
MINFREE=102400

. /etc/sysconfig/mldonkey

[ ! "$ENABLE_DF_MONITOR" = "yes" ] && exit

send_email() {
	email=`grep "^ mail =" /var/lib/mldonkey/downloads.ini | sed 's/ mail = //g'`
	[ -n $email ] && mail -s "mldonkey, disk space warning" $email << EOF

your $CACHEDIR has only $CURFREE KiB free space left
all downloads paused

BTW: you can control this check by editing /etc/sysconfig/mldonkey.
EOF
}


CURFREE=`df -P -k $CACHEDIR | tail -n 1 | awk '{ print $4 }'`
if [ $CURFREE -lt $MINFREE ] ; then
	/etc/init.d/mldonkey pause > /dev/null
	send_email
fi

