%global debug_package %{nil}

Name: yandex-disk-indicator
Version: 1.11.0
Release: 1%{?dist}
Summary: Panel indicator (GTK+) for YandexDisk CLI client for Linux. 

License: GNU General Public License v3.0
URL: https://github.com/slytomcat/yandex-disk-indicator
Source0: https://github.com/slytomcat/yandex-disk-indicator/archive/%{version}.tar.gz

Requires: yandex-disk
Requires: gtk3
Requires: python3
Requires: pygobject2-devel
Requires: pygobject2
Requires: xclip
Requires: zenity
Requires: libappindicator-gtk3
Requires: libappindicator-gtk3-devel

%description
Panel indicator (GTK+) for YandexDisk CLI client for Linux. 

%prep
%setup -q

%install
pushd .
cd build
TARGET=%{buildroot}%{_prefix} sh prepare.sh
popd

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md

%{_bindir}/%{name}
%{_datadir}/applications/Yandex.Disk-indicator.desktop
%{_datadir}/yd-tools

%changelog
* Wed 28 Sep 2022 03:55:53 AM +05
- Release 1.11.0
