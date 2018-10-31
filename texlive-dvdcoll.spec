Name:		texlive-dvdcoll
Version:	1.1a
Release:	2
Summary:	A class for typesetting DVD archives
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dvdcoll
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvdcoll.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvdcoll.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Having lost the overview of my DVD archives, I simply could not
remember if I already recorded the documentary running on TV
that day. I chose to recreate the index using LaTeX: the design
aim was a hyperlinked and fully searchable PDF-document,
listing my DVDs with all titles, lengths and so on. Further
requirements were support for seasons of tv series and a list
with all faulty or missing programs for rerecording. The
dvdcoll class supports all these requirements. dvdcoll.cls
follows the structure <number><title><length>. As a result, the
class is not limited to DVDs--you can of course typeset
archives of CD-ROMs, Audio-CDs and so on. Supported languages
at the moment: English, French, German, Italian, Polish,
Portuguese, Spanish. Some help is needed for other languages!.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/dvdcoll/dcbib.bst
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/UKenglish.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/USenglish.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/acadian.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/american.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/australian.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/austrian.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/brazil.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/brazilian.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/british.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/canadian.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/canadien.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/english.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/francais.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/french.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/frenchb.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/german.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/germanb.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/italian.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/naustrian.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/newzealand.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/ngerman.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/polish.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/portuges.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/portuguese.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcl/spanish.dcl
%{_texmfdistdir}/tex/latex/dvdcoll/dcwrtbib.sty
%{_texmfdistdir}/tex/latex/dvdcoll/dvdcoll.cls
%{_texmfdistdir}/tex/latex/dvdcoll/pdfnotiz.sty
%doc %{_texmfdistdir}/doc/latex/dvdcoll/CHANGES
%doc %{_texmfdistdir}/doc/latex/dvdcoll/INSTALL
%doc %{_texmfdistdir}/doc/latex/dvdcoll/README
%doc %{_texmfdistdir}/doc/latex/dvdcoll/dcexample.pdf
%doc %{_texmfdistdir}/doc/latex/dvdcoll/dcexample.tex
%doc %{_texmfdistdir}/doc/latex/dvdcoll/dvdcoll.pdf
%doc %{_texmfdistdir}/doc/latex/dvdcoll/dvdcoll_de.pdf
%doc %{_texmfdistdir}/doc/latex/dvdcoll/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.1a-2
+ Revision: 751175
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.1a-1
+ Revision: 718274
- texlive-dvdcoll
- texlive-dvdcoll
- texlive-dvdcoll
- texlive-dvdcoll

