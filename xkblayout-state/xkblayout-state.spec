%global debug_package %{nil}

%global gitdate 20211106
%global githash f311779ed95f43f1fdebed0f710ad84057e6fe19
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: xkblayout-state
Version: 1b^%{gitdate}.%{shorthash}
Release: %autorelease
Summary: A small command-line program to get/set the current keyboard layout.

License: GNU General Public License v2.0 
URL: https://github.com/nonpop/xkblayout-state
Source0: https://github.com/nonpop/xkblayout-state/archive/%{githash}.tar.gz

Requires: libX11

BuildRequires: libX11-devel
BuildRequires: g++
BuildRequires: make

%description
A small command-line program to get/set the current keyboard layout.

%prep
%setup -q -n %{name}-%{githash}

%build
make %{?_smp_mflags}

%install
make PREFIX=%{buildroot}/%{_prefix} install

%files
%doc README.md

%{_bindir}/%{name}

%changelog
%autochangelog
