# revision 19457
# category Package
# catalog-ctan /info/latex-samples/TitlePages
# catalog-date 2010-07-14 08:54:32 +0200
# catalog-license lppl
# catalog-version 2010-07-14
Name:		texlive-titlepages
Version:	20190228
Release:	1
Summary:	Sample titlepages, and how to code them
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/latex-samples/TitlePages
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepages.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepages.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100714-2
+ Revision: 756921
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100714-1
+ Revision: 719754
- texlive-titlepages
- texlive-titlepages
- texlive-titlepages

