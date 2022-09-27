%global debug_package %{nil}

Name: mktrayicon
Version: 1.0.0
Release: 1
Summary: Create system tray icons by writing to a pipe. 

License: MIT
URL: https://github.com/infastin/mktrayicon
Source0: https://github.com/infastin/mktrayicon/archive/%{version}.tar.gz

Requires: gtk3

BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf

BuildArch: x86_64

%description
Create system tray icons by writing to a pipe. 

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make PREFIX=%{buildroot}/%{_prefix} install

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}

%changelog
* Tue 27 Sep 2022 10:03:56 PM +05
- Release 1.0.0
