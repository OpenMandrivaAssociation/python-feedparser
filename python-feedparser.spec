%define	modname	feedparser

Summary:	Parse RSS and Atom feeds in Python
Name:		python-%{modname}
Version:	6.0.10
Release:	3

Source0:	https://files.pythonhosted.org/packages/63/9a/824e3c036dec4f0adb4e7c36dcf4cbffc9ee317a4985218cb1663c7ab4ad/feedparser-6.0.10.tar.gz
License:	BSD
URL:		https://pypi.org/project/feedparser/
Group:		Development/Python
BuildRequires:  python-devel
BuildRequires: python3dist(setuptools)
BuildArch:	noarch
%rename		python3-%{modname}

%description
Feedparser is the "Universal Feed Parser" library for python, which
handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

%prep
%setup -qn %{modname}-%{version}

%build
%py_build

%install
%py_install

rm -Rf %{buildroot}%{py3_puresitedir}/__pycache__

%files
%defattr(644,root,root,755)
%{python_sitelib}/feedparser-%{version}-py*.*.egg-info/
%{python_sitelib}/feedparser/__init__.py
%{python_sitelib}/feedparser/api.py
%{python_sitelib}/feedparser/datetimes/*
%{python_sitelib}/feedparser/encodings.py
%{python_sitelib}/feedparser/exceptions.py
%{python_sitelib}/feedparser/html.py
%{python_sitelib}/feedparser/http.py
%{python_sitelib}/feedparser/mixin.py
%{python_sitelib}/feedparser/namespaces/*
%{python_sitelib}/feedparser/parsers/*
%{python_sitelib}/feedparser/sanitizer.py
%{python_sitelib}/feedparser/sgml.py
%{python_sitelib}/feedparser/urls.py
%{python_sitelib}/feedparser/util.py
