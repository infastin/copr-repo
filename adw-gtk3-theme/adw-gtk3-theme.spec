%global debug_package %{nil}

Name: adw-gtk3-theme
Version: 5.3
Release: 1%{?dist}
Summary: The theme from libadwaita ported to GTK-3.

License: GNU Lesser General Public License v2.1
URL: https://github.com/lassekongo83/adw-gtk3
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: sassc
BuildRequires: meson >= 0.51

%description
An unofficial GTK3 port of libadwaita.

%prep
%setup -q -n adw-gtk3-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md

%{_datadir}/themes/adw-gtk3*

%changelog
%autochangelog
