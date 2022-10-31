%global debug_package %{nil}

Name: adw-gtk3-theme
Version: 4.0
Release: 2%{?dist}
Summary: The theme from libadwaita ported to GTK-3.

License: GNU Lesser General Public License v2.1
URL: https://github.com/lassekongo83/adw-gtk3
Source0: https://github.com/lassekongo83/adw-gtk3/archive/refs/tags/v%{version}.tar.gz

BuildRequires: sassc
BuildRequires: meson >= 0.51

%description
The theme from libadwaita ported to GTK-3.

%prep
%setup -q -n adw-gtk3-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_datadir}/themes/adw-gtk3*

%changelog
%autochangelog
