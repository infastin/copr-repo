%global debug_package %{nil}

%global gitdate 20201002
%global githash 84290e8bcfd51093230b2ffdd3986c891a7fb485
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: xkblayout-subscribe
Version: 0^%{gitdate}.%{shorthash}
Release: 4%{?dist}
Summary: A small command-line program to monitor keyboard layout changes.

License: MIT
URL: https://git.sr.ht/~infastin/xkblayout-subscribe
Source0: %{url}/archive/%{githash}.tar.gz

Requires: libX11

BuildRequires: libX11-devel
BuildRequires: gcc
BuildRequires: make

%description
A small command-line program to monitor keyboard layout changes.

%prep
%setup -q -n %{name}-%{githash}

%build
make %{?_smp_mflags}

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%license LICENSE

%{_bindir}/%{name}

%changelog
%autochangelog
