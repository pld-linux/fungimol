Summary:	An extensible system for designing atomic-scale objects
Name:		fungimol
Version:	0.5.1
Release:	1
License:	LGPL
Group:		Applications/Engineering
Source0:	http://www.fungible.com/fungimol/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
Patch1:		%{name}-static-init.patch
URL:		http://www.fungible.com/fungimol/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	netpbm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	gcc-g77
BuildRequires:	XFree86-devel

%description
The intent is to eventually extend it to be a useful system for doing
molecular nanotechnology design work. At the moment it can view PDB
files, edit Buckminsterfullerines, and it has a plugin to do Brenner's
molecular dynamics force field.

Donald Brenner's Fortran molecular dynamics package is also included.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%{_datadir}/fungimol/plugins
