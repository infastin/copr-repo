%global debug_package %{nil}

Name: fira-code-nerd-fonts
Version: 2.3.3
Release: 1%{?dist}
Summary: A Nerd Font patched version of Fira Code.

License: MIT
URL: https://github.com/ryanoasis/nerd-fonts
Source0: https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/FiraCode.zip

%description
A Nerd Font patched version of Fira Code,

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
%autochangelog
