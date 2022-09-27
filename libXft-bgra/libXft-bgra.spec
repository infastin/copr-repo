%global debug_package %{nil}

Name: libXft-bgra
Version: 2.3.3
Release: 1%{?dist}
Summary: A patched version of libxft that allows for colored emojis to be rendered in Suckless software.

License: Custom
URL: https://github.com/uditkarode/libxft-bgra
Source0: https://github.com/uditkarode/libxft-bgra/archive/072cd202c0.tar.gz

Provides: libXft

Requires: libX11
Requires: libXrender
Requires: fontconfig
Requires: freetype
Requires: libXext

BuildRequires: libXext-devel
BuildRequires: libX11-devel
BuildRequires: xorg-x11-util-macros
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: libXrender-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconf

BuildArch: x86_64

%package devel
Summary: Development files for %{name}-%{version}-%{release}.
Provides: libXft-devel

%description
A patched version of libxft that allows for colored emojis to be rendered in Suckless software.

%description devel
Development files for %{name}-%{version}-%{release}.

%prep
%setup -q -n libxft-bgra-072cd202c0f4f757b32deac531586bc0429c8401

%build
sh autogen.sh --sysconfdir=%{_sysconfdir}\
	--prefix=%{_prefix} --mandir=%{_mandir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

find $RPM_BUILD_ROOT -name "*.la" -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README.md NEWS

%{_prefix}/lib/libXft.so.%{version}
%{_prefix}/lib/libXft.so.%(echo %{version} | cut -d. -f1)
%{_prefix}/lib/libXft.so

%files devel
%{_mandir}/man3/Xft.3.gz
%{_prefix}/lib/libXft.a
%{_includedir}/X11/Xft/*
%{_prefix}/lib/pkgconfig/xft.pc

%changelog
* Tue 27 Sep 2022 11:09:16 PM +05
- Release 2.3.3
