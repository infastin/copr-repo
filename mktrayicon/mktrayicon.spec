%global debug_package %{nil}

Name: mktrayicon
Version: 1.0.0
Release: %autorelease
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
%autochangelog
