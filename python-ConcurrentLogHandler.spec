%define 	module	ConcurrentLogHandler
Summary:	Concurrent logging handler (drop-in replacement for RotatingFileHandler)
Name:		python-%{module}
Version:	0.8.4
Release:	1
License:	Apache 2.0
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/C/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	6d1665c645711380d29c06a7017eed49
URL:		http://pypi.python.org/pypi/ConcurrentLogHandler/
#BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Concurrent logging handler (drop-in replacement for
RotatingFileHandler).

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README PKG-INFO LICENSE

%{py_sitescriptdir}/cloghandler.*
%{py_sitescriptdir}/portalocker.*
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
