%define	modname	feedparser

Summary:	Parse RSS and Atom feeds in Python
Name:		python-%{modname}
Version:	5.1.2
Release:	3

Source0:	http://pypi.python.org/packages/source/f/feedparser/%{modname}-%{version}.tar.bz2
License:	BSD
URL:		http://code.google.com/p/feedparser/
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
Feedparser is the "Universal Feed Parser" library for python, which
handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

%prep
%setup -q -n %{modname}-%{version}

%build
python setup.py build

%check
pushd feedparser
#    python feedparsertest.py
popd

%install
python setup.py install --root="%{buildroot}"

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{py_puresitedir}/*
