%global debug_package %{nil}

%global gitdate 20230719
%global githash 3072479c3c3c4818b0a41dc2aed288e8b3ec0582
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: odin
Version: 0^%{gitdate}.%{shorthash}
Release: 1%{?dist}
Summary: Odin Programming Language.

License: BSD 3-Clause License
URL: https://github.com/odin-lang/Odin
Source0: https://github.com/odin-lang/Odin/archive/%{githash}.tar.gz

BuildRequires: llvm14-devel
BuildRequires: llvm14
BuildRequires: clang
BuildRequires: make

%description
A fast, concise, readable, pragmatic and open sourced programming language.

%prep
%setup -q -n Odin-%{githash}

%build
make %{?_smp_mflags} PREFIX=%{buildroot}%{_prefix} release

%global optdir /opt/fedora/%{name}

%install
install -m 0755 -d %{buildroot}%{optdir}
install -m 0755 odin %{buildroot}%{optdir}
install -m 0755 -d %{buildroot}%{optdir}/core
cp -r core/ %{buildroot}%{optdir}/core
install -m 0755 -d %{buildroot}%{optdir}/shared
cp -r shared/ %{buildroot}%{optdir}/shared
install -m 0755 -d %{buildroot}%{_bindir}

%post
ln -sf %{optdir}/odin %{_bindir}

%postun
rm -f %{_bindir}/odin

%files
%license LICENSE
%doc README.md

%{optdir}
%{_bindir}

%changelog
%autochangelog
