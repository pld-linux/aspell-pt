Summary:	Portuguese dictionaries for aspell
Summary(pl):	Portugalskie s³owniki dla aspella
Name:		aspell-pt
Version:	0.0
%define	subv	3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://aspell.sourceforge.net/%{name}-%{version}-%{subv}.tar.bz2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell
Requires:	aspell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portuguese dictionaries (i.e. word lists) for aspell.

%description -l pl
Portugalskie s³owniki (listy s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f doc/README{,.dicts}
mv -f doc/BR/README{,.pt_BR}

gzip -9nf README Copyright doc/README.* doc/BR/README.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz doc/BR/*.gz
%{_libdir}/aspell/*
%{_datadir}/aspell/*
%{_datadir}/pspell/*
