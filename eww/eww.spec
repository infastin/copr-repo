%global debug_package %{nil}

Name: eww
Version: 0.4.0
Release: 1%{?dist}
Summary: ElKowars wacky widgets.

License: MIT
URL: https://github.com/elkowar/eww
Source0: https://github.com/elkowar/eww/archive/refs/tags/v%{version}.tar.gz

ExclusiveArch: %{rust_arches}

Requires: gtk3, pango, gdk-pixbuf2, cairo, glib2
Requires: glibc, libgcc

BuildRequires: gtk3-devel, pango-devel, gdk-pixbuf2-devel, cairo-devel, glib2-devel
BuildRequires: glibc-devel
BuildRequires: gtk-layer-shell-devel
BuildRequires: pkgconf
BuildRequires: curl
BuildRequires: gcc

%define BUILD_DIR %{_builddir}/%{name}
%define RUSTUP_HOME %{BUILD_DIR}/.rustup
%define CARGO_HOME %{BUILD_DIR}/.cargo
%define WAYLAND_PKG %{name}-wayland

%package -n %{WAYLAND_PKG}
Summary: %{name}-%{version}-%{release} with Wayland support.

%description
%{name}-%{version}-%{release} with Wayland support.

%description -n %{WAYLAND_PKG}
Elkowars Wacky Widgets is a standalone widget system made in Rust that allows you to implement your own,
custom widgets in any window manager.

%prep
%setup -q

export RUSTUP_HOME=%{RUSTUP_HOME}
export CARGO_HOME=%{CARGO_HOME}

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain none
%{CARGO_HOME}/bin/rustup toolchain install nightly

%build
export RUSTUP_HOME=%{RUSTUP_HOME}
export CARGO_HOME=%{CARGO_HOME}

%{CARGO_HOME}/bin/cargo build --release --target-dir=build
%{CARGO_HOME}/bin/cargo build --release --no-default-features --features=wayland --target-dir=build_wayland

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 build/release/eww %{buildroot}%{_bindir}/eww
install -m 0755 build_wayland/release/eww %{buildroot}%{_bindir}/eww-wayland

%files
%license LICENSE
%doc README.md

%{_bindir}/eww

%files -n %{WAYLAND_PKG}
%license LICENSE
%doc README.md

%{_bindir}/eww-wayland

%changelog
%autochangelog
