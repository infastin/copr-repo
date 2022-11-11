%global debug_package %{nil}

Name: elvish
Version: 0.18.0
Release: 1%{?dist}
Summary: Elvish = Expressive Programming Language + Versatile Interactive Shell

License: BSD 2-Clause
URL: https://elv.sh/
Source0: https://github.com/elves/elvish/archive/v%{version}.tar.gz

BuildRequires: golang >= 1.18.0

%description
Elvish is an expressive programming language and a versatile interactive shell, combined into one seamless package.

%prep
%setup -q

%build
go build ./cmd/elvish

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 elvish %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md

%{_bindir}/elvish

%changelog
%autochangelog
