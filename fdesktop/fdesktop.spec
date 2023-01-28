%global debug_package %{nil}

%global gitdate 20230129
%global githash 2e697541ab81a659e1bf9a1703ecdb99a3d5e9ce
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: fdesktop
Version: 0^%{gitdate}.%{shorthash}
Release: 1%{?dist}
Summary: A command-line program that lists FreeDesktop desktop entries.

License: MIT
URL: https://gitlab.com/infastin/go-fdesktop
Source0: https://gitlab.com/infastin/go-fdesktop/-/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires: golang >= 1.18.0

%description
A command-line program that lists FreeDesktop desktop entries.

%prep
%setup -q -n go-%{name}-%{githash}

%build
go build cmd/%{name}.go

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}

%changelog
%autochangelog
