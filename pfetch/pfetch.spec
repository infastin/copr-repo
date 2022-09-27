%global debug_package %{nil}

Name: pfetch
Version: 0.6.0
Release: 1%{?dist}
Summary: A pretty system information tool written in POSIX sh.

License: MIT
URL: https://github.com/dylanaraps/pfetch
Source0: https://github.com/dylanaraps/pfetch/archive/v%{version}.tar.gz

BuildArch: x86_64

%description
A pretty system information tool written in POSIX sh.

%prep
%setup -q

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 pfetch %{buildroot}%{_bindir}

%files
%license LICENSE.md
%doc README.md

%{_bindir}/pfetch

%changelog
* Wed 28 Sep 2022 03:55:53 AM +05
- Release 0.6.0
