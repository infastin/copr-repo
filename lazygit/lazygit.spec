%global debug_package %{nil}

Name: lazygit
Version: 0.35
Release: %autorelease
Summary: Simple terminal UI for git commands.

License: MIT
URL: https://github.com/jesseduffield/lazygit
Source0: https://github.com/jesseduffield/lazygit/archive/v%{version}.tar.gz

BuildRequires: golang >= 1.18.0

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
%autochangelog
