%global debug_package %{nil}

Name: bibata-cursor-theme
Version: 2.0.0
Release: %autorelease
Summary: Opensource, compact, and material designed cursor set. 

License: GNU General Public License v3.0
URL: https://github.com/ful1e5/Bibata_Cursor
Source0: https://github.com/ful1e5/Bibata_Cursor/releases/download/v%{version}/Bibata.tar.gz

%description
Opensource, compact, and material designed cursor set. 

%prep
%setup -q -c

%install
install -m 0755 -d %{buildroot}%{_datadir}/icons

for theme in *; do
	if ! [[ -d ${theme} ]]; then
		continue
	fi

	install -m 0755 -d %{buildroot}%{_datadir}/icons/${theme}
	install -m 0755 -d %{buildroot}%{_datadir}/icons/${theme}/cursors

	install -m 0644 ${theme}/cursor.theme %{buildroot}%{_datadir}/icons/${theme}
	install -m 0644 ${theme}/index.theme %{buildroot}%{_datadir}/icons/${theme}	

	for cursor in ${theme}/cursors/*; do
		install -m 0644 ${cursor} %{buildroot}%{_datadir}/icons/${theme}/cursors
	done
done

%files
%{_datadir}/icons/Bibata*

%changelog
%autochangelog
