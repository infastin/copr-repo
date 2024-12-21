%global debug_package %{nil}

%global crate shadowsocks-rust

Name: shadowsocks-rust
Version: 1.21.2
Release: 1%{?dist}
Summary: Shadowsocks is a fast tunnel proxy that helps you bypass firewalls.

License: MIT
URL: https://crates.io/crates/shadowsocks-rust
Source: %{crates_source}

BuildRequires: rustc >= 1.74
BuildRequires: cargo >= 1.74

%description
Shadowsocks is a fast tunnel proxy that helps you bypass firewalls.

%package -n %{crate}
Summary: %{summary}
License: MIT

%description -n %{crate}
Shadowsocks is a fast tunnel proxy that helps you bypass firewalls

%files -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/sslocal
%{_bindir}/ssmanager
%{_bindir}/ssserver
%{_bindir}/ssservice
%{_bindir}/ssurl

%prep
%autosetup -n %{crate}-%{version} -p1

%build
export RUSTFLAGS="%build_rustflags"
cargo build --release --features local-http,local-redir,local-tun

%install
make TARGET=release PREFIX=%{buildroot}%{_bindir} install

%changelog
%autochangelog
