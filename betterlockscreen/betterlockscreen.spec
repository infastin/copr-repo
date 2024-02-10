%global debug_package %{nil}

Name: betterlockscreen
Version: 4.0.4
Release: 1%{?dist}
Summary: Sweet looking lockscreen for linux system.

License: MIT
URL: https://github.com/betterlockscreen/betterlockscreen
Source0: %{url}/archive/v%{version}.tar.gz

Requires: i3lock-color >= 2.13.c.3
Requires: xdpyinfo
Requires: xrandr
Requires: xrdb
Requires: xset
Requires: ImageMagick

BuildRequires: systemd
BuildRequires: systemd-rpm-macros

%description
Sweet looking lockscreen for linux system.

%prep
%setup -q

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}
install -m 0755 -d %{buildroot}%{_unitdir}
install -m 0644 system/%{name}@.service %{buildroot}%{_unitdir}

%post
%systemd_post %{name}@USER.service

%preun
%systemd_preun %{name}@USER.service

%postun
%systemd_postun %{name}@USER.service

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%doc examples

%{_bindir}/%{name}
%{_unitdir}/%{name}@.service

%changelog
%autochangelog
