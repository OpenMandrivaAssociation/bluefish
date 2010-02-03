%define	version	2.0.0
%define betaver rc3
%define	rel	1
%define	release	%mkrel -c %betaver %rel

Summary:	Web development studio
Name:		bluefish
Version:	%{version}
Release:	%{release}
URL:		http://bluefish.openoffice.nl/
License:	GPLv2+
Group:		Networking/WWW
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}-%{betaver}.tar.bz2
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	pcre-devel
BuildRequires:	gnome-vfs2-devel >= 2.5.0
BuildRequires:	enchant-devel
BuildRequires:	aspell-devel
BuildRequires:	intltool
BuildRequires:	gucharmap-devel

%description
Bluefish is a programmer's HTML editor, designed to save the experienced
webmaster some keystrokes.

It features a multiple file editor, multiple toolbars, custom menus, image
and thumbnail dialogs,  open from the web, HTML validation and lots of wizards.

This is not a WYSIWYG editor but a HTML editor (you edit the HTML code).

%prep
%setup -qn %{name}-%{version}-%{betaver}

%build
%configure2_5x --disable-update-databases --disable-splash-screen
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}%{_libdir}/%{name}/*.la

%find_lang %{name} --all-name

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%update_mime_database
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%clean_mime_database
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
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
