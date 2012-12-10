#!/bin/bash
# simple wrapper to set i18n in mldonkey_gui ( guillaume "dictateur" rousse idea )
# guillaume "dictateur" rousse code too, cause i'm too lame myself

MLDONKEY_GUI_HOME=/usr/share/mldonkey
MLDONKEY_GUI=/usr/lib/mldonkey/mlgui

if [ -f "$MLDONKEY_GUI_HOME/gui_messages.ini.${LANG}" ]; then
	MLDONKEY_GUI_MESSAGES=$MLDONKEY_GUI_HOME/gui_messages.ini.${LANG}
elif [ -f "$MLDONKEY_GUI_HOME/gui_messages.ini.${LANG%_*}" ]; then
	MLDONKEY_GUI_MESSAGES=$MLDONKEY_GUI_HOME/gui_messages.ini.${LANG%_*}
fi
export MLDONKEY_GUI_MESSAGES
exec $MLDONKEY_GUI
