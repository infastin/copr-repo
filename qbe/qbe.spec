%global debug_package %{nil}

Name: qbe
Version: 1.1
Release: 1%{?dist}
Summary: A small compiler backend written in C.

License: MIT
URL: https://c9x.me/compile
Source0: https://c9x.me/compile/release/qbe-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: make

%description
QBE is a compiler backend that aims to provide 70% of the performance of
industrial optimizing compilers in 10% of the code. QBE fosters language
innovation by offering a compact user-friendly and performant backend.
The size limit constrains QBE to focus on the essential and prevents
embarking on a never-ending path of diminishing returns. 

%prep
%setup -q

%build
make CFLAGS="$CFLAGS -std=c11 -fPIE" %{?_smp_mflags}

%install
make PREFIX=%{buildroot}%{_prefix} install
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -r doc/ %{buildroot}/%{_docdir}/%{name}

%check
make check

%files
%license LICENSE
%doc README

%{_bindir}/%{name}
%{_docdir}/%{name}

%changelog
%autochangelog
