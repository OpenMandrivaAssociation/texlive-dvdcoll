%global tl_name dvdcoll
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	A class for typesetting DVD archives
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dvdcoll
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvdcoll.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvdcoll.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Having lost the overview of my DVD archives, I simply could not remember
if I already recorded the documentary running on TV that day. I chose to
recreate the index using LaTeX: the design aim was a hyperlinked and
fully searchable PDF-document, listing my DVDs with all titles, lengths
and so on. Further requirements were support for seasons of tv series
and a list with all faulty or missing programs for rerecording. The
dvdcoll class supports all these requirements. dvdcoll.cls follows the
structure <number><title><length>. As a result, the class is not limited
to DVDs--you can of course typeset archives of CD-ROMs, Audio-CDs and so
on. Supported languages at the moment: English, French, German, Italian,
Polish, Portuguese, Spanish. Some help is needed for other languages!

