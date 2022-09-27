Name: cbatticon
Version: 1.6.13
Release: 1
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

BuildArch: noarch

%description
A lightweight and fast battery icon that sits in your system tray.

%prep
%setup -q

%build
make %{?_smp_mflags} WITH_NOTIFY=1 WITH_GTK3=1

%install
make PREFIX=%{buildroot}/%{_prefix} install

%files
%license COPYRIGHT
%doc README
%{_bindir}/%{name}

%changelog
* Tue 27 Sep 2022 06:46:21 PM +05 
- Release 1.6.13
