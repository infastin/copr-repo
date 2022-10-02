%global debug_package %{nil}

%global uuid com.github.GradienceTeam.Gradience

Name: gradience
Version: 0.3.0
Release: %autorelease
Summary: Gradience is a tool for customizing Libadwaita applications and the adw-gtk3 theme. 

License: GNU General Public License v3.0 
URL: https://github.com/GradienceTeam/Gradience
Source0: https://github.com/GradienceTeam/Gradience/archive/%{version}.tar.gz

Requires: python3
Requires: python3-gobject
Requires: gtk4 >= 4.5.0
Requires: libadwaita >= 1.2~alpha
Requires: hicolor-icon-theme
Requires: python3dist(aiohttp)
Requires: python3dist(anyascii) >= 0.3
Requires: python3dist(cssutils)
Requires: python3dist(jinja2)
Requires: python3dist(material-color-utilities-python)
Requires: python3dist(svglib)
Requires: python3dist(yapsy)

BuildRequires: sassc
BuildRequires: python3-devel
BuildRequires: pkgconfig
BuildRequires: blueprint-compiler
BuildRequires: python3-gobject-devel
BuildRequires: gtk4-devel
BuildRequires: meson
BuildRequires: libadwaita-devel
BuildRequires: python3
BuildRequires: python3-lxml
BuildRequires: desktop-file-utils

%description
Gradience is a tool for customizing Libadwaita applications and the adw-gtk3 theme.

%prep
%setup -q -n Gradience-%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md CODE_OF_CONDUCT.md CONTRIBUTING.md 
%doc ROADMAP.md SECURITY.md MAINTAINERS.md

%{_bindir}/gradience
%{python3_sitelib}/gradience
%{_datadir}/gradience
%{_datadir}/appdata/%{uuid}.appdata.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{uuid}*.svg

%changelog
%autochangelog
