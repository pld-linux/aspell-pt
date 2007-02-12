Summary:	Portuguese dictionaries for aspell
Summary(pl.UTF-8):   Portugalskie słowniki dla aspella
Summary(pt_BR.UTF-8):   Dicionário de português para o aspell
Name:		aspell-pt
Version:	0.50
%define	subv	2
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/pt/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	e4e15179f90b76ec0336b687d1293edd
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portuguese dictionaries (i.e. word lists) for aspell.

%description -l pl.UTF-8
Portugalskie słowniki (listy słów) dla aspella.

%description -l pt_BR.UTF-8
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
