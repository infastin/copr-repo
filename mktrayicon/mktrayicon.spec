%global debug_package %{nil}

Name: mktrayicon
Version: 0.1.0
Release: 1%{?dist}
Summary: Create system tray icons by writing to a pipe.

License: MIT
URL: https://github.com/infastin/mktrayicon
Source0: %{url}/archive/v%{version}.tar.gz

Requires: gtk3

BuildRequires: gtk3-devel
BuildRequires: libX11-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf

%description
Create system tray icons by writing to a pipe.

%prep
%setup -q -n %{name}-%{version}

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
