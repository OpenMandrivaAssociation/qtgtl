Summary:	Qtbindings for OpenGTL and OpenShiva
Name:		qtgtl
Version:	0.9.2
Release:	6
License:	GPLv2
Group:		System/Libraries
Source0:	http://download.opengtl.org/libQtGTL-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(OpenCTL)

%description
Qtbindings for OpenGTL and OpenShiva.

#------------------------------------------------------------------------------
%define qtgtl_major 0.1
%define libqtgtl %mklibname QtGTL %qtgtl_major

%package -n %{libqtgtl}
Summary:	Qtbinding for OpenGTL
Group:		System/Libraries

%description -n %{libqtgtl}
Qtbinding for OpenGTL.

%files -n %{libqtgtl}
%{_libdir}/libQtGTL.so.%{qtgtl_major}
%{_libdir}/libQtGTL.so.%{version}

#------------------------------------------------------------------------------
%define qtshiva_major 0.1
%define libqtshiva %mklibname QtShiva %qtshiva_major

%package -n %{libqtshiva}
Summary:	Qtbinding for OpenShiva
Group:		System/Libraries

%description -n %{libqtshiva}
Qtbinding for OpenShiva.

%files -n %{libqtshiva}
%{_libdir}/libQtShiva.so.%{qtshiva_major}
%{_libdir}/libQtShiva.so.%{version}

#------------------------------------------------------------------------------
%package devel
Summary:	Development files for Qtbindings for OpenGTL and OpenShiva
Group:		Development/KDE and Qt
Requires:	%{libqtgtl} = %{version}-%{release}
Requires:	%{libqtshiva} = %{version}-%{release}
Provides:	QtGTL-devel = %{version}-%{release}
Provides:	qtshiva-devel = %{version}-%{release}
Provides:	QtShiva-devel = %{version}-%{release}

%description devel
Development files for Qtbindings for OpenGTL and OpenShiva.

%files devel
%{_libdir}/*.so
%{_includedir}/QtGTL
%{_includedir}/QtShiva
%{_libdir}/pkgconfig/*.pc

#------------------------------------------------------------------------------

%prep
%setup -qn libQtGTL-%{version}

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

