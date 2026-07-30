%define upstream_name    Sphinx-Config
%define upstream_version 0.10
Name:		perl-%{upstream_name}
Version:	0.10
Release:	1

Summary:	Sphinx search engine configuration file read/modify/write
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Sphinx-Config
Source0:	https://cpan.metacpan.org/authors/id/J/JJ/JJSCHUTZ/Sphinx-Config-0.10.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Test::Pod::Coverage)
BuildArch:	noarch

%description
Sphinx search engine configuration file read/modify/write.

%prep
%setup -q -n %{upstream_name}-%{version}

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

