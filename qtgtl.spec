Summary: Qtbindings for OpenGTL and OpenShiva
Name: qtgtl
Version: 0.9.1
Release: %mkrel 2
License: GPLv2
Group: System/Libraries
Source:	http://www.opengtl.org/download/libQtGTL-%{version}.tar.bz2
Patch0: libQtGTL-0.9.0-linkage.patch
Patch1: http://bitbucket.org/opengtl/libqtgtl/changeset/f7913d273bb4/raw/libqtgtl-f7913d273bb4.diff
URL: http://opengtl.org/
BuildRequires: qt4-devel
BuildRequires: cmake
BuildRequires: opengtl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%patch0 -p0
%patch1 -p1

%build
%cmake_qt4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot
