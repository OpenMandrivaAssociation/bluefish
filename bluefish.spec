%define _disable_ld_no_undefined 1

Summary:	Web development studio
Name:		bluefish
Version:	2.2.4
Release:	7
URL:		http://bluefish.openoffice.nl/
License:	GPLv2+
Group:		Networking/WWW
Source0:	http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	aspell-devel
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gucharmap-2.90)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(python)
Requires:	python2
Suggests:	dos2unix
Suggests:	tidy
Suggests:	lynx

%description
Bluefish is a programmer's HTML editor, designed to save the experienced
webmaster some keystrokes.

It features a multiple file editor, multiple toolbars, custom menus, image
and thumbnail dialogs,  open from the web, HTML validation and lots of wizards.

This is not a WYSIWYG editor but a HTML editor (you edit the HTML code).

%prep
%setup -q

%build
%configure \
		--disable-update-databases --disable-splash-screen

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
