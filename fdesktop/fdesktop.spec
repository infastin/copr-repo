%global debug_package %{nil}

Name: fdesktop
Version: 0.1.1
Release: 1%{?dist}
Summary: A command-line program that lists FreeDesktop desktop entries.

License: MIT
URL: https://github.com/infastin/go-fdesktop
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: golang >= 1.21.0
BuildRequires: git

%description
A command-line program that lists FreeDesktop desktop entries.

%prep
%setup -q -n go-%{name}-%{version}

%build
go build -o ./build/ ./...

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 ./build/%{name} %{buildroot}%{_bindir}

%files
%license LICENSE

%{_bindir}/%{name}

%changelog
%autochangelog
