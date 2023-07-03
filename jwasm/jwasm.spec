%global debug_package %{nil}

Name: jwasm
Version: 2.17
Release: 1%{?dist}
Summary: Masm compatible assembler 

License: Sybase Open Watcom Public License version 1.0
URL: https://github.com/Baron-von-Riedesel/JWasm
Source0: https://github.com/Baron-von-Riedesel/JWasm/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
Masm compatible assembler

%prep
%setup -q -n JWasm-%{version}

%build
make -f GccUnix.mak

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 build/GccUnixR/jwasm %{buildroot}%{_bindir}

%files
%license Html/License.html
%doc README.md

%{_bindir}/%{name}

%changelog
%autochangelog
