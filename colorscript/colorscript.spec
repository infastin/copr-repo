%global debug_package %{nil}

%global gitdate 20230922
%global githash 43a8d9187253aaaf86bf664ac92011e6c66d94e3
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: colorscript
Version: 0^%{gitdate}.%{shorthash}
Release: 2%{?dist}
Summary: A collection of terminal color scripts.

License: MIT
URL: https://github.com/infastin/colorscript
Source0: %{url}/archive/%{githash}.tar.gz

BuildRequires: make

%description
A collection of terminal color scripts Derek Taylor accumulated over the years.
Some of them were cut out because of their size. This variation has 38 scripts in total.

%prep
%setup -q -n %{name}-%{githash}

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
%autochangelog
