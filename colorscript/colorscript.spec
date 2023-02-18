%global debug_package %{nil}

%global gitdate 20220928
%global githash 3a255648d3b0fa9f804158d311b4f62bd61b227f
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: colorscript
Version: 0^%{gitdate}.%{shorthash}
Release: 4%{?dist}
Summary: A collection of terminal color scripts.

License: MIT
URL: https://git.sr.ht/~infastin/colorscript
Source0: https://git.sr.ht/~infastin/colorscript/archive/%{githash}.tar.gz

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
