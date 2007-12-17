%define real_name Sphinx-Config

Summary:	Sphinx search engine configuration file read/modify/write
Name:		perl-%{real_name}
Version:	0.01
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JJ/JJSCHUTZ/%{real_name}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Pod-Coverage
BuildArch:	noarch

%description
Sphinx search engine configuration file read/modify/write.

%prep

%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Sphinx/Config.pm
%attr(0644,root,root) %{_mandir}/man3/Sphinx::Config.3pm*

