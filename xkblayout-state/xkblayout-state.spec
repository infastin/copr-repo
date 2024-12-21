%global debug_package %{nil}

Name: xkblayout-state
Version: 1.0.0
Release: 1%{?dist}
Summary: A small command-line program to get/set the current keyboard layout.

License: GNU General Public License v2.0
URL: https://github.com/infastin/xkblayout-state
Source0: %{url}/archive/v%{version}.tar.gz

Requires: libX11

BuildRequires: libX11-devel
BuildRequires: g++
BuildRequires: make

%description
A small command-line program to get/set the current keyboard layout.

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%doc README.md

%{_bindir}/%{name}

%changelog
%autochangelog
