%global tl_name titlepages
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Sample titlepages, and how to code them
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-samples/TitlePages
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepages.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titlepages.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The document provides examples of over two dozen title page designs
based on a range of published books and theses, together with the LaTeX
code used to create them.

