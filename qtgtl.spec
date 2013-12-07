Summary: Qtbindings for OpenGTL and OpenShiva
Name: qtgtl
Version: 0.9.2
Release: 4
License: GPLv2
Group: System/Libraries
Source:	http://download.opengtl.org/libQtGTL-%{version}.tar.bz2
BuildRequires: qt4-devel
BuildRequires: cmake
BuildRequires: opengtl-devel >= 0.9.16

%description
Qtbindings for OpenGTL and OpenShiva.

#------------------------------------------------------------------------------
%define qtgtl_major 0.1
%define libqtgtl %mklibname QtGTL %qtgtl_major

%package -n %libqtgtl
Summary: Qtbinding for OpenGTL
Group: System/Libraries

%description -n %libqtgtl
Qtbinding for OpenGTL.

%files -n %libqtgtl
%defattr(-,root,root)
%{_libdir}/libQtGTL.so.%{qtgtl_major}
%{_libdir}/libQtGTL.so.%{version}

#------------------------------------------------------------------------------
%define qtshiva_major 0.1
%define libqtshiva %mklibname QtShiva %qtshiva_major

%package -n %libqtshiva
Summary: Qtbinding for OpenShiva
Group: System/Libraries

%description -n %libqtshiva
Qtbinding for OpenShiva.

%files -n %libqtshiva
%defattr(-,root,root)
%{_libdir}/libQtShiva.so.%{qtshiva_major}
%{_libdir}/libQtShiva.so.%{version}

#------------------------------------------------------------------------------
%package devel
Summary: Development files for Qtbindings for OpenGTL and OpenShiva
Group: Development/KDE and Qt
Requires: %libqtgtl = %version
Requires: %libqtshiva = %version
Provides: QtGTL-devel = %version-%release
Provides: qtshiva-devel = %version-%release
Provides: QtShiva-devel = %version-%release

%description devel
Development files for Qtbindings for OpenGTL and OpenShiva.

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/QtGTL
%{_includedir}/QtShiva
%{_libdir}/pkgconfig/*.pc

#------------------------------------------------------------------------------

%prep
%setup -q -n libQtGTL-%{version}

%build
%cmake_qt4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Wed Apr 18 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.9.2-1
+ Revision: 791693
- 0.9.2

* Sun Oct 24 2010 Funda Wang <fwang@mandriva.org> 0.9.1-3mdv2011.0
+ Revision: 589151
- we don't need this patch at the time

* Sun Oct 24 2010 Funda Wang <fwang@mandriva.org> 0.9.1-2mdv2011.0
+ Revision: 588936
- add upstream patch to build with latest opengtl

* Sat Apr 17 2010 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2010.1
+ Revision: 535931
- New version 0.9.1

* Fri Oct 09 2009 Funda Wang <fwang@mandriva.org> 0.9.0-1mdv2010.0
+ Revision: 456411
- import qtgtl

