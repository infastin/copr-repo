%global debug_package %{nil}

Name: lua-language-server
Version: 3.5.6
Release: %autorelease
Summary: A language server that offers Lua language support - programmed in Lua.

License: MIT
URL: https://github.com/sumneko/lua-language-server
Source0: https://github.com/sumneko/lua-language-server/releases/download/3.5.6/%{name}-%{version}-submodules.zip

BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-static

%description
A language server that offers Lua language support - programmed in Lua.

%prep
%setup -q -c

%build
cd 3rd/luamake
./compile/install.sh
cd ../..
./3rd/luamake/luamake

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 ./bin/lua-language-server %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md

%{_bindir}/lua-language-server

%changelog
%autochangelog
