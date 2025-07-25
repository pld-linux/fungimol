# TODO: fix %%doc location
Summary:	An extensible system for designing atomic-scale objects
Summary(pl.UTF-8):	Rozszerzalny system do projektowania obiektów o skali atomu
Name:		fungimol
Version:	0.5.1
Release:	1
License:	LGPL
Group:		Applications/Engineering
Source0:	http://www.fungible.com/fungimol/%{name}-%{version}.tar.gz
# Source0-md5:	f1bc872b74c62a7bbdf8f1729ccacb46
Patch0:		%{name}-shared.patch
Patch1:		%{name}-static-init.patch
URL:		http://www.fungible.com/fungimol/index.html
BuildRequires:	XFree86-devel
BuildRequires:	gcc-g77
BuildRequires:	libstdc++-devel
BuildRequires:	netpbm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The intent is to eventually extend it to be a useful system for doing
molecular nanotechnology design work. At the moment it can view PDB
files, edit Buckminsterfullerines, and it has a plugin to do Brenner's
molecular dynamics force field.

Donald Brenner's Fortran molecular dynamics package is also included.

%description -l pl.UTF-8
Celem tego projektu jest ewentualne rozszerzenie, aby był przydatnym
systemem do wykonywania prac związanych z projektami z dziedziny
nanotechnologii molekularnej. W tej chwili można przeglądać pliki PDB,
modyfikować Buckminsterfullerine; ma wtyczką do obliczania sił
dynamiki molekularnej Brennera.

Dołączony jest także pakiet dynamiki molekularnej w Fortranie Donalnda
Brennera.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} fullbuild CPLUSPLUS=%{__cxx} %{!?debug:NDEBUG=yes}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_prefix}/doc/fungimol-0.5.1
%attr(755,root,root) %{_bindir}/*
%{_includedir}/fungimol
%{_datadir}/brennermd
%dir %{_datadir}/fungimol
%{_datadir}/fungimol/plugins
