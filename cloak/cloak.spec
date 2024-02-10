%global debug_package %{nil}

Name: cloak
Version: 2.7.0
Release: 1%{?dist}
Summary: A censorship circumvention tool to evade detection by authoritarian state adversaries.

License: GNU General Public License v3.0
URL: https://github.com/cbeuw/Cloak
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: golang >= 1.14.0
BuildRequires: git
BuildRequires: make

%description
A censorship circumvention tool to evade detection by authoritarian state adversaries.

%prep
%setup -q -n Cloak-%{version}

%build
go mod tidy
make %{?_smp_mflags}

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 build/ck-server %{buildroot}%{_bindir}
install -m 0755 build/ck-client %{buildroot}%{_bindir}

%files
%license LICENSE

%{_bindir}/ck-server
%{_bindir}/ck-client

%changelog
%autochangelog
