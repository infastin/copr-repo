%global debug_package %{nil}

Name: jetbrains-mono-nerd-fonts
Version: 2.2.2
Release: 1%{?dist}
Summary: A Nerd Font patched version of JetBrains Mono.

License: MIT
URL: https://github.com/ryanoasis/nerd-fonts
Source0: https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/JetBrainsMono.zip

%description
A Nerd Font patched version of JetBrains Mono.

%prep
%setup -q -c

%build
find -iname "*Windows Compatible.ttf" -delete

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts
install -m 0755 -d %{buildroot}%{_datadir}/fonts/%{name}
find -iname "*.ttf" -exec install -m 0644 {} %{buildroot}%{_datadir}/fonts/%{name} \;

%post
fc-cache -f -v

%postun
fc-cache -f -v

%files
%doc readme.md

%{_datadir}/fonts/%{name}

%changelog
* Wed 28 Sep 2022 03:55:53 AM +05
- Release 2.2.2