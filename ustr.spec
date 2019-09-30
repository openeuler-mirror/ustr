Name:      ustr
Version:   1.0.4
Release:   28
Summary:   Micro String API for C
License:   MIT or LGPLv2+ or BSD
URL:       http://www.and.org/ustr/
Source0:   http://www.and.org/ustr/%{version}/%{name}-%{version}.tar.bz2
#Acknowledge Patch0 from Fedora
Patch0:    c99-inline.patch

%description
 Micro string api is easier to be integrated into existing code
 than conventioal string api due to it's excellent compatibility.
 It takes fewer memory while being safer than just using string.h.

%package devel
Summary: Development files for ustr

Requires:  pkgconfig >= 0.14 %{name} = %{version}-%{release}
Provides:  ustr-static
Obsoletes: ustr-static

%description devel
Package devel includes development files like header files, static library
and ustr api import manner etc.

%package debug
Summary:   Development files for ustr
Requires:  pkgconfig >= 0.14 %{name}-devel = %{version}-%{release}
Provides:  ustr-debug-static
Obsoletes: ustr-debug-static

%description debug
Files for constructing debug function of ustr.

%package help
Summary:   Documents for ustr
%description help
It provides manualbook for ustr.



%prep
%autosetup -n %{name}-%{version} -p1

%build
%make_build  all-shared CFLAGS="${CFLAGS:-%optflags}  -fgnu89-inline" \
  LDFLAGS="$RPM_LD_FLAGS" HIDE=

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make $@ install-multilib-linux prefix=%{_prefix} \
                bindir=%{_bindir}         mandir=%{_mandir} \
                datadir=%{_datadir}       libdir=%{_libdir} \
                includedir=%{_includedir} libexecdir=%{_libexecdir} \
                DOCSHRDIR=%{_datadir}/doc/ustr-devel \
                DESTDIR=$RPM_BUILD_ROOT LDCONFIG=/bin/true HIDE=

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post debug -p /sbin/ldconfig

%postun debug -p /sbin/ldconfig

%files
%{_libdir}/libustr-1.0.so.*
%doc LICENSE* ChangeLog README NEWS


%files devel
%{_datadir}/ustr-%{version}
%{_bindir}/ustr-import
%{_libexecdir}/ustr-%{version}
%{_includedir}/ustr.h
%{_includedir}/ustr-*.h
%{_libdir}/pkgconfig/ustr.pc
%{_datadir}/doc/ustr-devel
%{_libdir}/libustr.a
%{_libdir}/libustr.so


%files debug
%{_libdir}/pkgconfig/ustr-debug.pc
%{_libdir}/libustr-debug.a
%{_includedir}/ustr*debug*.h
%{_libdir}/libustr-debug-1.0.so.*
%{_libdir}/libustr-debug.so


%files help
%{_mandir}/man1/*
%{_mandir}/man3/*



%changelog
* Tue Sep 3 2019 lizaiwang<lizaiwang1@huawei.com> - 1.0.4-28
- Init package
