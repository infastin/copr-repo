%global debug_package %{nil}

%global gitdate 20200807
%global githash 072cd202c0f4f757b32deac531586bc0429c8401 
%global shorthash %(echo %{githash} | cut -c 1-10)

Name: libXft-bgra
Version: 2.3.3^%{gitdate}.%{shorthash}
Release: 3%{?dist}
Summary: A patched version of libxft that allows for colored emojis to be rendered in Suckless software.

License: MIT
URL: https://github.com/uditkarode/libxft-bgra
Source0: https://github.com/uditkarode/libxft-bgra/archive/%{githash}.tar.gz

Provides: libXft(%{_arch})
Conflicts: libXft(%{_arch})

Requires: fontconfig >= 2.2-1

BuildRequires: make	
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: pkgconfig(xrender)
BuildRequires: freetype-devel >= 2.1.9-2
BuildRequires: fontconfig-devel >= 2.2-1

%package devel
Summary: Development files for %{name}-%{version}-%{release}.
Requires: %{name} = %{version}-%{release}

Provides: libXft-devel(%{_arch})
Conflicts: libXft-devel(%{_arch})

%description
A patched version of libxft that allows for colored emojis to be rendered in Suckless software.

%description devel
Development files for %{name}-%{version}-%{release}.

%prep
%setup -q -n libxft-bgra-%{githash}

%build
autoreconf -v --install --force
%configure
make %{?_smp_mflags} 

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

find $RPM_BUILD_ROOT -name "*.la" -delete

%ldconfig_post
%ldconfig_postun

%files
%license COPYING
%doc AUTHORS README.md NEWS

%{_libdir}/libXft.so.2*
%{_libdir}/libXft.so

%files devel
%{_mandir}/man3/Xft.3*
%{_libdir}/libXft.a
%{_includedir}/X11/Xft
%{_libdir}/pkgconfig/xft.pc

%changelog
%autochangelog
