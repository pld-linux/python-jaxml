%define		module	jaxml
Summary:	Module for automated generation of XML, XHTML or HTML documents
Summary(pl.UTF-8):	Moduł do automatycznego generowania dokumentów XML, XHTML lub HTML
Name:		python-%{module}
Version:	3.02
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/j/jaxml/jaxml-%{version}.tar.gz
# Source0-md5:	1526ccc4468342e3a39af6cebeab3dc8
URL:		http://www.librelogiciel.com/software/jaxml/action_Presentation
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JAXML is a Python module which makes the automated generation of XML,
XHTML or HTML documents easy.

%description -l pl.UTF-8
JAXML jest modułem dla Pythona, który upraszcza automatyczne
generowanie dokumentów XML, XHTML or HTML.

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
%doc CREDITS NEWS README
%{py_sitescriptdir}/jaxml.py[co]
%{py_sitescriptdir}/jaxml*.egg-info
