%define upstream_name    Sphinx-Config
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Sphinx search engine configuration file read/modify/write
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JJ/JJSCHUTZ/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Test::Pod::Coverage)
BuildArch:	noarch

%description
Sphinx search engine configuration file read/modify/write.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Sphinx/Config.pm
%attr(0644,root,root) %{_mandir}/man3/Sphinx::Config.3pm*

%changelog
* Sat Mar 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 648578
- update to new version 0.09
- update to new version 0.08

* Thu Aug 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 410706
- adding missing buildrequires:
- update to 0.05

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 404393
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-4mdv2009.0
+ Revision: 258357
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-3mdv2009.0
+ Revision: 246419
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Nov 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdv2008.1
+ Revision: 104412
- import perl-Sphinx-Config


* Thu Nov 01 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01-1mdv2008.1
- initial Mandriva package 
