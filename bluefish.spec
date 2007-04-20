%define version 1.0.7
%define release %mkrel 1

Summary:	Web development studio
Name:		bluefish
Version:	%{version}
Release:	%{release}

URL:		http://bluefish.openoffice.nl/
License:	GPL
Group:		Networking/WWW
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		http://bluefish.openoffice.nl/download/%{name}-%{version}.tar.bz2

BuildRequires:	ImageMagick
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	pcre-devel
BuildRequires:	gnome-vfs2-devel >= 2.5.0
BuildRequires:	aspell-devel
BuildRequires:	gettext
BuildRequires:  desktop-file-utils

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

%build
sed -i "s/ICONDIR\/bluefish-icon.png/bluefish-icon.png/g;" data/bluefish.desktop.in
%configure --disable-update-databases --disable-splash-screen --enable-bookmarks

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# Menu item
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
 command="%{_bindir}/bluefish" \
 icon="bluefish.png" \
 needs="x11" \
 title="BlueFish" \
 longtitle="Web development studio" \
 section="Internet/Web Editors" \
 xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="WebDevelopment" \
  --add-category="Network" \
  --add-category="X-MandrivaLinux-Internet-WebEditors" \
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

%post
%update_menus
		
%postun
%clean_menus

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
%{_mandir}/man1/%name.1.bz2
%{_menudir}/%{name}
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png

