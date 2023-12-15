#
# Conditional build:
%bcond_without	apidocs		# documentation
%bcond_without	static_libs	# static libraries

Summary:	Library for Emulated Input
Summary(pl.UTF-8):	Biblioteka emulowanego wejścia
Name:		libei
Version:	1.2.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://gitlab.freedesktop.org/libinput/libei/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	80e375c002df47935f0b1ef40bdc03c5
URL:		https://libinput.pages.freedesktop.org/libei/
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	libevdev-devel
BuildRequires:	libxml2-progs
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.9
BuildRequires:	python3-attrs
BuildRequires:	python3-jinja2
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libei is a library for Emulated Input, primarily aimed at the Wayland
stack. It provides three parts:

- EI (Emulated Input) for the client side (libei)
- EIS (Emulated Input Server) for the server side (libeis)
- oeffis is an optional helper library for DBus communication with the
  XDG RemoteDesktop portal (liboeffis)

This package ships libei.

%description -l pl.UTF-8
libei to biblioteka emulowanego wejścia (Emulated Input), przeznaczona
głównie dla stosu Wayland. Składa się z trzech części:
- EI (Emulated Input) dla strony klienckiej (libei)
- EIS (Emulated Input Server) dla strony serwerowej (libeis)
- oeffis to opcjonalna biblioteka pomocnicza do komunikacji DBus z
  portalem XDG RemoteDesktop (liboeffis)

Ten pakiet dostarcza libei.

%package devel
Summary:	Development files for libei
Summary(pl.UTF-8):	Pliki programistyczne libei
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use libei.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących libei.

%package static
Summary:	Static libei library
Summary(pl.UTF-8):	Statyczna biblioteka libei
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libei library.

%description static -l pl.UTF-8
Statyczna biblioteka libei.

%package tools
Summary:	Utilities for libei
Summary(pl.UTF-8):	Narzędzia do libei
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description tools
Utilities for libei.

%description tools -l pl.UTF-8
Narzędzia do libei.

%package -n libeis
Summary:	Library for Emulated Input
Summary(pl.UTF-8):	Biblioteka emulowanego wejścia
Group:		Libraries

%description -n libeis
libei is a library for Emulated Input, primarily aimed at the Wayland
stack. It provides three parts:

- EI (Emulated Input) for the client side (libei)
- EIS (Emulated Input Server) for the server side (libeis)
- oeffis is an optional helper library for DBus communication with the
  XDG RemoteDesktop portal (liboeffis)

This package ships libeis.

%description -n libeis -l pl.UTF-8
libei to biblioteka emulowanego wejścia (Emulated Input), przeznaczona
głównie dla stosu Wayland. Składa się z trzech części:
- EI (Emulated Input) dla strony klienckiej (libei)
- EIS (Emulated Input Server) dla strony serwerowej (libeis)
- oeffis to opcjonalna biblioteka pomocnicza do komunikacji DBus z
  portalem XDG RemoteDesktop (liboeffis)

Ten pakiet dostarcza libeis.

%package -n libeis-devel
Summary:	Development files for libeis
Summary(pl.UTF-8):	Pliki programistyczne libeis
Group:		Development/Libraries
Requires:	libeis = %{version}-%{release}

%description -n libeis-devel
This package contains the header files for developing applications
that use libeis.

%description -n libeis-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących libeis.

%package -n libeis-static
Summary:	Static libeis library
Summary(pl.UTF-8):	Statyczna biblioteka libeis
Group:		Development/Libraries
Requires:	libeis-devel = %{version}-%{release}

%description -n libeis-static
Static libeis library.

%description -n libeis-static -l pl.UTF-8
Statyczna biblioteka libeis.

%package -n liboeffis
Summary:	Library for Emulated Input
Summary(pl.UTF-8):	Biblioteka emulowanego wejścia
Group:		Libraries

%description -n liboeffis
libei is a library for Emulated Input, primarily aimed at the Wayland
stack. It provides three parts:

- EI (Emulated Input) for the client side (libei)
- EIS (Emulated Input Server) for the server side (libeis)
- oeffis is an optional helper library for DBus communication with the
  XDG RemoteDesktop portal (liboeffis)

This package ships liboeffis.

%description -n liboeffis -l pl.UTF-8
libei to biblioteka emulowanego wejścia (Emulated Input), przeznaczona
głównie dla stosu Wayland. Składa się z trzech części:
- EI (Emulated Input) dla strony klienckiej (libei)
- EIS (Emulated Input Server) dla strony serwerowej (libeis)
- oeffis to opcjonalna biblioteka pomocnicza do komunikacji DBus z
  portalem XDG RemoteDesktop (liboeffis)

Ten pakiet dostarcza liboeffis.

%package -n liboeffis-devel
Summary:	Development files for liboeffis
Summary(pl.UTF-8):	Pliki programistyczne liboeffis
Group:		Development/Libraries
Requires:	liboeffis = %{version}-%{release}

%description -n liboeffis-devel
This package contains the header files for developing applications
that use liboeffis.

%description -n liboeffis-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących liboeffis.

%package -n liboeffis-static
Summary:	Static liboeffis library
Summary(pl.UTF-8):	Statyczna biblioteka liboeffis
Group:		Development/Libraries
Requires:	liboeffis-devel = %{version}-%{release}

%description -n liboeffis-static
Static liboeffis library.

%description -n liboeffis-static -l pl.UTF-8
Statyczna biblioteka liboeffis.

%package apidocs
Summary:	API documentation for libei library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libei
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libei library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libei.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	-Ddocumentation=%{?with_apidocs:api} \
	-Dliboeffis=enabled \
	-Dsd-bus-provider=libsystemd \
	-Dtests=disabled

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n libeis -p /sbin/ldconfig
%postun	-n libeis -p /sbin/ldconfig

%post	-n liboeffis -p /sbin/ldconfig
%postun	-n liboeffis -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_libdir}/libei.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libei.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libei.so
%dir %{_includedir}/libei-1.0
%{_includedir}/libei-1.0/libei.h
%{_pkgconfigdir}/libei-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libei.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ei-debug-events

%files -n libeis
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_libdir}/libeis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeis.so.1

%files -n libeis-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeis.so
%{_includedir}/libei-1.0/libeis.h
%{_pkgconfigdir}/libeis-1.0.pc

%if %{with static_libs}
%files -n libeis-static
%defattr(644,root,root,755)
%{_libdir}/libeis.a
%endif

%files -n liboeffis
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_libdir}/liboeffis.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboeffis.so.1

%files -n liboeffis-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboeffis.so
%{_includedir}/libei-1.0/liboeffis.h
%{_pkgconfigdir}/liboeffis-1.0.pc

%if %{with static_libs}
%files -n liboeffis-static
%defattr(644,root,root,755)
%{_libdir}/liboeffis.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc build/doc/html/*
%endif
