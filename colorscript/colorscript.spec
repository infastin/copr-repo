%global debug_package %{nil}

Name: colorscript
Version: 0.1.0
Release: 1%{?dist}
Summary: A collection of terminal color scripts.

License: MIT
URL: https://github.com/infastin/colorscript
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: make

%description
A collection of terminal color scripts Derek Taylor accumulated over the years.
Some of them were cut out because of their size. This variation has 36 scripts in total.

%prep
%setup -q -n %{name}-%{version}

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
%autochangelog
