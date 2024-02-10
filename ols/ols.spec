%global debug_package %{nil}

%global gitdate 20240210
%global githash 7145764020fa463ee393b1f2701b1c151c162cce
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: ols
Version: 0^%{gitdate}.%{shorthash}
Release: 1%{?dist}
Summary: Language server for Odin.

License: MIT
URL: https://github.com/DanielGavin/ols
Source0: %{url}/archive/%{githash}.tar.gz

BuildRequires: odin
BuildRequires: clang

%description
Language server for Odin.

%prep
%setup -q -n %{name}-%{githash}

%build
./build.sh

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}

%changelog
%autochangelog
