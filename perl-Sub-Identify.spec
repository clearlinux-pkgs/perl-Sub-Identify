#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sub-Identify
Version  : 0.14
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/Sub-Identify-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/Sub-Identify-0.14.tar.gz
Summary  : 'Retrieve names of code references'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Sub-Identify-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# Sub::Identify
This perl module allows you to retrieve the real name of code references
as well as their original package and location. See the module's POD
documentation for examples.

%package dev
Summary: dev components for the perl-Sub-Identify package.
Group: Development
Requires: perl-Sub-Identify-lib = %{version}-%{release}
Provides: perl-Sub-Identify-devel = %{version}-%{release}

%description dev
dev components for the perl-Sub-Identify package.


%package lib
Summary: lib components for the perl-Sub-Identify package.
Group: Libraries

%description lib
lib components for the perl-Sub-Identify package.


%prep
%setup -q -n Sub-Identify-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Sub/Identify.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sub::Identify.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Sub/Identify/Identify.so
