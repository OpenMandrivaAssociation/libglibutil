%define _empty_manifest_terminate_build 0

%define libname %mklibname glibutil
%define devname %mklibname -d glibutil

Name:           libglibutil
Version:        1.0.74
Release:        1
Summary:        Library of glib utilities
License:        BSD-3-Clause
URL:            https://github.com/sailfishos/libglibutil
Source:         https://github.com/sailfishos/libglibutil/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)

%description
Library of glib utilities.

%package -n %{libname}
Summary:        Library of glib utilities

%description -n %{libname}
Library of glib utilities.

%package -n %{devname}
Summary:        Devel library for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%autosetup -p1

%build
%make_build \
 LIBDIR=%{_libdir} \
 KEEP_SYMBOLS=1 \
 release \
 pkgconfig

%install
%make_install \
 LIBDIR=%{_libdir} \
 DESTDIR=%{buildroot} \
 install-dev


%files -n %{libname}
%license LICENSE
%doc README
%{_libdir}/*.so.*

%files -n %{devname}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}.so
%dir %{_includedir}/gutil
%{_includedir}/gutil/*.h
