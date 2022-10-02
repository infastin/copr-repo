%global debug_package %{nil}

%global gitdate 20220920
%global githash f7bd4f25f3764883717c09a1fd867f560c9a9581
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: material-icons-fonts
Version: 4.0.0^%{gitdate}.%{shorthash}
Release: 9%{?dist}
Summary: Material Design icons by Google. 

License: Apache License 2.0
URL: https://github.com/google/material-design-icons
Source0: https://github.com/google/material-design-icons/archive/%{githash}.tar.gz

%description
Material Design icons by Google.

%prep
%setup -q -n material-design-icons-%{githash}

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts
install -m 0755 -d %{buildroot}%{_datadir}/fonts/%{name}
find -ipath './font/*.*tf' -exec install -m 0644 {} %{buildroot}%{_datadir}/fonts/%{name} \;

%post
fc-cache -f -v

%postun
fc-cache -f -v

%files
%license LICENSE
%doc README.md

%{_datadir}/fonts/%{name}

%changelog
* Wed 28 Sep 2022 03:55:53 AM +05
- Release 4.0.0^20220920.f7bd4f25f3
