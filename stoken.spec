%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Token code generator compatible with RSA SecurID 128-bit (AES) token
Name:		stoken
Version:	0.92
Release:	1
Group:		Networking/Other
License:	LGPLv2+
Url:		https://github.com/cernekee/%{name}
Source0:	https://github.com/cernekee/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(hogweed)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(nettle)
BuildRequires:	pkgconfig(gmp)

%description
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

%package -n %{libname}
Summary:	Dynamic libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --with-gtk --disable-static
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete
rm -fr %{buildroot}%{_docdir}/%{name}

%files
%license COPYING.LIB
%doc CHANGES
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/applications/%{name}-gui-small.desktop
%{_datadir}/pixmaps/%{name}-gui.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}-gui.1*
%{_mandir}/man1/%{name}.1*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
