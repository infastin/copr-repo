%global debug_package %{nil}

Name: jetbrains-mono-nerd-fonts
Version: 3.0.2
Release: 2%{?dist}
Summary: A Nerd Font patched version of JetBrains Mono.

License: SIL Open Font License 1.1
URL: https://github.com/ryanoasis/nerd-fonts
Source0: %{url}/releases/download/v%{version}/JetBrainsMono.zip

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
%license OFL.txt
%doc readme.md

%{_datadir}/fonts/%{name}

%changelog
%autochangelog
