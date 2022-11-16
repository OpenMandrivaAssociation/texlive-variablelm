Name:		texlive-variablelm
Version:	60014
Release:	1
Summary:	Font definitions for the variable Latin Modern fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/variablelm
License:	gfl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/variablelm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/variablelm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a mechanism for scaling a typeface. It is
directed at the Latin Modern fonts and provides the font
definitions and the corresponding style file. This mechanism is
useful in mixed text compositions, for example Japanese-Latin.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/variablelm
%doc %{_texmfdistdir}/doc/fonts/variablelm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
