%define		module	jaxml

Summary:	Module for automated generation of XML, XHTML or HTML documents
Summary(pl.UTF-8):	Moduł do automatycznego generowania dokumentów XML, XHTML lub HTML
Name:		python-%{module}
Version:	3.01
Release:	3
License:	LGPL
Group:		Libraries/Python
Source0:	http://www.librelogiciel.com/software/jaxml/tarballs/%{module}-%{version}.tar.gz
# Source0-md5:	87687c2bb5bceca0f93c53cd600ed9f1
URL:		http://www.librelogiciel.com/software/jaxml/action_Presentation
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
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
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS NEWS README
%{py_sitescriptdir}/jaxml.py[co]
%{py_sitescriptdir}/jaxml*.egg-info
