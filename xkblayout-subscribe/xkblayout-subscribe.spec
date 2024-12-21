%global debug_package %{nil}

Name: xkblayout-subscribe
Version: 0.1.0
Release: 1%{?dist}
Summary: A small command-line program to monitor keyboard layout changes.

License: MIT
URL: https://github.com/infastin/xkblayout-subscribe
Source0: %{url}/archive/v%{version}.tar.gz

Requires: libX11

BuildRequires: libX11-devel
BuildRequires: gcc
BuildRequires: make

%description
A small command-line program to monitor keyboard layout changes.

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags}

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%license LICENSE

%{_bindir}/%{name}

%changelog
%autochangelog
