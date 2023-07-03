%global debug_package %{nil}

Name: material-design-icons-font
Version: 7.2.96
Release: 1%{?dist}
Summary: 7000+ Material Design Icons from the Community.

License: Apache License 2.0
URL: https://pictogrammers.com/library/mdi/
Source0: https://github.com/Templarian/MaterialDesign-Webfont/archive/refs/tags/v%{version}.tar.gz

%description
7000+ Material Design Icons from the Community.

%prep
%setup -q -n MaterialDesign-Webfont-%{version}

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts
install -m 0755 -d %{buildroot}%{_datadir}/fonts/%{name}
find \( -iname "*.ttf" -o -iname "*.eot" -o -iname "*.woff2" -o -iname "*.woff" \) \
	-exec install -m 0644 {} %{buildroot}%{_datadir}/fonts/%{name} \;

%post
fc-cache -f -v

%postun
fc-cache -f -v

%files
%license LICENSE
%doc README.md

%{_datadir}/fonts/%{name}

%changelog
%autochangelog
