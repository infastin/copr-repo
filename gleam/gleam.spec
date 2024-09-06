%global debug_package %{nil}

Name: gleam
Version: 1.4.1
Release: 1%{?dist}
Summary: A friendly language for building type-safe, scalable systems!

License: Apache License 2.0
URL: https://gleam.run
Source0: https://github.com/gleam-lang/gleam/archive/v%{version}.tar.gz

Requires: erlang

BuildRequires: rustc
BuildRequires: cargo

%description
A friendly language for building type-safe, scalable systems!

%prep
%setup -q -n %{name}-%{version}

%build
export RUSTFLAGS="%build_rustflags"
cargo build --release

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENCE
%doc README.md

%{_bindir}/%{name}

%changelog
%autochangelog
