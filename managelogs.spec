%define major 2
%define libname %mklibname managelogs %{major}

Summary:	A log management software for apache
Name:		managelogs
Group:		System/Servers
Version:	2.2.0
Release:	%mkrel 1
License:	Apache license
URL:		http://managelogs.tekwire.net/
Source0:	managelogs-%{version}.tar.gz
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

%build
%serverbuild

%configure2_5x \
    --with-apr=%{_bindir}/apr-1-config \
    --with-zlib=%{_prefix} \
    --with-bz2=%{_prefix}

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanup devel crap
rm -f %{buildroot}%{_libdir}/*.*a
rm -f %{buildroot}%{_libdir}/*.so
rm -f %{buildroot}%{_includedir}/*.h

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
