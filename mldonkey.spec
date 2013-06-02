Name:		mldonkey
Version:	3.1.3
Release:	1
Summary:	Door to the 'donkey' network
License:	GPLv2
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
#http://savannah.nongnu.org/download/mldonkey/%{name}-%{version}.tar.bz2
Source1:	%{name}-icon-16.png
Source2:	%{name}-icon-32.png
Source3:	%{name}-icon-48.png
Source4:	%{name}.init
Source5:	downloads.ini
Source6:	%{name}.sysconfig
Source7:	mlnet.sh
Source8:	mldonkey_df_monitor.crond
Source9:	mldonkey_df_monitor.sh
Source10:	mlgui.sh
Source11:	mldonkey.logrotate
URL:		http://sourceforge.net/projects/mldonkey/
#http://www.nongnu.org/mldonkey
Group:		System/Servers
BuildRequires:	camlp4
BuildRequires:	gd-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:  ocaml >= 3.10.2
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	bzip2-devel
BuildRequires:	magic-devel
Epoch:		1
Requires: 	netcat

%description
MLDonkey is a door to the 'donkey' network, a decentralized network used to
exchange big files on the Internet. It is written in a wonderful language,
called Objective-Caml, and present most features of the basic Windows donkey
client, plus some more:
  - It should work on most UNIX-compatible platforms.
  - You can remotely command your client, either by telnet, on a WEB browser,
    or with the GTK interface.
  - You can connect to several servers, and each search will query all the
     connected servers.
  - You can select mp3s by bitrates in queries (useful ?).
  - You can select the name of a downloaded file before moving it to your
    incoming directory.
  - You can have several queries in the graphical user interface at the same
     time.
  - You can remember your old queries results in the command-line interface.
  - You can search in the history of all files you have seen on the network.

It can also access other peer-to-peer networks:
- Direct Connect
- Open Napster
- Gnutella LimeWire
- Soulseek
- Audio Galaxy
- OpenFT
- Overnet
- Bittorent
- FileTP

%package gui
Summary:	Graphical frontend for mldonkey based on GTK
Group:		Networking/Other
Provides:	mldonkey-gui-i18n
Provides:       mldonkey-gui-i18n-de
Provides:       mldonkey-gui-i18n-es
Provides:       mldonkey-gui-i18n-fr
Provides:       mldonkey-gui-i18n-pt_BR
Provides:       mldonkey-gui-i18n-sv
Obsoletes:      mldonkey-gui-i18n-de
Obsoletes:      mldonkey-gui-i18n-es
Obsoletes:      mldonkey-gui-i18n-fr
Obsoletes:      mldonkey-gui-i18n-pt_BR
Obsoletes:      mldonkey-gui-i18n-sv

%description gui
The GTK interface for mldonkey provides a convenient way of managing
all mldonkey operations. It gives details about conected servers,
downloaded files, friends and lets one search for files in a pleasing
way.

%package init
Requires(pre):	rpm-helper
Summary:	Init to launch mldonkey
Group:		System/Servers
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description init
Contains init and configs to launch mldonkey as a service.

NOTE: by default incoming dir is located in /var/lib/mldonkey/incoming and
temp dir in /var/cache/mldonkey. Mlondkey is launched by daemon function
with mldonkey user (created in postinst script).

NOTE: If you are using a password for your mldonkey, you now need to specify
it in your /etc/sysconfig/mldonkey, because mldonkey now stores them crypted.

%package ed2k_submit
Summary:	This tool gives you an easy way to add a ed2k-link
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	perl-libwww-perl

