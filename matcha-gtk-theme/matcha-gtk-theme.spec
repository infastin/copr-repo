%global debug_package %{nil}

%global gitversion 2024-05-01

Name: matcha-gtk-theme
Version: %(echo %{gitversion} | tr '-' '.')
Release: 1%{?dist}
Summary: Matcha is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell.

License: GNU General Public License v3.0
URL: https://github.com/vinceliuice/Matcha-gtk-theme
Source0: %{url}/archive/%{gitversion}.tar.gz

Requires: gtk-murrine-engine
Requires: gtk2-engines

%description
Matcha is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell

%prep
%setup -q -n Matcha-gtk-theme-%{gitversion}

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
