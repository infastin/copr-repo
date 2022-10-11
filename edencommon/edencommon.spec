%global debug_package %{nil}

Name: edencommon
Version: 2022.10.10.00
Release: %autorelease
Summary: Shared library for Watchman and Eden projects.

License: MIT
URL: https://github.com/facebookexperimental/edencommon
Source0: https://github.com/facebookexperimental/edencommon/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: folly-devel
BuildRequires: gmock-devel
BuildRequires: glog-devel
BuildRequires: gflags-devel

%package devel
Summary: Development files for %{name}-%{version}-%{release}.

%description
This contains various utility libraries common between EdenFS
and Watchman as well as utilities for clients of EdenFS or Watchman.

%description devel
Development files for %{name}-%{version}-%{release}.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md

%{_libdir}/libedencommon_utils.so

%files devel

%{_includedir}/eden/common
%{_prefix}/lib/cmake/%{name}

%changelog
%autochangelog
