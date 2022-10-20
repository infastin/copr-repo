%global debug_package %{nil}
%global __brp_check_rpaths %{nil}

%global gitdate 20221020
%global githash a4eb221b9ef7dab8fa1c6cc07c7891e25d98d2b6
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: zig
Version: 0.9.1^%{gitdate}.%{shorthash}
Release: %autorelease
Summary: General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.

License: MIT
URL: https://ziglang.org
Source0: https://github.com/ziglang/zig/archive/%{githash}.tar.gz
Source1: macros.%{name}

BuildRequires: lld-devel >= 15.0.0
BuildRequires: llvm-devel >= 15.0.0
BuildRequires: clang-devel >= 15.0.0
BuildRequires: cmake >= 2.8.12
BuildRequires: zlib-devel
BuildRequires: sed
BuildRequires: help2man

Requires: %{name}-libs = %{version}

%description
General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.

%package libs
Summary: %{name} Standard Library

%description libs
%{name} Standard Library

%package rpm-macros
Summary: Common RPM macros for %{name}
Requires: rpm

%description rpm-macros
This package contains common RPM macros for %{name}.

%prep
%setup -q -n zig-%{githash}

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DZIG_PREFER_CLANG_CPP_DYLIB=ON \
	-DZIG_STATIC_ZLIB=on
%cmake_build

%install
%cmake_install

help2man --no-discard-stderr %{buildroot}%{_bindir}/zig --version-option=version --output=%{name}.1

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -p -m644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/
sed -i -e "s|@@ZIG_VERSION@@|%{version}|"  %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name}

%files
%license LICENSE
%doc README.md

%{_bindir}/zig
%{_mandir}/man1/%{name}.1.*

%files libs
%{_prefix}/lib/%{name}

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.%{name}

%changelog
%autochangelog
