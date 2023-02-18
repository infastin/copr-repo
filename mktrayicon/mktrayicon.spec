%global debug_package %{nil}

%global gitdate 20220927
%global githash 30a073d2eeab60416b3c2f2cd99176ff72ea1de9
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: mktrayicon
Version: 0^%{gitdate}.%{shorthash}
Release: 4%{?dist}
Summary: Create system tray icons by writing to a pipe. 

License: MIT
URL: https://git.sr.ht/~infastin/mktrayicon
Source0: https://git.sr.ht/~infastin/mktrayicon/archive/%{githash}.tar.gz

Requires: gtk3

BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf

%description
Create system tray icons by writing to a pipe. 

%prep
%setup -q -n %{name}-%{githash}

%build
make %{?_smp_mflags}

%install
make PREFIX=%{buildroot}%{_prefix} install

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}

%changelog
%autochangelog
