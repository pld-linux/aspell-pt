Summary:	Portuguese dictionaries for aspell
Summary(pl):	Portugalskie s³owniki dla aspella
Summary(pt_BR):	Dicionário de português para o aspell
Name:		aspell-pt
Version:	0.50
%define	subv	2
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/pt/%{name}-%{version}-%{subv}.tar.bz2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portuguese dictionaries (i.e. word lists) for aspell.

%description -l pl
Portugalskie s³owniki (listy s³ów) dla aspella.

%description -l pt_BR
Dicionários da língua portuguesa para o verificador ortográfico
aspell.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/README.* doc/BR/README.*
%{_libdir}/aspell/*
%{_datadir}/aspell/*
