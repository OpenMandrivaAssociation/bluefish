%define	version	2.2.3
%define	rel	1
%if %{mdkver} >= 201100
%define release %{rel}
%else
%define	release	%mkrel %rel
%endif

Summary:	Web development studio
Name:		bluefish
Version:	%{version}
Release:	%{release}
URL:		http://bluefish.openoffice.nl/
License:	GPLv2+
Group:		Networking/WWW
Source0:	http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
%if %{mdvver} <= 201100
BuildRequires:	gtk+2-devel >= 2.2.0
%else
BuildRequires:	gtk+3-devel
%endif
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

rm -f %{buildroot}%{_libdir}/%{name}/*.la
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
