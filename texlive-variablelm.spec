%global tl_name variablelm
%global tl_revision 60014

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Font definitions for the variable Latin Modern fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/variablelm
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/variablelm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/variablelm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a mechanism for scaling a typeface. It is directed
at the Latin Modern fonts and provides the font definitions and the
corresponding style file. This mechanism is useful in mixed text
compositions, for example Japanese-Latin.

