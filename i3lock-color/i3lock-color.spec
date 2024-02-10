%global debug_package %{nil}

Name: i3lock-color
Version: 2.13.c.4
Release: 1%{?dist}
Summary: The world's most popular non-default computer lockscreen.

License: MIT
URL: https://github.com/Raymo111/i3lock-color
Source0: %{url}/archive/%{version}.tar.gz

Provides: i3lock

Requires: fontconfig
Requires: libXinerama
Requires: libXrandr

BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cairo-devel
BuildRequires: libev-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: pkgconf
BuildRequires: pam-devel
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-xrm-devel

%description
The world's most popular non-default computer lockscreen.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%doc README.md CHANGELOG SECURITY.md

%{_sysconfdir}/pam.d/i3lock
%{_bindir}/i3lock
%{_mandir}/man1/i3lock.1.gz

%changelog
%autochangelog
