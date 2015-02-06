%define major 2
%define libname %mklibname managelogs %{major}

Summary:	A log management software for apache
Name:		managelogs
Group:		System/Servers
Version:	2.2.1
Release:	4
License:	Apache license
URL:		http://managelogs.tekwire.net/
Source0:	managelogs-%{version}.tar.gz
BuildRequires:	apr-devel
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel

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
export CFLAGS="%{optflags} -fPIC"

%configure2_5x \
    --with-apr=%{_bindir}/apr-1-config \
    --with-zlib=%{_prefix} \
    --with-bz2=%{_prefix}

%make CFLAGS="%{optflags} -fPIC"

%install
%makeinstall_std

# cleanup devel crap
rm -f %{buildroot}%{_libdir}/*.*a
rm -f %{buildroot}%{_libdir}/*.so
rm -f %{buildroot}%{_includedir}/*.h

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files
%defattr(-,root,root,-)
%{_bindir}/managelogs
%{_mandir}/man8/managelogs.8*


%changelog
* Thu Dec 02 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.2.1-2mdv2011.0
+ Revision: 605303
- Rebuild with apr with workaround to issue with gcc type based

* Mon Aug 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-1mdv2011.0
+ Revision: 568089
- 2.2.1

* Fri Apr 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-1mdv2010.1
+ Revision: 530766
- 2.2.0

* Thu Mar 11 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-1mdv2010.1
+ Revision: 518153
- 2.1.0

* Sun Feb 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-1mdv2010.1
+ Revision: 505802
- 2.0.0

* Sun Jan 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2010.1
+ Revision: 492873
- import managelogs


* Sun Jan 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdv2010.0
- initial Mandriva package