%description ed2k_submit
This tool gives you an easy way to add an ed2k-link
(like ed2k://|file|filename.exe|21352658|72b0b287cab7d875ccc1d89ebe910b9g|)
with a single click to your mldonkey download queue.

You need to edit /etc/sysconfig/mldonkey_submit

%prep
%setup -q

%build
# Looks like autoconf, but isn't -- don't use the
# %%configure macros
CFLAGS="%optflags" CXXFLAGS="%optflags" \
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--enable-gui
%make

%install
rm -rf %{buildroot}

# core
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/%{name}
install -m 755 %{SOURCE7} %{buildroot}%{_bindir}/mlnet
install -m 755 mlnet %{buildroot}%{_libdir}/%{name}/mlnet
install -m 755 distrib/mldonkey_command %{buildroot}%{_bindir}/mldonkey_command
install -m 755 distrib/kill_mldonkey %{buildroot}%{_bindir}/kill_mldonkey

for link in mlbt mldonkey mlgnut; do
		ln -s mlnet %{buildroot}%{_libdir}/%{name}/$link ;
done

# gui
install -m 755 mlgui %{buildroot}%{_libdir}/%{name}/mlgui
install -m 755 mlguistarter %{buildroot}%{_libdir}/%{name}/mlguistarter
install -m 755 distrib/mldonkey_previewer %{buildroot}%{_bindir}/mldonkey_previewer
install -m 755 %{SOURCE10} %{buildroot}%{_bindir}/mlgui

# i18n
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 distrib/i18n/gui_messages.ini.de %{buildroot}%{_datadir}/%{name}/gui_messages.ini.de
install -m 644 distrib/i18n/gui_messages.ini.fr.noaccents %{buildroot}%{_datadir}/%{name}/gui_messages.ini.fr
install -m 644 distrib/i18n/gui_messages.ini.sp %{buildroot}%{_datadir}/%{name}/gui_messages.ini.es
install -m 644 distrib/i18n/gui_messages.ini.pt_BR %{buildroot}%{_datadir}/%{name}/gui_messages.ini.pt_BR
install -m 644 distrib/i18n/gui_messages.ini.sv %{buildroot}%{_datadir}/%{name}/gui_messages.ini.sv
install -m 644 distrib/i18n/gui_messages.ini.catalan %{buildroot}%{_datadir}/%{name}/gui_messages.ini.ca
install -m 644 distrib/i18n/gui_messages.ini.dutch %{buildroot}%{_datadir}/%{name}/gui_messages.ini.dutch
install -m 644 distrib/i18n/gui_messages.ini.ga %{buildroot}%{_datadir}/%{name}/gui_messages.ini.ga

# init
install -d -m 755 %{buildroot}%{_initrddir}
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/incoming
install -d -m 755 %{buildroot}%{_localstatedir}/cache/mldonkey
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/cron.d
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -m 755 %{SOURCE4} %{buildroot}%{_initrddir}/mldonkey
install -m 644 %{SOURCE5} %{buildroot}%{_localstatedir}/lib/%{name}/downloads.ini
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/mldonkey
install -m 644 %{SOURCE8} %{buildroot}%{_sysconfdir}/cron.d/mldonkey_df_monitor
install -m 755 %{SOURCE9} %{buildroot}%{_libdir}/%{name}/mldonkey_df_monitor.sh
install -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/logrotate.d/mldonkey

# macroize library dirs in scripts
perl -i -pe 's|/usr/lib/%{name}|%{_libdir}/%{name}|g' \
	%{buildroot}%{_bindir}/mlnet %{buildroot}%{_bindir}/mlgui \
	%{buildroot}%{_initrddir}/mldonkey \
	%{buildroot}%{_sysconfdir}/cron.d/mldonkey_df_monitor \
	%{buildroot}%{_localstatedir}/lib/%{name}/downloads.ini \
	%{buildroot}%{_libdir}/%{name}/mldonkey_df_monitor.sh

# ed2k_submit
install -d -m 755 %{buildroot}%{_datadir}/services/
install -m 755 distrib/ed2k_submit/mldonkey_submit %{buildroot}%{_bindir}/mldonkey_submit
install -m 644 distrib/ed2k_submit/mldonkey %{buildroot}%{_sysconfdir}/sysconfig/mldonkey_submit
install -m 644 distrib/ed2k_submit/ed2k.protocol  %{buildroot}%{_datadir}/services/ed2k.protocol

# menu
install %{SOURCE1} -D -m 644 %{buildroot}%{_miconsdir}/%{name}.png
install %{SOURCE2} -D -m 644 %{buildroot}%{_iconsdir}/%{name}.png
install %{SOURCE3} -D -m 644 %{buildroot}%{_liconsdir}/%{name}.png

install -d -m 755 %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}-gui.desktop
[Desktop Entry]
Name=Mldonkey GUI
Comment=Download files with Mldonkey
Exec=%{_bindir}/mlgui
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Network;FileTransfer;P2P;X-MandrivaLinux-Internet-FileTransfer;
EOF

