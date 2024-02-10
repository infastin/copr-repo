%global debug_package %{nil}

%global gitdate 20240201
%global githash 539cec7496c128a0f8bb10794a1d3d0d043705f0
%global shorthash %(echo %{githash} | cut -c 1-10)

%define __check_files %{nil}
%define __spec_install_post %{nil}
%define __os_install_post %{nil}

Name: odin
Version: 0^%{gitdate}.%{shorthash}
Release: 3%{?dist}
Summary: Odin Programming Language.

License: BSD 3-Clause License
URL: https://github.com/odin-lang/Odin
Source0: %{url}/archive/%{githash}.tar.gz

BuildRequires: llvm14-devel
BuildRequires: clang
BuildRequires: make

%description
A fast, concise, readable, pragmatic and open sourced programming language.

%prep
%setup -q -n Odin-%{githash}

%build
make %{?_smp_mflags} PREFIX=%{buildroot}%{_prefix} release

%global libdir %{_libdir}/%{name}
%global __provides_exclude_from ^(%{libdir}/vendor/.*)$

%install
install -m 0755 -d %{buildroot}%{libdir}
install -m 0755 %{name} %{buildroot}%{libdir}
install -m 0755 -d %{buildroot}%{_bindir}
cp -r base/ %{buildroot}%{libdir}/
cp -r core/ %{buildroot}%{libdir}/
cp -r vendor/ %{buildroot}%{libdir}/

%post
ln -sf %{libdir}/%{name} %{_bindir}

%postun
if [[ "$1" -eq 0 ]]; then
  rm -f %{_bindir}/%{name} ;;
fi

%files
%license LICENSE
%doc README.md

%{libdir}

%changelog
%autochangelog
