Name:		texlive-titlepages
Version:	19457
Release:	1
Summary:	Sample titlepages, and how to code them
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex-samples/TitlePages
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepages.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepages.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document provides examples of over two dozen title page
designs based on a range of published books and theses,
together with the LaTeX code used to create them.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/titlepages/README
%doc %{_texmfdistdir}/doc/latex/titlepages/titlepages.pdf
%doc %{_texmfdistdir}/doc/latex/titlepages/titlepages.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
