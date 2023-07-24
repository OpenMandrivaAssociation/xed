# Build with python by default
%bcond_without python

Name:           xed
Version:        3.4.3
Release:        1
Summary:        A small and lightweight text editor
License:        GPLv2+
Group:          Editors
Url:            https://github.com/linuxmint/xed
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  mate-common
BuildRequires:  meson
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(xapp)
BuildRequires:  gnome-common
BuildRequires:  itstool
Requires:       typelib(PeasGtk)

%description
X-Apps Text Editor is a small, but powerful text editor designed
for the Cinnamon desktop and others. It has most standard text
editor functions and fully supports international text in Unicode.
Advanced features include syntax highlighting and automatic
indentation of source code, printing and editing of multiple
documents in one window.

X-Apps Text Editor is extensible through a plugin system, which
currently includes support for spell checking, comparing files,
viewing VCS ChangeLogs, and adjusting indentation levels.

%package devel
Summary:        Small and lightweight text editor
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description devel
X-Apps Text Editor is a small, but powerful text editor designed
for the Cinnamon desktop and others. It has most standard text
editor functions and fully supports international text in Unicode.
Advanced features include syntax highlighting and automatic
indentation of source code, printing and editing of multiple
documents in one window.

X-Apps Text Editor is extensible through a plugin system, which
currently includes support for spell checking, comparing files,
viewing VCS ChangeLogs, and adjusting indentation levels.


%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome


%files -f %{name}.lang
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_libdir}/%{name}/
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.x.editor.service
%{_mandir}/man?/%{name}.*
%{_datadir}/metainfo/xed.appdata.xml

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
