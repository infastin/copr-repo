%global debug_package %{nil}

Name: hdoc
Version: 1.4.0
Release: 1%{?dist}
Summary: The modern documentation tool for C++. 

License: GNU Affero General Public License v3.0
URL: https://hdoc.io/
Source0: https://github.com/hdoc/hdoc/archive/refs/tags/%{version}.tar.gz
Patch1: meson.patch
Patch0: argparse.patch

BuildRequires: llvm-devel
BuildRequires: clang-devel
BuildRequires: cmake
BuildRequires: meson
BuildRequires: openssl-devel
BuildRequires: zlib-devel
BuildRequires: vim-common

%description
The modern documentation tool for C++.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}
%{_bindir}/%{name}-online

%changelog
%autochangelog
