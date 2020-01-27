%define _disable_ld_no_undefined 1

Summary:	Web development studio
Name:		bluefish
Version:	2.2.11
Release:	1
URL:		http://bluefish.openoffice.nl/
License:	GPLv2+
Group:		Networking/WWW
Source0:	http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
Patch0:     bluefish-2.2.11-no-python.patch
BuildRequires: pkgconfig(enchant-2)
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-unix-2.0) >= 2.16
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-2.0) >= 2.16
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gucharmap-2.90)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: intltool
BuildRequires: desktop-file-utils
BuildRequires:  libxml2-utils
BuildRequires:  man

Requires(post): libxml2-utils
Requires(postun): libxml2-utils

%description
Bluefish is a programmer's HTML editor, designed to save the experienced
webmaster some keystrokes.

It features a multiple file editor, multiple toolbars, custom menus, image
and thumbnail dialogs,  open from the web, HTML validation and lots of wizards.

This is not a WYSIWYG editor but a HTML editor (you edit the HTML code).

%prep
%autosetup -p0

# switch to enchant2
sed -e 's|\[enchant\]|\[enchant-2\]|g' -e 's|\[enchant >|\[enchant-2 >|g' \
    -e 's|enchant/enchant.h|enchant-2/enchant.h|g' -e 's|BF_dependencies enchant|BF_dependencies enchant-2|g' \
    -i configure.ac

%build
autoreconf -vfi
%configure \
    --disable-update-databases \
    --disable-xml-catalog-update \
    --disable-python
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%find_lang %{name} --all-name

desktop-file-install --dir %{buildroot}%{_datadir}/applications/ \
    %{buildroot}%{_datadir}/applications/*.desktop

%post
/usr/bin/xmlcatalog --noout --add 'delegateURI' \
    'http://bluefish.openoffice.nl/ns/bflang/2.0/' '%{_datadir}/xml/%{name}' \
    %{_sysconfdir}/xml/catalog > /dev/null || :

%postun
if [ "$1" = 0 ]; then
    /usr/bin/xmlcatalog --noout --del \
        'http://bluefish.openoffice.nl/ns/bflang/2.0/' \
        %{_sysconfdir}/xml/catalog > /dev/null || :
fi

%files -f %{name}.lang
%doc AUTHORS README ChangeLog NEWS TODO
%exclude /usr/share/doc/bluefish/bflang/sample.bflang2
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/xml/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
%{_datadir}/mime/packages/*
%{_mandir}/man1/%name.1.*
%{_iconsdir}/*/*/*/*
