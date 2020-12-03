%define	modname	feedparser

Summary:	Parse RSS and Atom feeds in Python
Name:		python-%{modname}
Version:	6.0.2
Release:	1

Source0:	https://files.pythonhosted.org/packages/ca/f4/91a056f11751701c24f86c692d92fee290b0ba3f99f657cdeb85ad3da402/feedparser-%{version}.tar.gz
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
%setup -qn %{module}-%{version}

%build
%py_build

%install
%py_install

rm -Rf %{buildroot}%{py3_puresitedir}/__pycache__

%files
%defattr(644,root,root,755)
%doc python3/LICENSE python3/
%{py3_puresitedir}/%{modname}*
%{py3_puresitedir}/__pycache__/feedparser.cpython*
