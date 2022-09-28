%global debug_package %{nil}

Name: colorscript
Version: 1.0.0
Release: 1%{?dist}
Summary: A collection of terminal color scripts.

License: MIT
URL: https://github.com/infastin/colorscript
Source0: https://github.com/infastin/colorscript/archive/%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

BuildArch: x86_64

%description
A collection of terminal color scripts Derek Taylor accumulated over the years.
Some of them were cut out because of their size. This variation has 38 scripts in total.

%prep
%setup -q

%install
make PREFIX=%{buildroot}/%{_prefix} install

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue 27 Sep 2022 10:03:56 PM +05
- Release 1.0.0
