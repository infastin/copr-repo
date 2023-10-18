%global debug_package %{nil}

Name: ctags
Version: 6.0.0
Release: 1%{?dist}
Summary: A maintained ctags implementation

License: GNU General Public License v2.0
URL: https://github.com/universal-ctags/ctags
Source0: https://github.com/universal-ctags/ctags/releases/download/v%{version}/universal-ctags-%{version}.tar.gz

BuildRequires: gcc make autoconf automake

%description
A maintained ctags implementation

%prep
%setup -q -n universal-ctags-%{version}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README.md

%{_bindir}/%{name}
%exclude %{_bindir}/optscript
%exclude %{_bindir}/readtags

%changelog
%autochangelog
