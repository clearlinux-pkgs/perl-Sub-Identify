#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sub-Identify
Version  : 0.12
Release  : 1
URL      : http://search.cpan.org/CPAN/authors/id/R/RG/RGARCIA/Sub-Identify-0.12.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/R/RG/RGARCIA/Sub-Identify-0.12.tar.gz
Summary  : Retrieve names of code references
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Sub-Identify-lib
Requires: perl-Sub-Identify-doc

%description
# Sub::Identify
This perl module allows you to retrieve the real name of code references
as well as their original package and location. See the module's POD
documentation for examples.

%package doc
Summary: doc components for the perl-Sub-Identify package.
Group: Documentation

%description doc
doc components for the perl-Sub-Identify package.


%package lib
Summary: lib components for the perl-Sub-Identify package.
Group: Libraries

%description lib
lib components for the perl-Sub-Identify package.


%prep
%setup -q -n Sub-Identify-0.12

%build
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Sub/Identify.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/auto/Sub/Identify/Identify.so