%pre init
%_pre_useradd %{name} %{_localstatedir}/lib/%{name} /bin/bash

%post init
%_post_service %{name}

%preun init
%_preun_service %{name}

%postun init
%_postun_userdel %{name}

%post gui
%update_menus

%postun gui
%clean_menus

%files
%defattr(-,root,root)
%doc Copying.txt distrib/Authors.txt distrib/Bugs.txt distrib/ChangeLog
%doc distrib/Todo.txt distrib/ed2k_submit/README.MLdonkeySubmit distrib/Developers.txt
%doc docs
%{_bindir}/mlnet
%{_bindir}/mldonkey_command
%{_bindir}/kill_mldonkey
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/mlbt
%{_libdir}/%{name}/mldonkey
%{_libdir}/%{name}/mlgnut
%{_libdir}/%{name}/mlnet
#{_libdir}/%{name}/use_tags

%files gui
%defattr(-,root,root)
%doc Copying.txt distrib/Authors.txt distrib/Bugs.txt distrib/ChangeLog distrib/Developers.txt distrib/Todo.txt
%{_bindir}/mlgui*
%{_bindir}/mldonkey_previewer
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/mlgui
%{_libdir}/%{name}/mlguistarter
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/%{name}
%{_datadir}/applications/%{name}-gui.desktop

%files init
%defattr(-,root,root)
%doc Copying.txt
%attr(600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/cron.d/mldonkey_df_monitor
%config(noreplace) %{_initrddir}/mldonkey
%config(noreplace) %{_sysconfdir}/logrotate.d/mldonkey
%{_libdir}/%{name}/mldonkey_df_monitor.sh
%attr(600,mldonkey,mldonkey) %config(noreplace) %{_localstatedir}/lib/mldonkey/downloads.ini
%attr(770,mldonkey,mldonkey) %dir %{_localstatedir}/lib/%{name}/incoming
%attr(700,mldonkey,mldonkey) %dir %{_localstatedir}/cache/%{name}
%attr(710,mldonkey,mldonkey) %dir %{_localstatedir}/lib/%{name}

%files ed2k_submit
%defattr(-,root,root)
%doc Copying.txt distrib/ed2k_submit/README.MLdonkeySubmit
%config(noreplace) %{_sysconfdir}/sysconfig/mldonkey_submit
%{_bindir}/mldonkey_submit
%{_datadir}/services/ed2k.protocol

%clean
rm -rf %{buildroot}


%changelog
* Fri Jun 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:3.1.2-1
+ Revision: 803350
- Fix BuildRequires: to not install 32bit code on x86_64
- Fix unresolvable "kdebase" dependency in ed2k-submit
- Update to 3.1.2

* Mon Jan 16 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:3.1.0-1
+ Revision: 761807
- Clean up spec file
- Update to 3.1.0

* Fri Aug 05 2011 Andrey Bondrov <abondrov@mandriva.org> 1:3.0.7-1
+ Revision: 693323
- Add patch1 to fix gcc-4.6 build. Drop obsoleted chat package.
- imported package mldonkey


* Sat Jul 23 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1:3.0.7-1mdv2011.0
- New version 3.0.7
- Import from PLF
- Remove PLF reference

* Sat Oct 31 2009 Guillaume Rousse <guillomovitch@zarb.org> 1:3.0.1-1plf2010.0
- new version
- drop old configure patch
- drop old menu entry
- add libmagic support
- fix #250:
 - fix '%%{_localstatedir}' semantic change
 - fix log file handling in initscript

* Sun Mar 01 2009 Stefan van der Eijk <stefan@zarb.org> 1:3.0.0-1plf2009.1
- 3.0.0
- fix netcat dependency
