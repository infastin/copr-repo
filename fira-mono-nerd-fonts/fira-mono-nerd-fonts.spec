%global debug_package %{nil}

Name: fira-mode-nerd-fonts
Version: 2.3.3
Release: 2%{?dist}
Summary: A Nerd Font patched version of Fira Mono.

License: MIT
URL: https://github.com/ryanoasis/nerd-fonts
Source0: https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/FiraMono.zip

%description
A Nerd Font patched version of Fira Mono,

%prep
%setup -q -c

%build
find -iname "*Windows Compatible.otf" -delete
find -iname "Fura*.otf" -print0 | xargs -0 -I{} sh -c 'mv "$1" "${1//Fura/Fira}"' -- {}

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts
install -m 0755 -d %{buildroot}%{_datadir}/fonts/%{name}
find -iname "*.otf" -exec install -m 0644 {} %{buildroot}%{_datadir}/fonts/%{name} \;

%post
fc-cache -f -v

%postun
fc-cache -f -v

%files
%doc readme.md

%{_datadir}/fonts/%{name}

%changelog
%autochangelog
