%global debug_package %{nil}

%global gitdate 20221020
%global githash 886cfeacb5069510028e6bc1464e1b67da512932
%global shorthash %(echo %{githash} | cut -c 1-10)

%global zig_master zig-linux-x86_64-0.10.0-dev.4472+a4eb221b9

Name: zls
Version: 0.9.0^%{gitdate}.%{shorthash}
Release: %autorelease
Summary: Zig LSP implementation + Zig Language Server.

License: MIT
URL: https://github.com/zigtools/zls
Source0: https://github.com/zigtools/zls/archive/%{githash}.tar.gz
Source1: https://ziglang.org/builds/%{zig_master}.tar.xz

BuildRequires: git

%description
Zig Language Server, or zls, is a language server for Zig.

%prep
%setup -q -c

tar -xf %{SOURCE1}

git init
git remote add origin %{URL}.git
git fetch origin %{githash}
git reset --hard FETCH_HEAD
git submodule update --init --recursive

%build
./%{zig_master}/zig build -Drelease-safe

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 zig-out/bin/zls %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md

%{_bindir}/zls

%changelog
%autochangelog
