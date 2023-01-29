%global debug_package %{nil}

%global gitdate 20230129
%global githash 88df1e3ee7b0daf0ae4f4b6b7572a34fc2a5fb65
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: fdesktop
Version: 0^%{gitdate}.%{shorthash}
Release: 1%{?dist}
Summary: A command-line program that lists FreeDesktop desktop entries.

License: MIT
URL: https://gitlab.com/infastin/go-fdesktop
Source0: https://gitlab.com/infastin/go-fdesktop/-/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires: golang >= 1.18.0
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
