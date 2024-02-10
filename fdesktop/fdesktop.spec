%global debug_package %{nil}

%global gitdate 20240128
%global githash 5b3b543b4abcd8056e9fab95ebaf1c3e54adc68b
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: fdesktop
Version: 0^%{gitdate}.%{shorthash}
Release: 1%{?dist}
Summary: A command-line program that lists FreeDesktop desktop entries.

License: MIT
URL: https://github.com/infastin/go-fdesktop
Source0: %{url}/archive/%{githash}.tar.gz

BuildRequires: golang >= 1.16.0
BuildRequires: git

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
%license LICENSE

%{_bindir}/%{name}

%changelog
%autochangelog
