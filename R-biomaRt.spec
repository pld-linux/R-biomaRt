%define		packname	biomaRt

Summary:	R Interface to BioMart databases
Name:		R-%{packname}
Version:	2.18.0
Release:	1
License:	Artistic 2.0
Group:		X11/Applications
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	2692dafbad92824a549ed451d5fccabc
URL:		http://www.bioconductor.org/packages/release/bioc/html/biomaRt.html
BuildRequires:	R-cran-RCurl
BuildRequires:	R-cran-XML
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-cran-RCurl
Requires:	R-cran-XML
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In recent years a wealth of biological data has become available in
public data repositories. Easy access to these valuable data resources
and firm integration with data analysis is needed for comprehensive
bioinformatics data analysis. biomaRt provides an interface to a
growing collection of databases implementing the BioMart software
suite (http://www.biomart.org). The package enables retrieval of large
amounts of data in a uniform way without the need to know the
underlying database schemas or write complex SQL queries. Examples of
BioMart databases are Ensembl, COSMIC, Uniprot, HGNC, Gramene,
Wormbase and dbSNP mapped to Ensembl. These major databases give
biomaRt users direct access to a diverse set of data and enable a wide
range of powerful online queries from gene annotation to database
mining.

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/scripts/
