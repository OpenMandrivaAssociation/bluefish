%define _disable_ld_no_undefined 1

Summary:	Web development studio
Name:		bluefish
Version:	2.2.4
Release:	7
URL:		http://bluefish.openoffice.nl/
License:	GPLv2+
Group:		Networking/WWW
Source0:	http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
BuildRequires:	gtk+3-devel
BuildRequires:	pcre-devel
BuildRequires:	enchant-devel
BuildRequires:	aspell-devel
BuildRequires:	intltool
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	gucharmap-devel
%py_requires -d
Requires:	python
Suggests:	dos2unix tidy lynx

%description
Bluefish is a programmer's HTML editor, designed to save the experienced
webmaster some keystrokes.

It features a multiple file editor, multiple toolbars, custom menus, image
and thumbnail dialogs,  open from the web, HTML validation and lots of wizards.

This is not a WYSIWYG editor but a HTML editor (you edit the HTML code).

%prep
%setup -q

%build
%configure2_5x --disable-update-databases --disable-splash-screen
%make

%install
%makeinstall_std

for script in %{buildroot}%{_datadir}/bluefish/plugins/zencoding/filters/*.py \
	%{buildroot}%{_datadir}/bluefish/plugins/zencoding/actions/*.py \
	%{buildroot}%{_datadir}/bluefish/plugins/zencoding/resources.py \
	%{buildroot}%{_datadir}/bluefish/plugins/zencoding/utils.py \
	%{buildroot}%{_datadir}/bluefish/plugins/zencoding/html_matcher.py
do
[ -f "$script" ] && chmod +x "$script"
done

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/xml/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
%{_datadir}/mime/packages/*
%{_mandir}/man1/%name.1.*
%{_iconsdir}/*/*/*/*


%changelog
* Fri Jun 29 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.2.3-1mdv2012.0
+ Revision: 807508
- update to 2.2.3

* Sun Mar 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.2.2-1
+ Revision: 784096
- new version 2.2.2

* Fri Jan 27 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.2.1-1
+ Revision: 769266
- new version 2.2.1

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-2
+ Revision: 663326
- mass rebuild

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 2.0.3-1
+ Revision: 639840
- update to new version 2.0.3

* Thu Sep 16 2010 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2011.0
+ Revision: 578947
- new version 2.0.2

* Sun Jul 11 2010 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 550547
- update to new version 2.0.1

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 2.0.0-2mdv2010.1
+ Revision: 507041
- rebuild

* Tue Feb 16 2010 Frederik Himpe <fhimpe@mandriva.org> 2.0.0-1mdv2010.1
+ Revision: 506846
- Update to new version 2.0.0
- Does not need gnome-vfs now, it uses gio

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 2.0.0-0.rc3.1mdv2010.1
+ Revision: 500037
- 2.0.0 rc3

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix licence to GPLv2+

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-6mdv2010.0
+ Revision: 413176
- rebuild

* Thu Mar 19 2009 Funda Wang <fwang@mandriva.org> 1.0.7-5mdv2009.1
+ Revision: 357816
- fix str fmt

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.0.7-5mdv2009.0
+ Revision: 218428
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Jan 21 2008 Olivier Blin <blino@mandriva.org> 1.0.7-5mdv2008.1
+ Revision: 155558
- fix titypo
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - fix "error: (...)there should be no extension as described in the Icon Theme Specification if the value is not an absolute path"
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Funda Wang <fwang@mandriva.org> 1.0.7-4mdv2008.0
+ Revision: 77317
- Rebuild to obsolete old packages.

* Thu Aug 16 2007 Pascal Terjan <pterjan@mandriva.org> 1.0.7-3mdv2008.0
+ Revision: 64231
- Merge contrib and main packages
- Fix manpage listing
- Cosmetic fixes

* Fri Apr 20 2007 Eskild Hustvedt <eskild@mandriva.org> 1.0.7-1mdv2008.0
+ Revision: 16308
- New version 1.0.7


* Thu Sep 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.5-3mdv2007.0
- Fix BuildRequires

* Thu Sep 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.5-2mdv2007.0
- Use mkrel
- XDG

* Mon Mar 27 2006 Jerome Soyer <saispo@mandriva.org> 1.0.5-1mdk
- New release 1.0.5

* Sat Dec 10 2005 Eskild Hustvedt <eskild@mandriva.org> 1.0.4-1mdk
- New version 1.0.4

* Sun Jul 17 2005 Eskild Hustvedt <eskild@mandriva.org> 1.0.2-2mdk
- Drop ispell dependencies (fixes bug #15064)
- Spec cleanups

* Sat Jul 16 2005 Eskild Hustvedt <eskild@mandriva.org> 1.0.2-1mdk
- New version 1.0.2
- %%mkrel
- Drop COPYING (is in common-licenses)
- Drop Patch0
- Drop Patch1
- Fix menu

* Sun May 23 2004 Abel Cheung <deaddog@deaddog.org> 0.13-1mdk
- New version
- Patch0: No, bluefish doesn't need libintl, that's for OpenBSD!
- Patch1: Fix DESTDIR support
- Add many unreasonable buildrequires

* Fri Apr 30 2004 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.12-4mdk
- build for new gettext

* Mon Feb 09 2004 Olivier Blin <blino@mandrake.org> 0.12-3mdk
- fix Summary and menu section (move to Internet/Web editors)
- fix date in previous changelog entry

* Fri Jan 30 2004 Nicolas Planel <nplanel@mandrakesoft.com> 0.12-2mdk
- remove from Networking/WWW menu.

* Tue Nov 25 2003 Abel Cheung <deaddog@deaddog.org> 0.12-1mdk
- 0.12
- Use ImageMagick to convert icons
- BuildRequires fix for 64bit arch
- Turn on bookmark feature

* Fri Oct 31 2003 Jean-Michel Dault <jmdault@mandrakesoft.com> 0.11-4mdk
- disable annoying splash screen

