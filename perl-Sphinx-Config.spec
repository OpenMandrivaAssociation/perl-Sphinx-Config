%define upstream_name    Sphinx-Config
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Sphinx search engine configuration file read/modify/write
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JJ/JJSCHUTZ/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl-Test-Pod-Coverage
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Sphinx search engine configuration file read/modify/write.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
