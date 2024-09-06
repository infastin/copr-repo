%global debug_package %{nil}

%global gitdate 20240426
%global githash 4f1de19860e2b7d43d770d3a984d6537848d9cd8
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: matcha-gtk-theme
Version: 0^%{gitdate}.%{shorthash}
Release: 1%{?dist}
Summary: Matcha is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell.

License: GNU General Public License v3.0
URL: https://github.com/vinceliuice/Matcha-gtk-theme
Source0: %{url}/archive/%{githash}.tar.gz

Requires: gtk-murrine-engine
Requires: gtk2-engines

%description
Matcha is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell

%prep
%setup -q -n Matcha-gtk-theme-%{githash}

%install
install -m 0755 -d %{buildroot}%{_datadir}
install -m 0755 -d %{buildroot}%{_datadir}/themes
./install.sh -d %{buildroot}%{_datadir}/themes

%files
%license LICENSE
%doc README.md

%{_datadir}/themes/Matcha-*

%changelog
%autochangelog
