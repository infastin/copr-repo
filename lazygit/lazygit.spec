%global debug_package %{nil}

Name: lazygit
Version: 0.35
Release: 1%{?dist}
Summary: Simple terminal UI for git commands.

License: MIT
URL: https://github.com/jesseduffield/lazygit
Source0: https://github.com/jesseduffield/lazygit/archive/v%{version}.tar.gz

BuildRequires: golang

BuildArch: x86_64

%description
Simple terminal UI for git commands 

%prep
%setup -q

%build
go build

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 lazygit %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md CODE-OF-CONDUCT.md

%{_bindir}/lazygit

%changelog
* Wed 28 Sep 2022 06:02:38 AM +05 
- Release 0.35
