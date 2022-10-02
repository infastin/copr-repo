%global debug_package %{nil}

Name: cbatticon
Version: 1.6.13
Release: 1%{?dist}
Summary: A lightweight and fast battery icon that sits in your system tray.

License: GNU General Public License v2.0 
URL: https://github.com/valr/cbatticon
Source0: https://github.com/valr/cbatticon/archive/%{version}.tar.gz

Requires: libnotify
Requires: gtk3

BuildRequires: gtk3-devel
BuildRequires: libnotify-devel
BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconf

%description
A lightweight and fast battery icon that sits in your system tray.

%prep
%setup -q

%build
make %{?_smp_mflags} WITH_NOTIFY=1 WITH_GTK3=1

%install
make PREFIX=%{buildroot}/%{_prefix} install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING

%{_docdir}/%{name}-%{version}/README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue 27 Sep 2022 06:46:21 PM +05 
- Release 1.6.13
