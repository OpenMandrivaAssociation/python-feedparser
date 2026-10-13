%define	modname	feedparser

Summary:	Parse RSS and Atom feeds in Python
Name:		python-%{modname}
Version:	6.0.14
Release:	1

Source0:	https://files.pythonhosted.org/packages/source/f/feedparser/feedparser-%{version}.tar.gz
License:	BSD-2-Clause
URL:		https://pypi.org/project/feedparser/
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(feedparser-sgmllib)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch
%rename		python3-%{modname}

%description
Feedparser is the "Universal Feed Parser" library for python, which
handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

%prep
%setup -qn %{modname}-%{version} -n feedparser-6.0.14

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/feedparser
%{python_sitelib}/feedparser-%{version}.dist-info
