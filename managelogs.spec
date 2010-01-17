%define major 1
%define libname %mklibname managelogs %{major}

Summary:	A log management software for apache
Name:		managelogs
Group:		System/Servers
Version:	1.0.1
Release:	%mkrel 1
License:	Apache license
URL:		http://managelogs.tekwire.net/
Source0:	managelogs-1.0.1.tar.gz
BuildRequires:	apr-devel
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
managelogs is a log management program for Apache, like rotatelogs and
cronolog. It allows to rotate and purge the Apache log files based on
different size limits. It also brings a lot of other features, like
running as a given non-root user, on-the-fly compression, maintaining
symbolic links on log files, ensuring that rotation occurs on line
boundaries, and more.

%package -n	%{libname}
Summary:	Shared library for managelogs
Group:		System/Libraries

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with managelogs.

%prep

%setup -q

find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

%build
make \
    CC_FLAGS="%{optflags}" \
    GZIP_LIBS="-lz" \
    BZ2_LIBS="-lbz2" \
    LIBTOOL="libtool" \
    APR_CONFIG="%{_bindir}/apr-1-config"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_mandir}/man8

libtool --silent --mode=install install lib/liblogmanager.la %{buildroot}%{_libdir}
libtool --silent --mode=install install src/managelogs %{buildroot}%{_bindir}
install -m0644 doc/managelogs.8 %{buildroot}%{_mandir}/man8/

# cleanup devel crap
rm -f %{buildroot}%{_libdir}/*.*a
rm -f %{buildroot}%{_libdir}/*.so

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files
%defattr(-,root,root,-)
%{_bindir}/managelogs
%{_mandir}/man8/managelogs.8*

