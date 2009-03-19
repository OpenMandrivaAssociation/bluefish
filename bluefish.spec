%define version	1.0.7
%define rel	5
%define release	%mkrel %rel

Summary:	Web development studio
Name:		bluefish
Version:	%{version}
Release:	%{release}

URL:		http://bluefish.openoffice.nl/
License:	GPL
Group:		Networking/WWW
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		http://bluefish.openoffice.nl/download/%{name}-%{version}.tar.bz2
Patch0:		bluefish-1.0.7-fix-str-fmt.patch
BuildRequires:	imagemagick
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	pcre-devel
BuildRequires:	gnome-vfs2-devel >= 2.5.0
BuildRequires:	aspell-devel
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	autoconf

# Needs the mime directories
BuildRequires:	gnome-mime-data

%description
Bluefish is a programmer's HTML editor, designed to save the experienced
webmaster some keystrokes.

It features a multiple file editor, multiple toolbars, custom menus, image
and thumbnail dialogs,  open from the web, HTML validation and lots of wizards.

This is not a WYSIWYG editor but a HTML editor (you edit the HTML code).

%prep
%setup -q
%patch0 -p0

%build
sed -i "s/ICONDIR\/bluefish-icon.png/bluefish-icon.png/g;" data/bluefish.desktop.in
%configure2_5x --disable-update-databases --disable-splash-screen --enable-bookmarks

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

perl -pi -e 's/\..*// if /^Icon/' $RPM_BUILD_ROOT%{_datadir}/applications/*
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# Install icons
install -m 755 -d $RPM_BUILD_ROOT%{_iconsdir} \
                  $RPM_BUILD_ROOT%{_miconsdir}
install -m 644 -D       inline_images/bluefish_icon1.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -geometry 32x32 inline_images/bluefish_icon1.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -geometry 16x16 inline_images/bluefish_icon1.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

# Something is broken badly :)
rm -rf $RPM_BUILD_ROOT/home/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

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
%defattr(-,root,root,0755)
%doc AUTHORS README ChangeLog NEWS TODO
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/application-registry/*.applications
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*.png
%{_datadir}/mime/packages/*
%{_mandir}/man1/%name.1.*
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
